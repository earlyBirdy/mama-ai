"""Model loading and prediction helpers for mama-ai.

Uses a small Hugging Face sentiment model as a concrete example:
- distilbert-base-uncased-finetuned-sst-2-english
"""

from functools import lru_cache
from transformers import pipeline


@lru_cache(maxsize=1)
def _get_pipeline():
    """Lazy-load a sentiment-analysis pipeline.

    Caches the instance so the model is only loaded once per process.
    """
    return pipeline(
        task="sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
    )


def predict_text(text: str) -> dict:
    """Run sentiment prediction on a single text string.

    Returns a simple dict: {"label": str, "score": float}
    """
    pipe = _get_pipeline()
    result = pipe(text)[0]
    return {
        "label": result.get("label", "UNKNOWN"),
        "score": float(result.get("score", 0.0)),
    }
