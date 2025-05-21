import sys
from types import ModuleType


def test_fetch(monkeypatch) -> None:
    fake_requests = ModuleType("requests")
    setattr(fake_requests, "get", lambda *a, **k: None)
    sys.modules["requests"] = fake_requests
    from src import perplexity_scraper


    def fake_get(url, params, headers=None, timeout=10):
        class Response:
            def raise_for_status(self):
                pass

            def json(self):
                return {"web_results": [{"url": f"http://{i}.com"} for i in range(12)]}

        return Response()

    monkeypatch.setattr(perplexity_scraper.requests, "get", fake_get)
    links = perplexity_scraper.fetch("test")
    assert len(links) == 10
    assert links[0] == "http://0.com"


def test_fetch_with_header(monkeypatch) -> None:
    fake_requests = ModuleType("requests")
    setattr(fake_requests, "get", lambda *a, **k: None)
    sys.modules["requests"] = fake_requests
    from src import perplexity_scraper

    captured_headers = {}

    def fake_get(url, params, headers=None, timeout=10):
        captured_headers.update(headers or {})

        class Response:
            def raise_for_status(self):
                pass

            def json(self):
                return {"web_results": []}

        return Response()

    monkeypatch.setattr(perplexity_scraper.requests, "get", fake_get)
    monkeypatch.setenv("PERPLEXITY_KEY", "tok")
    perplexity_scraper.fetch("test")
    assert captured_headers == {"Authorization": "Bearer tok"}
