# app.py

import streamlit as st
import subprocess

st.set_page_config(page_title="Voice Assistant")
st.title("🎙️ Voice Assistant")

st.markdown("Click the button below to start voice assistant.")
st.markdown("Make sure your microphone is connected and working.")

if st.button("🟢 Start Voice Assistant"):
    st.success("Launching voice.py ...")
    subprocess.Popen(["python", "voice.py"])
