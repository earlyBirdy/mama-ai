# Gemini‑3 Hackathon – Draft Submission (Mama‑AI)

> **Note:** This is a draft you can paste into the Kaggle submission form and refine as needed.

---

## 1. Project Title

**Mama‑AI – Daily Health Reflection from Photos**

---

## 2. One‑liner

*A gentle, photo‑driven daily check‑in companion that helps caregivers notice small health changes over time – without ever pretending to be a doctor.*

---

## 3. What the project does

Mama‑AI lets a caregiver (or an adult looking after themselves or an elder) upload simple daily photos – meals, medication setups, skin/wound checks, mobility aids, or mood selfies – and receive:

- A short, friendly description of what the assistant notices.
- 2–4 small, practical suggestions for the day (drink more water, protect skin, organise pills, etc.).
- Gentle reminders about safety and when to consider seeking professional help.

The goal is **reflection and awareness**, not diagnosis. Over time, a timeline of “daily cards” helps the user see trends, not just isolated snapshots.

---

## 4. How it uses Gemini

In the intended full setup, Gemini acts as the **multimodal reasoning core**:

1. The backend receives an uploaded image + optional text note.
2. It constructs a prompt that combines:
   - The image (e.g., meal, wound close‑up, medication box).
   - Structured context (age group, rough goals like “improve diet” or “monitor skin irritation”).
   - Recent conversation history for continuity.
3. A Gemini vision‑capable model (e.g., `gemini-2.0-flash`) returns:
   - A brief natural‑language summary of the scene.
   - A small set of suggestions grouped into “Today”, “This week”, and “Watch out for”.
   - A clearly phrased safety reminder.

All prompts are written to **avoid medical diagnosis** and to push users towards professional care when anything looks concerning.

For the hackathon, the repo is structured so that:

- Gemini calls can be wired into a single integration layer (see `docs/gemini_integration.md`).
- If no API key is available, the app runs in “offline demo mode” with deterministic placeholder responses.

---

## 5. Why this matters

- Many caregivers are already taking photos (meals, medication, wounds) but **have no structured way** to reflect on them.
- Search engines and social media are noisy and often unsafe for health questions.
- A gentle, **reflection‑oriented** assistant can nudge people towards better habits and earlier professional consultation – without offering risky pseudo‑diagnoses.

Mama‑AI aims to be:

- **Low friction** – just take a photo and upload.
- **Emotionally safe** – careful wording, no alarming language, lots of reassurance and disclaimers.
- **Respectful of limits** – always “supporting decisions”, never “making decisions”.

---

## 6. What’s implemented in this repo

Technically, this repository includes:

- A small FastAPI backend for handling uploads and returning structured responses.
- A simple web / Streamlit front‑end for demo purposes.
- Basic tests (5 passed) that cover the core request/response pipeline.
- Stubbed Gemini integration points so you can plug in real API calls with minimal changes.
- Documentation in `docs/` describing the Gemini flow and hackathon context.

This is intentionally lightweight so judges can clone, install, and run a demo quickly.

---

## 7. How to run it locally (for judges)

```bash
git clone <your-repo-url>.git
cd mama-ai

python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

pip install -r requirements.txt

# (Optional) run tests
pytest -q

# Start the API or demo app
./run_api.sh          # or: uvicorn api.main:app --reload
# For Streamlit demo:
streamlit run streamlit_app.py
```

If you have a Gemini API key, export it before starting the app:

```bash
export GEMINI_API_KEY="your_key_here"
```

The app will then route requests through Gemini instead of the offline placeholder logic (depending on how you wire the integration).

---

## 8. Links (to fill in)

- **GitHub repo:** `<your GitHub URL>`
- **Hugging Face Space (demo):** `<your HF Space URL>`
- **Video demo (optional):** `<link if available>`

---

## 9. Future work (after the hackathon)

- Richer timelines and weekly/monthly summaries powered by Gemini.
- Goal‑based coaching (hydration, sleep hygiene, mobility, nutrition) with configurable prompts.
- Better privacy controls and on‑device preprocessing options.
- Localisation for non‑English caregivers and families.