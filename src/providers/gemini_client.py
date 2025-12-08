"""Gemini provider stub for mama-ai."""

from __future__ import annotations

import os
from typing import Dict

try:
    from google import genai  # type: ignore
except Exception:
    genai = None  # type: ignore


def _get_client():
    if genai is None:
        raise RuntimeError(
            "Gemini client library not installed (google-genai). Install it or disable 'gemini' backend."
        )
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set in environment.")
    return genai.Client(api_key=api_key)


def gemini_predict(text: str) -> Dict[str, object]:
    """Call Gemini with the given input text."""
    client = _get_client()
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=text,
    )
    out_text = getattr(response, "text", None) or "GEMINI_OUTPUT"
    return {"label": out_text, "score": 0.99}
