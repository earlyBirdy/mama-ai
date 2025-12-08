"""Streamlit demo UI for mama-ai with real HF model."""
import streamlit as st

from src.model import predict_text


st.set_page_config(page_title="mama-ai Demo", layout="centered")

st.title("mama-ai – Prototype Demo v1.1")
st.write("Quick hackathon-ready UI backed by a real HF sentiment model.")

text = st.text_area("Enter some text", "I really like this hackathon!")

if st.button("Run demo"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Running model..."):
            result = predict_text(text)
        label = result["label"]
        score = result["score"]
        st.success(f"Prediction: **{label}** (confidence {score:.3f})")
