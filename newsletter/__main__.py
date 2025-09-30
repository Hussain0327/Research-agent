from __future__ import annotations

import argparse
import logging
import os
from pathlib import Path

from dotenv import load_dotenv

from .config import Settings
from .models import FormInput
from .pipeline import run_pipeline
from .emailer import send_email
from .pipeline import plan_sections
from .models import SectionPlan


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate and send a research-backed newsletter")
    p.add_argument("--topic", required=True, help="Newsletter topic")
    p.add_argument("--tone", required=True, help="Tone (e.g., Professional, Funny)")
    p.add_argument("--audience", required=True, help="Target audience description")
    p.add_argument("--to", nargs="*", help="Email recipients (optional)")
    p.add_argument("--send-email", action="store_true", help="Send via SMTP if configured")
    p.add_argument("--provider", choices=["openai", "anthropic"], help="LLM provider override")
    p.add_argument("--model", help="LLM model override")
    p.add_argument("--output-dir", help="Directory to write outputs")
    return p.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()

    settings = Settings()
    if args.provider:
        settings.llm_provider = args.provider
    if args.model:
        settings.llm_model = args.model
    if args.output_dir:
        settings.output_dir = args.output_dir
    settings.validate_provider_keys()

    logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO))

    form = FormInput(topic=args.topic, tone=args.tone, audience=args.audience)
    # Run and also persist debug artifacts
    newsletter = run_pipeline(settings, form)

    out_dir = Path(settings.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "subject.txt").write_text(newsletter.subject, encoding="utf-8")
    (out_dir / "newsletter.html").write_text(newsletter.html, encoding="utf-8")

    print(f"Subject: {newsletter.subject}")
    print(f"Wrote HTML: {out_dir / 'newsletter.html'}")

    if args.send_email and args.to:
        send_email(settings, newsletter.subject, newsletter.html, args.to)
        print(f"Email sent to: {', '.join(args.to)}")
    elif args.send_email:
        print("--send-email provided but --to is empty; skipped sending.")


if __name__ == "__main__":  # pragma: no cover
    main()
