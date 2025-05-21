from src.renderer import compose_issue


def test_compose_issue() -> None:
    links = ["http://example.com"]
    clause = "Example clause"
    issue = compose_issue(links, clause)
    assert "Counsel Codex" in issue
    assert "Example clause" in issue
