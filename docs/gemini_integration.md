# Gemini Integration – Mama‑AI

This document explains how **Mama‑AI** is designed to plug into Google’s **Gemini** family of multimodal models
for the Gemini‑3 Kaggle hackathon.

## 1. Current Architecture (No‑Gemini Baseline)

Today the repo provides:

- A lightweight FastAPI backend that exposes image upload + metadata endpoints.
- Simple preprocessing utilities to:
  - Normalize and resize photos from a phone gallery.
  - Extract basic EXIF / contextual hints (timestamp, device, optional user tags).
- A small rules/heuristics layer that can return placeholder suggestions so the app is usable even without an API key.
- Streamlit / simple web front‑end (`streamlit_app.py`) that lets a caregiver upload a photo and view responses.

This “baseline” mode makes the project easy to run locally without any external API access.

## 2. Where Gemini Fits in the Loop

When a valid Gemini API key is configured (via environment variable or config file), the flow becomes:

1. User uploads a **daily photo** (e.g., meal, medication, wound, mood selfie) plus optional notes.
2. Backend stores the image temporarily and runs light preprocessing.
3. Backend builds a **multimodal prompt** for Gemini, including:
   - The uploaded image
   - Short text context (age group, known conditions, current goal like “track wound healing”)
   - A conversation history snippet (recent check‑ins and suggestions)
4. Gemini returns:
   - A brief, caregiver‑friendly summary in natural language
   - 2–4 small actionable suggestions
   - Optional flags (e.g., “watch closely”, “non‑urgent”, “consider consulting a professional if X persists”)
5. Backend structures this into a JSON response which the UI renders as a “Daily Health Card”.

The app is intentionally **guidance‑oriented**, not diagnostic. All prompts emphasize that this is **not medical advice**.

## 3. Prompting Strategy (High Level)

For each request, Mama‑AI uses a prompt template along the lines of:

- System: You are a gentle, cautious assistant helping caregivers reflect on daily photos. You never provide a diagnosis.
- User: Provides the image + short note.
- Additional context: Safe‑use policy, disclaimers, and user goals.

The model is asked to produce:

- A short “what I see” paragraph.
- A few “today you could…” suggestions.
- A safety reminder where appropriate.

## 4. Configuration

A typical config for Gemini integration might look like:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.0-flash
GEMINI_MAX_TOKENS=512
GEMINI_TEMPERATURE=0.4
```

The backend would read these values from environment variables or a `.env` file and only enable Gemini calls when
a key is present.

## 5. Fallback Behaviour

If the Gemini key is missing or invalid:

- The app falls back to a deterministic, offline‑only mode with generic tips.
- The UI clearly labels responses as **“Offline demo mode (no AI)”**.
- This ensures judges (or future users) can still run the demo without provisioning keys.

## 6. Ideas for Future Extensions

Post‑hackathon, Gemini could power:

- **Timeline views**: Generate weekly summaries (“This week your meals looked more balanced than last week.”).
- **Goal‑oriented coaching**: Prompts that track specific goals (hydration, movement, sleep hygiene, etc.).
- **Multimodal comparisons**: Side‑by‑side image reasoning (e.g., wound day 1 vs day 5) with cautious language.

This repository focuses on getting the **data flow, safety framing, and basic UX** ready so Gemini can be attached
with minimal plumbing.