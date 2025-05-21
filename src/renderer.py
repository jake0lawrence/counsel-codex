"""Render a Markdown issue from collected content (stub)."""

from __future__ import annotations


def compose_issue(links: list[str], clause: str) -> str:
    """Compose a full markdown issue."""
    # TODO: implement templating logic
    issue_lines = ["# Counsel Codex", "", *links, "", clause]
    return "\n".join(issue_lines)
