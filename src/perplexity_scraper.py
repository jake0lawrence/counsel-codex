"""Fetch AI-law links using Perplexity search."""

from __future__ import annotations

import os
import requests  # type: ignore
from typing import List

SEARCH_URL = "https://www.perplexity.ai/api/search"


def fetch(theme: str) -> List[str]:
    """Return the top 10 links for the given theme."""
    headers = None
    token = os.getenv("PERPLEXITY_KEY")
    if token:
        headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(
        SEARCH_URL,
        params={"q": f"{theme} AI law"},
        headers=headers,
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()
    links: List[str] = []
    for item in data.get("web_results", [])[:10]:
        url = item.get("url") or item.get("sourceUrl")
        if url:
            links.append(url)
    return links
