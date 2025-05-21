"""Generate contract clause suggestions using OpenAI."""

from __future__ import annotations

from typing import List

import openai  # type: ignore

SYSTEM_PROMPT = "You are an elite legal prompt-engineer specializing in concise, actionable contract language."


def make_clauses(resources: List[str]) -> List[str]:
    """Return a list of clause suggestions based on provided resources."""
    user_content = "\n".join(resources)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Generate five bullet clauses using these resources:\n{user_content}"},
    ]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    text = response["choices"][0]["message"]["content"].strip()
    clauses = [line.lstrip("- ").strip() for line in text.splitlines() if line.strip()]
    return clauses[:5]
