# mama-ai – Hackathon Submission

## One-line description

A minimal, pluggable AI starter that turns any model into a CLI, API, and web demo in minutes — with Hugging Face, Gemini, and heuristic backends.

## What it does

- Provides a clean, production-lean skeleton for AI projects.
- Includes a CLI, FastAPI service, and Streamlit UI.
- Uses a sentiment model by default (HF DistilBERT when available).
- Falls back to a rule-based heuristic if heavy deps or network fail.
- Optionally integrates with Google Gemini via `GEMINI_API_KEY`.

## Gemini-specific section

- The backend architecture supports a "gemini" mode, which routes text to
  a Gemini model (e.g., `gemini-2.0-flash`) via the official client.
- Configuration uses environment variables:
  - `GEMINI_API_KEY` is read from `.env` or the OS environment.
- In the UI, you can set or override the Gemini key for the **current
  session** only (no secrets are written to disk).
- If Gemini is not configured, the app:
  - Flags this in the "Backend Health" panel.
  - Falls back to the heuristic backend instead of crashing.
- This makes the demo safe to run on any judge's laptop or cloud workspace,
  regardless of whether Gemini is available.

## How to run it (judge-friendly)

```bash
pip install -r requirements.txt
cp .env.example .env        # optional: configure GEMINI_API_KEY
./run_ui.sh                 # start the Streamlit UI
./run_api.sh                # start the FastAPI backend
```

- Open `http://localhost:8501` for the UI.
- Select a backend: `hf`, `gemini`, or `heuristic`.
- Type a sentence and click **Run demo**.
- Use the "Backend Health" panel to see which backends are ready.

## Future work

- Add task-specific prompts and labels for Gemini (classification, scoring).
- Add logging and metrics for backend selection and performance.
- Provide Docker / k8s manifests for easy deployment.
