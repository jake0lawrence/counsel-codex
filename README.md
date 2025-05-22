# Counsel Codex

**Counsel Codex** is an automated, AI-powered newsletter for legal-ops and in-house counsel.  
It scrapes fresh AI-law resources, generates ready-to-use contract clauses with GPT-4, and publishes weekly issues via Beehiiv—all from this repo.

| | |
|---|---|
| **Stack** | Python 3.11 • OpenAI • Airtable • Perplexity • Beehiiv |
| **Automation** | GitHub Actions (cron) |
| **Dev quick-start** | `pip install -r requirements.txt`<br>`export OPENAI_API_KEY=...`<br>`export AIRTABLE_API_KEY=...`<br>`python -m src.main --theme "AI Contract Drafting"` |

### Running Tests

Install development dependencies and run the test suite:

```bash
pip install -r requirements-dev.txt  # or `make install`
pytest -q
```

For contributor instructions and repo conventions, see **[AGENTS.md](./AGENTS.md)**.
## License

This project is licensed under the [MIT License](./LICENSE).
