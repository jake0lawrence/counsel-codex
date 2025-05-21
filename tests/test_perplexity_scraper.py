import sys
import types


def test_fetch(monkeypatch) -> None:
    sys.modules['requests'] = types.SimpleNamespace(get=lambda *a, **k: None)
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
