````markdown
# 🤖 Counsel Codex – Contributor / Agent Guide

This repository powers **Counsel Codex**, an AI-generated newsletter for legal-ops professionals.  
GPT Codex (or any human contributor) should follow the conventions below to keep code, docs, and CI healthy.

---

## 1 Project Layout

| Path / File | Purpose |
|-------------|---------|
| `src/` | Python application code |
| `src/main.py` | Orchestrates weekly issue generation |
| `src/airtable_client.py` | CRUD wrapper for Airtable resources |
| `src/perplexity_scraper.py` | Fetches AI-law links |
| `src/gpt_clauses.py` | Generates clause prompts via OpenAI |
| `src/renderer.py` | Renders Markdown issue (hook → 5 modules → CTA) |
| `tests/` | Pytest suites & fixtures |
| `.github/workflows/` | CI + newsletter cron |

> **Rule:** modify only inside `src/` or `tests/` unless a task explicitly says otherwise.

---

## 2 How to Run Locally

```bash
# ① Install runtime + dev deps
python -m pip install -r requirements.txt

# ② Export your OpenAI key (others optional for dry runs)
export OPENAI_API_KEY=sk-…

# ③ Generate a sample issue
python -m src.main --theme "AI Contract Drafting"
````

*If `BEEHIIV_TOKEN` is missing, the script prints Markdown to stdout instead of publishing.*

---

## 3 CI / Linters

GitHub Actions runs on every PR & merge to **main**:

1. `pip install -r requirements.txt`
2. `ruff .`  (lint)
3. `pyright` (type-check)
4. `pytest -q` (unit tests)

A failure in any step blocks merge. Fix or mark tests `xfail` with justification.

---

## 4 Coding Standards

* **Style** – PEP 8 with `ruff --fix .`
* **Types** – Add type hints; prefer `pydantic` models for strict data.
* **Functions** ≤ 40 lines when reasonable; favor small helpers & docstrings.
* **Secrets** never hard-coded—use `os.getenv()`.
* **Logging** via `structlog` or stdlib `logging`; avoid bare prints in lib code.

---

## 5 Typical Agent Tasks

| Scenario               | Example Codex Prompt                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Add new module**     | “Create `src/jurisdiction_summary.py` and integrate it into `renderer.compose_issue` as a 6th section after Tools.” |
| **Bug fix**            | “`pytest tests/test_renderer.py::test_cta` fails—patch renderer to include HTTPS link.”                             |
| **Dependency upgrade** | “Bump `openai` to ^1.13, update code & lockfile.”                                                                   |
| **Documentation**      | “Append CLI usage examples to README.md.”                                                                           |

---

## 6 Testing Notes

* Use **pytest-vcr** to record external HTTP calls (Perplexity, Airtable).
* Mock OpenAI completions with `pytest-mock`; **do not** burn tokens in CI.
* Every new feature needs at least one test; aim for > 90 % coverage on core logic.

---

## 7 PR Template

```
[Counsel-Codex] <concise title>

### What & Why
• Explain the change in one or two sentences.  
• Link any related issues or discussion.

### Checklist
- [ ] Unit tests pass
- [ ] ruff / pyright clean
- [ ] Docs updated (if applicable)
```

---

## 8 Release & Deployment Flow

1. Merge to **main** → cron workflow triggers every Friday (13:00 UTC).
2. Workflow assembles the issue, publishes to Beehiiv, and tracks a `CounselCodexSent` event in Segment.
3. Hot-fixes can be merged mid-week; they’ll ship in the next scheduled issue unless the workflow is re-run manually.

---

*Happy hacking—remember the guiding belief: **assume systems can be hacked, but do it ethically.***