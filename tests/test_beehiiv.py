import sys
from types import ModuleType


def test_create_campaign_dry_run(capfd, monkeypatch) -> None:
    fake_requests = ModuleType("requests")
    setattr(fake_requests, "post", lambda *a, **k: None)
    sys.modules["requests"] = fake_requests
    from src import beehiiv

    monkeypatch.delenv("BEEHIIV_TOKEN", raising=False)
    cid = beehiiv.create_campaign("markdown", "Subject")
    assert cid == "dry-run"
    out, _ = capfd.readouterr()
    assert "markdown" in out
