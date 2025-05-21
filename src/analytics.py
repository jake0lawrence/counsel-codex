"""Segment analytics wrapper."""

from __future__ import annotations

import os

try:
    import analytics as segment  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    segment = None


WRITE_KEY = os.getenv("SEGMENT_WRITE_KEY", "")

if segment and WRITE_KEY:
    segment.write_key = WRITE_KEY  # type: ignore[attr-defined]


def track_send(campaign_id: str) -> None:
    """Emit a `CounselCodexSent` event to Segment."""

    if not segment or not WRITE_KEY:
        return
    segment.track(  # type: ignore[attr-defined]
        "newsletter", "CounselCodexSent", {"campaign_id": campaign_id}
    )
