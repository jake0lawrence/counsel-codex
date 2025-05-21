import sys
import types


def test_upsert_and_get(monkeypatch) -> None:
    sys.modules['requests'] = types.SimpleNamespace(post=lambda *a, **k: None, get=lambda *a, **k: None)
    from src.airtable_client import AirtableClient


    posts = []
    gets = []

    class Response:
        def __init__(self, json_data):
            self._json = json_data

        def json(self):
            return self._json

        def raise_for_status(self):
            pass

    def fake_post(url, json, headers, timeout):
        posts.append((url, json))
        return Response({})

    def fake_get(url, params, headers, timeout):
        gets.append((url, params))
        return Response({"records": [{"url": "http://example.com"}]})

    monkeypatch.setattr("requests.post", fake_post)
    monkeypatch.setattr("requests.get", fake_get)

    client = AirtableClient(base_url="http://api")
    client.upsert_resource({"url": "x"})
    links = client.get_weekly_resources("theme")

    assert posts
    assert links == ["http://example.com"]
