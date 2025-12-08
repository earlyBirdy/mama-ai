"""Basic sanity tests for mama-ai model wrapper.

These tests are intentionally light and do *not* require NumPy.
If the HF stack is available, it will be used; otherwise the heuristic
fallback still returns a valid label/score pair.
"""

import pytest

from src.model import predict_text


@pytest.mark.parametrize("text", [
    "I love this product!",          # clearly positive
    "This is terrible.",            # clearly negative
    "It's okay, nothing special.",  # neutral-ish
])
def test_predict_text_runs(text):
    result = predict_text(text)
    assert "label" in result
    assert "score" in result
    assert isinstance(result["label"], str)
    assert isinstance(result["score"], float)
    assert 0.0 <= result["score"] <= 1.0
