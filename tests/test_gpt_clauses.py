import sys
import types
from types import ModuleType


def test_make_clauses(monkeypatch) -> None:
    fake_openai = ModuleType("openai")
    setattr(
        fake_openai,
        "ChatCompletion",
        types.SimpleNamespace(
            create=lambda *a, **k: {
                "choices": [
                    {"message": {"content": "- a\n- b\n- c\n- d\n- e\n- f"}}
                ]
            },
        ),
    )
    sys.modules["openai"] = fake_openai
    from src import gpt_clauses


    clauses = gpt_clauses.make_clauses(["x"])
    assert clauses[:2] == ["a", "b"]
    assert len(clauses) == 5
