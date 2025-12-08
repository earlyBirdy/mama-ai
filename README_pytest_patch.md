# mama-ai pytest import patch

This patch adds:

- `tests/conftest.py` to inject the project root into `sys.path` for pytest,
  so that `from src.model import predict_text` works reliably.
- A minimal `src/__init__.py` to ensure `src` is treated as a package.

## How to apply

1. Unzip this patch on top of your existing `mama-ai` repository.
   - You should end up with:
     - `tests/conftest.py`
     - `src/__init__.py` (if it wasn't already present)

2. From the repo root, run:

   ```bash
   pytest
   ```

You can also explicitly set `PYTHONPATH` if needed:

```bash
export PYTHONPATH="$PWD"   # macOS / Linux
pytest
```
