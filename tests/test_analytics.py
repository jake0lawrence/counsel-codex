from src import analytics


def test_track_send(monkeypatch) -> None:
    events = []

    class FakeAnalytics:
        def track(self, user_id, event, properties):
            events.append((user_id, event, properties))

    monkeypatch.setattr(analytics, "segment", FakeAnalytics())
    monkeypatch.setattr(analytics, "WRITE_KEY", "key")
    analytics.track_send("123")
    assert events == [("newsletter", "CounselCodexSent", {"campaign_id": "123"})]
