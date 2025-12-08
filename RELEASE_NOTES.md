# mama-ai v1.2.1 Release Notes

This release improves the Gemini integration experience and operational
readiness for demos and hackathons:

- Environment-based configuration using `.env` and `GEMINI_API_KEY`.
- Streamlit UI widgets to set the Gemini key for the current session.
- Backend health indicators surfaced via API and UI.
- A dedicated `docs/gemini_integration.md` to guide setup.


# mama-ai v1.1.0 Release Notes

This release makes mama-ai a hackathon-ready, *real* model demo:

- **Real model**: Uses a Hugging Face sentiment pipeline
  (`distilbert-base-uncased-finetuned-sst-2-english`).
- **API**: FastAPI service exposes `/health` and `/predict` (POST) endpoints.
- **UI**: Streamlit front-end lets judges type text and see predictions live.
- **Structure**: Clear folders for `src/`, `models/`, `data/`, `docs/`, and `hackathon/` assets.

See `hackathon/submission.md` for how to pitch and run it during events.
