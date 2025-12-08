## v1.2.1
- Added .env support for GEMINI_API_KEY (via python-dotenv).
- Added Streamlit UI controls to set Gemini key for the current session.
- Added backend health indicator (HF / Gemini / heuristic) in API and UI.
- Added `docs/gemini_integration.md` with detailed instructions.
- Expanded hackathon submission with a Gemini-specific section.

## v1.2.0
- Added pluggable model backend architecture (HF / Gemini / heuristic).
- Added Gemini provider stub (`src/providers/gemini_client.py`).
- Extended API to accept optional `backend` parameter.
- Extended Streamlit UI with model backend dropdown + quick benchmark tab.

## v1.1.0
- Added FastAPI demo API (`src/api.py`) with real HF sentiment model.
- Added Streamlit UI demo (`src/ui_demo.py`) backed by the same model.
- Added simple CLI entrypoint (`src/simple_cli.py`).
- Added hackathon submission assets under `hackathon/`.
- Updated docs for architecture and pitch.

## v1.0.0
- Initial PROTOTYPE release bundle.
- Repo initialized with standard structure.
