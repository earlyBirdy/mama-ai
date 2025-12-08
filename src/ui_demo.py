"""Streamlit demo UI for mama-ai with selectable backends."""
import streamlit as st

from src.model import predict_text


st.set_page_config(page_title="mama-ai Demo", layout="centered")

st.title("mama-ai – Prototype Demo v1.2")
st.write("Hackathon-ready UI with pluggable model backends (HF, Gemini, heuristic).")


backend_options = ["hf", "gemini", "heuristic"]
default_backend = "hf"

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
                except Exception as e:  # e.g., Gemini not configured
                    rows.append({
                        "text": s,
                        "backend": backend,
                        "label": f"ERROR: {e}",
                        "score": 0.0,
                    })
        st.dataframe(rows)
