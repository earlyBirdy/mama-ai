# mama-ai – Hackathon Submission

## One-line description
A minimal, end-to-end AI starter repo with CLI, API, and UI so teams can ship demos in hours.

## What it does
- Provides a clean skeleton for AI projects.
- Includes a CLI, FastAPI service, and Streamlit UI.
- Lets you plug in any model and quickly showcase value.

## How to run it
### CLI
```bash
python -m mama_ai.src.main
```

### FastAPI
```bash
uvicorn src.api:app --reload
```

### Streamlit
```bash
streamlit run src/ui_demo.py
```

## Future work
- Real model integration (HF or custom)
- Evaluation scripts and leaderboard
- Cloud-ready deployment templates
