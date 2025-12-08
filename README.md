# 🤖 mama-ai  
Prototype AI Starter — CLI + API + Web UI (HF + Gemini-ready)

> A minimal, hackathon-ready AI boilerplate that lets you plug in models and demo them in minutes — not hours.  
> Now with a pluggable backend architecture (Hugging Face, Gemini, heuristic).

## 🚀 TL;DR — Run the demo

```bash
pip install -r requirements.txt
./run_ui.sh   # Streamlit web UI
./run_api.sh  # FastAPI API backend
```

On Windows:

```bat
run_ui.bat
run_api.bat
```

## 🧠 What this project does

`mama-ai` gives you a ready-to-run sentiment analysis demo using:

- Hugging Face DistilBERT sentiment model (when available)
- Optional Google Gemini backend (stubbed, ready for API key + client)
- A safe heuristic fallback that never crashes if dependencies fail

It includes CLI, FastAPI, Streamlit UI, tests, a model abstraction layer,
and hackathon-ready pitch scripts.
