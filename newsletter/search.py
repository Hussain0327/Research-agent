from __future__ import annotations

import hashlib
import json
import logging
import os
from typing import List

import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from .config import Settings
from .models import SearchResult


logger = logging.getLogger(__name__)


def _cache_path(settings: Settings, query: str) -> str:
    os.makedirs(".cache/tavily", exist_ok=True)
    key = hashlib.sha256(query.encode("utf-8")).hexdigest()
    return os.path.join(".cache/tavily", f"{key}.json")


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=8), reraise=True,
       retry=retry_if_exception_type(requests.RequestException))
def tavily_search(settings: Settings, query: str) -> List[SearchResult]:
    """Search Tavily with simple on-disk caching."""
    cache_file = _cache_path(settings, query)
    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                cached = json.load(f)
                return [SearchResult(**r) for r in cached]
        except Exception:
            pass

    if not settings.tavily_api_key:
        logger.warning("No TAVILY_API_KEY set; returning empty results for query: %s", query)
        return []

    payload = {
        "api_key": settings.tavily_api_key,
        "query": query,
        "search_depth": "basic",
        "include_answer": True,
        "topic": "news",
        "include_raw_content": True,
        "max_results": settings.tavily_max_results,
    }
    resp = requests.post(settings.tavily_endpoint, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("results", [])[: settings.tavily_max_results]:
        results.append(
            SearchResult(
                url=item.get("url"),
                title=item.get("title") or None,
                content=item.get("content") or None,
            )
        )

    # write cache
    try:
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump([r.model_dump() for r in results], f)
    except Exception:
        pass

    return results
