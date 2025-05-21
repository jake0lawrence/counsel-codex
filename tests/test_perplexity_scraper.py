import sys
from types import ModuleType


def test_fetch(monkeypatch) -> None:
    fake_requests = ModuleType("requests")
    setattr(fake_requests, "get", lambda *a, **k: None)
    sys.modules["requests"] = fake_requests
    from src import perplexity_scraper


    def fake_get(url, params, timeout):
        class Response:
            def raise_for_status(self):
                pass

            def json(self):
                return {"web_results": [{"url": f"http://{i}.com"} for i in range(12)]}

        return Response()

    monkeypatch.setattr("requests.get", fake_get)
    links = perplexity_scraper.fetch("test")
    assert len(links) == 10
    assert links[0] == "http://0.com"
