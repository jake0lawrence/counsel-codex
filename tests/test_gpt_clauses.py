import sys
import types


def test_make_clauses(monkeypatch) -> None:
    sys.modules['openai'] = types.SimpleNamespace(ChatCompletion=types.SimpleNamespace(create=lambda *a, **k: {
        "choices": [{"message": {"content": "- a\n- b\n- c\n- d\n- e\n- f"}}]
    }))
    from src import gpt_clauses


    clauses = gpt_clauses.make_clauses(["x"])
    assert clauses[:2] == ["a", "b"]
    assert len(clauses) == 5
