import os
import streamlit as st
from src.transcription import transcribe_video

uploaded_file = st.file_uploader(
    "Upload video",
    type=["mp4"]
)

if uploaded_file:

    path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(path,"wb") as f:
        f.write(uploaded_file.read())

    transcript = transcribe_video(path)

    st.subheader("Transcript")
    st.write(transcript)