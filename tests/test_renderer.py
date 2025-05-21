from src.renderer import compose_issue


def test_compose_issue() -> None:
    theme = "AI Contracts"
    resources = ["http://example.com"]
    clauses = ["Clause 1", "Clause 2", "Clause 3", "Clause 4", "Clause 5"]
    issue = compose_issue(theme, clauses, resources)
    assert "Counsel Codex" in issue
    assert theme in issue
    assert "Clause 1" in issue
    assert "http://example.com" in issue
