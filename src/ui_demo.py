"""Streamlit demo UI for mama-ai."""
import streamlit as st

st.set_page_config(page_title="mama-ai Demo", layout="centered")

st.title("mama-ai – Prototype Demo v1.1")
st.write("Quick hackathon-ready UI to play with text input.")

text = st.text_area("Enter some text", "Hello, mama-ai!")
if st.button("Run demo"):
    # TODO: replace with real model call
    st.success("Demo prediction: **demo-label** (confidence 0.42)")
