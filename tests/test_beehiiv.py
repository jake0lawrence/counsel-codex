import sys
import types


def test_create_campaign_dry_run(capfd, monkeypatch) -> None:
    sys.modules["requests"] = types.SimpleNamespace(post=lambda *a, **k: None)
    from src import beehiiv

    monkeypatch.delenv("BEEHIIV_TOKEN", raising=False)
    cid = beehiiv.create_campaign("markdown", "Subject")
    assert cid == "dry-run"
    out, _ = capfd.readouterr()
    assert "markdown" in out
