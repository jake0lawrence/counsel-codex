"""Beehiiv publishing utilities."""

from __future__ import annotations

import os
import logging
import requests  # type: ignore


API_URL = "https://api.beehiiv.com/v2/campaigns"

logger = logging.getLogger(__name__)


def _headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def create_campaign(markdown: str, subject: str) -> str:
    """Publish a campaign and return its ID.

    If ``BEEHIIV_TOKEN`` is not set, the Markdown is logged and a placeholder ID
    is returned instead of performing a network request.
    """
    token = os.getenv("BEEHIIV_TOKEN")
    if not token:
        logger.info("Beehiiv dry run markdown:\n%s", markdown)
        return "dry-run"

    payload = {"subject": subject, "markdown": markdown}
    resp = requests.post(API_URL, json=payload, headers=_headers(token), timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return str(data.get("id", ""))
