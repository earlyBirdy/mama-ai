"""Streamlit demo UI for mama-ai with selectable backends and health panel."""
import os

import streamlit as st

from src.model import predict_text, get_backend_status


st.set_page_config(page_title="mama-ai Demo", layout="centered")

st.title("mama-ai – Prototype Demo v1.2.1")
st.write("Hackathon-ready UI with pluggable model backends (HF, Gemini, heuristic) and live health view.")


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


# --- Gemini key input for this session ---
st.subheader("Gemini Configuration (this session)")
current_key_set = bool(os.getenv("GEMINI_API_KEY"))
st.write(f"Current session key present: **{current_key_set}**")


with st.expander("Set or override GEMINI_API_KEY for this session"):
    gemini_key = st.text_input(
        "Gemini API key",
        type="password",
        value="" if not current_key_set else ""
    )
    if st.button("Apply Gemini key for this session"):
        if gemini_key.strip():
            os.environ["GEMINI_API_KEY"] = gemini_key.strip()
            st.success("GEMINI_API_KEY set for this session.")
        else:
            if "GEMINI_API_KEY" in os.environ:
                del os.environ["GEMINI_API_KEY"]
            st.info("Cleared GEMINI_API_KEY for this session.")


backend_options = ["hf", "gemini", "heuristic"]
default_backend = "hf"

st.subheader("Model Backend Selection")
selected_backend = st.selectbox(
    "Select backend", backend_options, index=backend_options.index(default_backend)
)

tab_single, tab_bench = st.tabs(["Single Prediction", "Quick Benchmark"])

with tab_single:
    text = st.text_area("Enter some text", "I really like this hackathon!")
    if st.button("Run demo", type="primary"):
        if not text.strip():
            st.warning("Please enter some text first.")
        else:
            with st.spinner(f"Running model via `{selected_backend}` backend..."):
                result = predict_text(text, backend=selected_backend)
            st.success(
                f"Backend: **{result['backend']}**  \n"
                f"Prediction: **{result['label']}** (confidence {result['score']:.3f})"
            )

with tab_bench:
    st.write("Run a quick comparison over a few sample sentences.")
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
                    rows.append({
                        "text": s,
                        "backend": r["backend"],
                        "label": r["label"],
                        "score": r["score"],
                    })
                except Exception as e:
                    rows.append({
                        "text": s,
                        "backend": backend,
                        "label": f"ERROR: {e}",
                        "score": 0.0,
                    })
        st.dataframe(rows)
