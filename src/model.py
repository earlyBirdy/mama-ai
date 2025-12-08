"""Model loading and prediction helpers for mama-ai.

Primary path:
    - Use a small Hugging Face sentiment model via `transformers.pipeline`
      (distilbert-base-uncased-finetuned-sst-2-english).

Fallback path:
    - If transformers/torch/NumPy are not available or fail at runtime,
      fall back to a simple rule-based sentiment heuristic so that demos
      and tests still run instead of crashing.
"""

from __future__ import annotations

from functools import lru_cache

try:
    from transformers import pipeline  # type: ignore
except Exception:  # transformers (or its deps) not installed/usable
    pipeline = None  # type: ignore


POSITIVE_WORDS = {"love", "like", "great", "awesome", "good", "fantastic", "amazing"}
NEGATIVE_WORDS = {"hate", "terrible", "bad", "awful", "horrible", "worst"}


@lru_cache(maxsize=1)
def _get_pipeline():
    """Lazy-load a sentiment-analysis pipeline if possible.

    Returns None if transformers/torch/NumPy are not working.
    """
    if pipeline is None:
        return None

    try:
        return pipeline(
            task="sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
        )
    except Exception:
        # Anything goes wrong (e.g., NumPy not available, CPU/GPU issues),
        # just fall back to heuristic mode.
        return None


def _heuristic_sentiment(text: str) -> dict:
    """Very simple rule-based sentiment as a safe fallback."""
    t = text.lower()
    pos_hits = sum(1 for w in POSITIVE_WORDS if w in t)
    neg_hits = sum(1 for w in NEGATIVE_WORDS if w in t)

    if pos_hits > neg_hits:
        return {"label": "POSITIVE", "score": 0.8}
    if neg_hits > pos_hits:
        return {"label": "NEGATIVE", "score": 0.8}
    return {"label": "NEUTRAL", "score": 0.5}


def predict_text(text: str) -> dict:
    """Run sentiment prediction on a single text string.

    Prefer the HF model when available; otherwise use heuristic fallback.

    Returns:
        dict: {"label": str, "score": float}
    """
    pipe = _get_pipeline()
    if pipe is not None:
        try:
            result = pipe(text)[0]
            label = result.get("label", "UNKNOWN")
            score = float(result.get("score", 0.0))
            return {"label": label, "score": score}
        except Exception:
            # If anything goes wrong at inference time, switch to heuristic.
            pass

    return _heuristic_sentiment(text)
