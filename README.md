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

---

# 💜 MAMA.AI  
*A gentle AI that helps you eat better — one small step at a time.*

---

## 🍽️ What is MAMA.AI?

Most health apps push numbers, rules, or guilt.

**MAMA.AI is different.**

You simply:

1. 📸 Take a photo of your meal  
2. 💬 Share how you feel (text or voice)  
3. 🚶 Tap how much you moved today  

Then MAMA.AI responds like someone who genuinely cares:

> “Your meal looked delicious — next time maybe add a little more protein.  
> You’re doing well already.”

---

## ✨ Core Features

- 🍲 **Meal Photo Analysis** – Gemini Vision identifies the meal and estimates calories  
- 🥦 **Plate Ratio Coaching** – Easy, realistic nutrition tweaks  
- 🏃 **Simple Activity Check-in** – One tap, no smartwatch  
- 💬 **Voice Emotional Log** – Understand stress, cravings, and patterns  
- 🛍️ **Grocery Suggestion Engine** – “Let me help tomorrow feel easier”  
- 💜 **Tone Adaptive System** – AI checks its own tone (Mom / Friend / Coach %)  

---

## 🧠 AI Architecture Overview

```text
User Input
  → Gemini 3 Pro (Vision + Text)
  → Reasoning & habit layer
  → Food swap engine + grocery planner
  → Tone self-evaluation
  → Final caring response
