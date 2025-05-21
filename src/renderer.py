"""Render Markdown issues for Counsel Codex."""

from __future__ import annotations

from typing import List


def compose_issue(theme: str, clauses: List[str], resources: List[str]) -> str:
    """Compose a markdown newsletter using the standard format."""
    lines = [f"# Counsel Codex – {theme}", ""]
    lines.append("## Hook")
    if clauses:
        lines.append(clauses[0])
    lines.append("")
    lines.append("## Value")
    for clause in clauses[:5]:
        lines.append(f"- {clause}")
    lines.append("")
    lines.append("## Resources")
    for url in resources:
        lines.append(f"- {url}")
    lines.append("")
    lines.append(
        "**Ready to streamline your contracts? [Subscribe to Counsel Codex](https://counselcodex.example.com)**"
    )
    return "\n".join(lines)
