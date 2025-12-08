# Gemini Integration Guide (mama-ai)

This document explains how to enable and use the Gemini backend in mama-ai.

## 1. Install optional dependencies

```bash
pip install python-dotenv
# and if you want real Gemini calls:
# pip install google-genai
```

`python-dotenv` is already in `requirements.txt`. You only need `google-genai`
if you intend to call Gemini for real.

## 2. Configure GEMINI_API_KEY

1. Copy the example env file:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and set your key:

   ```env
   GEMINI_API_KEY=your-real-key-here
   MAMA_AI_BACKEND=hf
   ```

3. mama-ai will automatically load `.env` on startup (API, UI, CLI).

You can also override the key at runtime inside the Streamlit UI using the
"Gemini key for this session" input, which updates `GEMINI_API_KEY` in
memory for the current process only.

## 3. Backends and selection

The central entrypoint is `src.model.predict_text(text, backend=None)`.

- If `backend` is `None`, it uses `MAMA_AI_BACKEND` from the environment
  (default: `hf`).
- If `backend` is `"hf"`, it tries the Hugging Face sentiment model.
- If `backend` is `"gemini"`, it tries the Gemini backend.
- If `backend` is `"heuristic"`, it uses a local rule-based heuristic.

The Streamlit UI exposes a dropdown to select the backend for each call.
The FastAPI `/predict` endpoint accepts an optional `backend` field in the
JSON body.

## 4. Backend health

`src.model.get_backend_status()` returns a dict describing the readiness of
each backend (hf, gemini, heuristic). This is surfaced via:

- API: `GET /backend_status`
- UI: a "Backend Health" panel at the top of the page

This lets you demo how the system behaves when Gemini is not configured
(e.g., missing key) without causing crashes.

## 5. Security notes

- Never commit `.env` or any real API keys to Git.
- `.env` is already in `.gitignore`.
- For hackathons, it's fine to use a single key for all your local demos,
  but consider separate keys for production / shared environments.
