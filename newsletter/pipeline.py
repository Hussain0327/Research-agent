from __future__ import annotations

import json
import logging
import os
import re
from collections import OrderedDict
from urllib.parse import urlparse
from typing import List, Dict, Tuple

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .config import Settings
from .llm import chat_completion
from .models import (
    FormInput,
    PlanOutput,
    SectionPlan,
    SectionDraft,
    Newsletter,
)
from .search import tavily_search


logger = logging.getLogger(__name__)


PLAN_SYSTEM = (
    "# Overview\n"
    "You plan a newsletter table of contents tailored to topic, tone, and audience.\n\n"
    "# Instructions\n"
    "- Analyze topic, tone, and audience.\n"
    "- Brainstorm 4-6 engaging sections.\n"
    "- Output strict JSON with key newsletterSections (list of {title, description}).\n"
)


SECTION_SYSTEM = (
    "# Role\nYou write the final newsletter section content (no prefacing).\n\n"
    "# Rules\n"
    "- Use provided Tavily research.\n"
    "- Inline cite via HTML <a href> links for any claims.\n"
    "- Audience-aware tone.\n"
    "- Return well-formed HTML only (no <html> wrapper).\n"
)


TITLE_SYSTEM = (
    "Create a concise, title-case subject for an email newsletter. "
    "Output plain text only, no quotes."
)


def _ensure_json(text: str) -> PlanOutput:
    """Extract PlanOutput JSON from text."""
    # Attempt direct JSON first
    try:
        obj = json.loads(text)
        return PlanOutput(**obj)
    except Exception:
        pass
    # Fallback: extract JSON block
    m = re.search(r"\{[\s\S]*\}$", text.strip())
    if m:
        try:
            obj = json.loads(m.group(0))
            return PlanOutput(**obj)
        except Exception:
            pass
    raise ValueError("Could not parse plan JSON from LLM output")


def plan_sections(settings: Settings, form: FormInput) -> List[SectionPlan]:
    user = (
        f"Topic: {form.topic}\n"
        f"Tone: {form.tone}\n"
        f"Audience: {form.audience}\n\n"
        "Output JSON strictly like: {\n  \"newsletterSections\": [\n    {\"title\": \"...\", \"description\": \"...\"}\n  ]\n}"
    )
    resp = chat_completion(settings, PLAN_SYSTEM, user)
    plan = _ensure_json(resp)
    if not plan.newsletterSections:
        raise ValueError("No sections planned")
    logger.info("Planned %d sections", len(plan.newsletterSections))
    # Cap at 6 sections to keep within word limits
    return plan.newsletterSections[:6]


def draft_section(settings: Settings, form: FormInput, section: SectionPlan) -> SectionDraft:
    # Research via Tavily
    query = f"{form.topic} — {section.title}. {section.description} Audience: {form.audience}."
    results = tavily_search(settings, query)
    # Build research context
    research_lines = []
    sources: List[str] = []
    for i, r in enumerate(results, start=1):
        research_lines.append(f"[Source {i}] URL: {r.url}\nTitle: {r.title or ''}\nContent: {r.content or ''}")
        sources.append(str(r.url))
    research_block = "\n\n".join(research_lines) if research_lines else "(no external sources available)"

    # Compose user prompt
    per_section_cap = settings.per_section_word_target
    user = (
        f"Section Title: {section.title}\n"
        f"Section Description: {section.description or ''}\n"
        f"Audience: {form.audience}\n"
        f"Tone: {form.tone}\n"
        f"Hard limit: {per_section_cap} words.\n"
        "Write 1-3 concise paragraphs. Include inline hyperlink citations for information that relies on research.\n\n"
        f"Research:\n{research_block}"
    )
    html_body = chat_completion(settings, SECTION_SYSTEM, user).strip()

    # Extract links from html for sources list; keep only absolute http(s) URLs
    urls = OrderedDict()
    # Support both single and double quotes around href values
    for url in re.findall(r'href=[\'"]([^\'"]+)[\'"]', html_body):
        parsed = urlparse(url)
        if parsed.scheme in ("http", "https") and parsed.netloc:
            urls[url] = None

    cleaned_sources = list(urls.keys())
    return SectionDraft(title=section.title, html=html_body, sources=cleaned_sources or [])


def _count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def compose_subject(settings: Settings, form: FormInput, html_body: str) -> str:
    # Provide the newsletter body and context for subject generation
    snippet = re.sub(r"<[^>]+>", " ", html_body)
    snippet = re.sub(r"\s+", " ", snippet).strip()
    user = (
        f"Tone: {form.tone}\nAudience: {form.audience}\n"
        f"Newsletter excerpt: {snippet[:1500]}"
    )
    subject = chat_completion(settings, TITLE_SYSTEM, user).strip()
    # Title case-ish normalization
    subject = subject.strip().strip('"').strip("'")
    return subject


def render_html(settings: Settings, subject: str, sections: List[SectionDraft]) -> Tuple[str, Dict[str, str]]:
    # Aggregate sources from sections, preserving order and uniqueness (keys as strings)
    agg_sources: Dict[str, str] = OrderedDict()
    for s in sections:
        for url in s.sources:
            url_str = str(url)  # coerce HttpUrl -> str (or keep str as-is)
            if url_str not in agg_sources:
                agg_sources[url_str] = ""

    # Sort sources alphabetically by URL for stability
    agg_sources = OrderedDict(sorted(agg_sources.items(), key=lambda kv: kv[0]))

    env = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    tpl = env.get_template("newsletter.html.j2")
    html_out = tpl.render(subject=subject, sections=sections, sources=agg_sources)
    # Word control: ensure content length
    if _count_words(re.sub(r"<[^>]+>", " ", html_out)) > settings.max_words:
        logger.warning("Newsletter exceeds max_words; content may need trimming.")
    return html_out, agg_sources


def run_pipeline(settings: Settings, form: FormInput) -> Newsletter:
    sections = plan_sections(settings, form)
    drafts: List[SectionDraft] = []
    for sec in sections:
        drafts.append(draft_section(settings, form, sec))

    # Compose subject after drafts, then render
    # Use section titles to bias the subject as well
    subject_hint = ", ".join(s.title for s in drafts)
    subject = compose_subject(settings, form, "\n".join(d.html for d in drafts))
    if not subject:
        subject = f"{form.topic.strip().title()} — {subject_hint[:60]}"

    html_out, sources = render_html(settings, subject, drafts)

    # Defensive: ensure string keys/values for Pydantic model
    sources = {str(k): ("" if v is None else str(v)) for k, v in (sources or {}).items()}

    return Newsletter(subject=subject, html=html_out, sources=sources)
