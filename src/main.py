"""Main entry for Counsel Codex newsletter automation."""

from __future__ import annotations

import argparse

from . import analytics, beehiiv, gpt_clauses, perplexity_scraper, renderer
from .airtable_client import airtable_client


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Counsel Codex newsletter tool")
    parser.add_argument(
        "--theme",
        type=str,
        default="AI and the Law",
        help="Optional theme for the weekly issue.",
    )
    return parser.parse_args()


def run_issue(theme: str) -> None:
    """Generate and publish a single newsletter issue."""
    links = perplexity_scraper.fetch(theme)
    for link in links:
        airtable_client.upsert_resource({"url": link, "theme": theme})

    resources = airtable_client.get_weekly_resources(theme)
    clauses = gpt_clauses.make_clauses(resources)
    markdown = renderer.compose_issue(theme, clauses, resources)

    cid = beehiiv.create_campaign(markdown, subject=f"{theme} – Counsel Codex")
    analytics.track_send(cid)


def main() -> None:
    """Entry point for generating a newsletter draft."""
    args = parse_args()
    run_issue(args.theme)


if __name__ == "__main__":
    main()
