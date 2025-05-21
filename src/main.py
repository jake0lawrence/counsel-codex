"""Main entry for Counsel Codex newsletter automation."""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Counsel Codex newsletter tool")
    parser.add_argument(
        "--theme",
        type=str,
        default="",
        help="Optional theme for the weekly issue.",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point for generating a newsletter draft."""
    args = parse_args()
    # Placeholder for newsletter generation logic
    print("Generating Counsel Codex newsletter (stub)")
    if args.theme:
        print(f"Theme: {args.theme}")


if __name__ == "__main__":
    main()
