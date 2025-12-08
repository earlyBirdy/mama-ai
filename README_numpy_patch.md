# mama-ai NumPy patch

The Hugging Face / PyTorch stack used by `src.model` requires NumPy.

This patch:
- Adds `numpy` to `requirements.txt`
- Updates `tests/test_model.py` to `importorskip("numpy")` so tests fail
  less cryptically if NumPy is missing.

## How to apply

1. Unzip into your existing `mama-ai` repository root.
   - Overwrite `requirements.txt`
   - Overwrite `tests/test_model.py`

2. Install / update dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Re-run tests:

   ```bash
   pytest
   ```

You should no longer see `RuntimeError: Numpy is not available`. If you do,
check that NumPy installed correctly in your active virtualenv.
