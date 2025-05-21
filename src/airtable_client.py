"""Airtable client wrapper."""

from __future__ import annotations

import os
from typing import List

import requests  # type: ignore
from pydantic import BaseModel


class Resource(BaseModel):
    url: str
    theme: str | None = None


class AirtableClient:
    """Minimal Airtable REST API wrapper."""

    def __init__(self, base_url: str | None = None, api_key: str | None = None) -> None:
        self.base_url = base_url or os.getenv("AIRTABLE_BASE_URL", "")
        self.api_key = api_key or os.getenv("AIRTABLE_API_KEY", "")

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

    def upsert_resource(self, resource: dict) -> None:
        """Create or update a resource entry."""
        url = f"{self.base_url}/resources"
        resp = requests.post(url, json=resource, headers=self._headers(), timeout=10)
        resp.raise_for_status()

    def get_weekly_resources(self, theme: str) -> List[str]:
        """Return resource URLs filtered by theme."""
        url = f"{self.base_url}/resources"
        resp = requests.get(url, params={"theme": theme, "view": "weekly"}, headers=self._headers(), timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return [item["url"] for item in data.get("records", [])]


# Default singleton used by the app
airtable_client = AirtableClient()
