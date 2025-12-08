"""Configuration utilities for mama-ai."""

from __future__ import annotations

import os
from functools import lru_cache

from dotenv import load_dotenv

# Load .env once at import time
load_dotenv()


@lru_cache(maxsize=1)
def get_settings() -> dict:
    """Return a simple settings dict."""
    return {
        "backend_default": os.getenv("MAMA_AI_BACKEND", "hf"),
        "gemini_api_key_present": bool(os.getenv("GEMINI_API_KEY")),
    }
