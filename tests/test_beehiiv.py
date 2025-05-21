import sys
from types import ModuleType


def test_create_campaign_dry_run(monkeypatch) -> None:
    fake_requests = ModuleType("requests")
    setattr(fake_requests, "post", lambda *a, **k: None)
    sys.modules["requests"] = fake_requests
    from src import beehiiv

    logs: list[str] = []

    class FakeLogger:
        def info(self, msg, *args, **kwargs):
            logs.append(msg % args if args else msg)

    monkeypatch.setattr(beehiiv, "logger", FakeLogger())

    monkeypatch.delenv("BEEHIIV_TOKEN", raising=False)
    cid = beehiiv.create_campaign("markdown", "Subject")
    assert cid == "dry-run"
    assert logs and "markdown" in logs[0]
