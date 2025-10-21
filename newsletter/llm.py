from __future__ import annotations

import logging
from typing import List, Dict, Any

from .config import Settings


logger = logging.getLogger(__name__)


def chat_completion(settings: Settings, system: str, user: str) -> str:
    provider = settings.llm_provider.lower()
    if provider == "openai":
        return _openai_chat(settings, system, user)
    elif provider == "anthropic":
        return _anthropic_chat(settings, system, user)
    else:
        raise ValueError(f"Unsupported llm_provider: {settings.llm_provider}")


def _openai_chat(settings: Settings, system: str, user: str) -> str:
    try:
        from openai import OpenAI
    except Exception as e:  # pragma: no cover
        raise RuntimeError("openai package not installed") from e

    if not settings.openai_api_key:
        raise RuntimeError("Missing OPENAI_API_KEY for OpenAI provider")

    client = OpenAI(api_key=settings.openai_api_key)
    logger.debug("Calling OpenAI model %s", settings.llm_model)

    try:
        resp = client.chat.completions.create(
            model=settings.llm_model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=settings.llm_temperature,
        )
        return resp.choices[0].message.content or ""
    except Exception as e:
        logger.error(f"OpenAI API failed: {e}")
        raise ValueError(f"LLM generation failed: {str(e)}") from e


def _anthropic_chat(settings: Settings, system: str, user: str) -> str:
    try:
        import anthropic
    except Exception as e:  # pragma: no cover
        raise RuntimeError("anthropic package not installed") from e

    if not settings.anthropic_api_key:
        raise RuntimeError("Missing ANTHROPIC_API_KEY for Anthropic provider")

    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
    logger.debug("Calling Anthropic model %s", settings.llm_model)

    try:
        msg = client.messages.create(
            model=settings.llm_model,
            max_tokens=2048,
            temperature=settings.llm_temperature,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        # content is a list of blocks; assemble text
        parts: List[str] = []
        for block in msg.content:
            if getattr(block, "type", "") == "text":
                parts.append(getattr(block, "text", ""))
        return "".join(parts)
    except Exception as e:
        logger.error(f"Anthropic API failed: {e}")
        raise ValueError(f"LLM generation failed: {str(e)}") from e

