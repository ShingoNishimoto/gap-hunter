"""
Shared Anthropic client.

Used by lib.concepts, lib.quiz, lib.grader.
Centralizing here prevents three copies of the API setup.
"""
import os
from typing import Optional

from anthropic import Anthropic

# Model strings (latest as of May 2026)
MODEL_SONNET = "claude-sonnet-4-6"
MODEL_HAIKU = "claude-haiku-4-5-20251001"

_client: Optional[Anthropic] = None


def get_client() -> Anthropic:
    """Lazy singleton. Reads ANTHROPIC_API_KEY from env."""
    global _client
    if _client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY missing. Set it in Streamlit Cloud Secrets "
                "or in your shell env for local dev."
            )
        _client = Anthropic(api_key=api_key)
    return _client


def call_claude(
    prompt: str,
    *,
    model: str = MODEL_SONNET,
    max_tokens: int = 2000,
    system: Optional[str] = None,
) -> str:
    """
    One-shot Claude call. Returns the response text.

    Use MODEL_HAIKU for cheap calls (concept extraction, batched work).
    Use MODEL_SONNET for question generation and grading.
    """
    kwargs = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        kwargs["system"] = system
    msg = get_client().messages.create(**kwargs)
    return msg.content[0].text
