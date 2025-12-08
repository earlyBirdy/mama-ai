"""Model loading and prediction helpers for mama-ai."""

from __future__ import annotations

import os
from functools import lru_cache
from typing import Dict

from src.config import get_settings

try:
    from transformers import pipeline  # type: ignore
except Exception:
    pipeline = None  # type: ignore

try:
    from src.providers.gemini_client import gemini_predict
except Exception:
    gemini_predict = None  # type: ignore


POSITIVE_WORDS = {"love", "like", "great", "awesome", "good", "fantastic", "amazing"}
NEGATIVE_WORDS = {"hate", "terrible", "bad", "awful", "horrible", "worst"}


@lru_cache(maxsize=1)
def _get_hf_pipeline():
    if pipeline is None:
        return None
    try:
        return pipeline(
            task="sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
        )
    except Exception:
        return None


def _heuristic_sentiment(text: str) -> Dict[str, object]:
    t = text.lower()
    pos_hits = sum(1 for w in POSITIVE_WORDS if w in t)
    neg_hits = sum(1 for w in NEGATIVE_WORDS if w in t)

    if pos_hits > neg_hits:
        return {"backend": "heuristic", "label": "POSITIVE", "score": 0.8}
    if neg_hits > pos_hits:
        return {"backend": "heuristic", "label": "NEGATIVE", "score": 0.8}
    return {"backend": "heuristic", "label": "NEUTRAL", "score": 0.5}


def predict_text(text: str, backend: str | None = None) -> Dict[str, object]:
    """Run sentiment prediction on a single text string."""
    settings = get_settings()
    if backend is None:
        backend = os.getenv("MAMA_AI_BACKEND", settings["backend_default"]).lower()

    if backend == "gemini" and gemini_predict is not None:
        try:
            result = gemini_predict(text)
            return {
                "backend": "gemini",
                "label": result.get("label", "UNKNOWN"),
                "score": float(result.get("score", 0.0)),
            }
        except Exception:
            return _heuristic_sentiment(text)

    if backend == "hf":
        pipe = _get_hf_pipeline()
        if pipe is not None:
            try:
                out = pipe(text)[0]
                return {
                    "backend": "hf",
                    "label": out.get("label", "UNKNOWN"),
                    "score": float(out.get("score", 0.0)),
                }
            except Exception:
                return _heuristic_sentiment(text)
        else:
            return _heuristic_sentiment(text)

    return _heuristic_sentiment(text)


def get_backend_status() -> Dict[str, Dict[str, object]]:
    """Return a lightweight health snapshot for each backend."""
    settings = get_settings()

    status: Dict[str, Dict[str, object]] = {
        "heuristic": {"available": True, "detail": "Always on (rule-based)."}
    }

    # HF status
    pipe = _get_hf_pipeline()
    if pipeline is None:
        status["hf"] = {"available": False, "detail": "transformers not installed or failed to import."}
    elif pipe is None:
        status["hf"] = {"available": False, "detail": "transformers loaded but pipeline failed to initialize."}
    else:
        status["hf"] = {"available": True, "detail": "HF pipeline initialized."}

    # Gemini status
    if gemini_predict is None:
        status["gemini"] = {"available": False, "detail": "Gemini client stub not importable or optional dependency missing."}
    else:
        if settings["gemini_api_key_present"]:
            status["gemini"] = {"available": True, "detail": "Gemini client ready (API key detected)."}
        else:
            status["gemini"] = {"available": False, "detail": "Gemini client code available but GEMINI_API_KEY missing."}

    return status
