"""Streamlit demo UI for mama-ai with selectable backends and a MAMA.AI prototype tab."""
import os

import requests
import streamlit as st

from src.model import predict_text, get_backend_status

API_BASE = os.getenv("MAMAAI_API_BASE", "http://localhost:8000")

st.set_page_config(page_title="MAMA.AI – Prototype Demo", layout="centered")

st.title("MAMA.AI – Prototype Demo v1.2.x")
st.write("Hackathon-ready UI with a gentle MAMA.AI flow plus a basic sentiment demo.")

# --- Backend health panel ---
st.subheader("Backend Health")
status = get_backend_status()
cols = st.columns(3)
for col, name in zip(cols, ["hf", "gemini", "heuristic"]):
    s = status.get(name, {})
    available = s.get("available", False)
    detail = s.get("detail", "Unknown status.")
    with col:
        st.markdown(f"**{name.upper()}**")
        if available:
            st.success("available", icon="✅")
        else:
            st.warning("unavailable", icon="⚠️")
        st.caption(detail)

st.divider()

tab_mama, tab_sentiment, tab_bench = st.tabs(
    ["💜 MAMA.AI Demo", "🧪 Sentiment Demo", "📊 Quick Benchmark"]
)

# --- MAMA.AI tab ---
with tab_mama:
    st.subheader("Daily Health Assistant (Prototype)")
    st.markdown(
        "Describe your day in three quick steps. "
        "This is a simulated flow – no images required for the hackathon demo."
    )

    default_meal = "Fried rice with egg and pork, plus a small cola."
    default_feeling = "I felt tired today and wanted something sweet."
    default_activity = "10–30 min"

    meal_description = st.text_area("🍽️ What did you eat?", default_meal)
    feeling = st.text_area("💬 How are you feeling?", default_feeling)
    activity_level = st.selectbox(
        "🏃 Movement today?",
        ["0–10 min", "10–30 min", "30–60 min", "60+ min"],
        index=["0–10 min", "10–30 min", "30–60 min", "60+ min"].index(default_activity),
    )

    if st.button("Run MAMA.AI 💜"):
        try:
            resp = requests.post(
                f"{API_BASE}/mama_ai_demo",
                json={
                    "meal_description": meal_description,
                    "feeling": feeling,
                    "activity_level": activity_level,
                },
                timeout=15,
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            st.error(f"Failed to contact backend: {e}")
        else:
            st.success("MAMA.AI responded:")

            summary = data.get("summary", {})
            if "headline" in summary:
                st.markdown(f"### {summary['headline']}")
            if "note" in summary:
                st.caption(summary["note"])

            meal = data.get("meal_analysis", {})
            emo = data.get("emotion_analysis", {})
            grocery = data.get("grocery_list", {})
            tone = data.get("tone_evaluation", {})

            st.markdown("#### 💜 Today’s Reflection")
            if meal.get("supportive_message"):
                st.write(meal["supportive_message"])
            if emo.get("validation_message"):
                st.write(emo["validation_message"])

            st.markdown("#### 🍲 Meal Insight")
            st.json(meal)

            st.markdown("#### 🛒 Grocery Helper")
            st.json(grocery)

            st.markdown("#### 🎚 Tone Evaluation")
            st.json(tone)

            with st.expander("Raw JSON (for judges / devs)"):
                st.json(data)

# --- Sentiment demo tab ---
backend_options = ["hf", "gemini", "heuristic"]
default_backend = "hf"

with tab_sentiment:
    st.subheader("Single Prediction")

    selected_backend = st.selectbox(
        "Select backend", backend_options, index=backend_options.index(default_backend)
    )
    text = st.text_area("Enter some text", "I really like this hackathon!")

    if st.button("Predict sentiment"):
        try:
            r = predict_text(text, backend=selected_backend)
            st.write(f"**Backend:** {r['backend']}")
            st.write(f"**Label:** {r['label']}")
            st.write(f"**Score:** {r['score']:.4f}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

# --- Benchmark tab ---
with tab_bench:
    st.subheader("Quick Benchmark (all backends)")

    samples = [
        "I absolutely love this product.",
        "This is the worst experience I've had.",
        "It's okay, nothing special.",
    ]

    if st.button("Run benchmark for all backends"):
        rows = []
        for s in samples:
            for backend in backend_options:
                try:
                    r = predict_text(s, backend=backend)
                    rows.append(
                        {
                            "text": s,
                            "backend": r["backend"],
                            "label": r["label"],
                            "score": r["score"],
                        }
                    )
                except Exception as e:
                    rows.append(
                        {
                            "text": s,
                            "backend": backend,
                            "label": f"ERROR: {e}",
                            "score": 0.0,
                        }
                    )
        st.dataframe(rows)
