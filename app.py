import os
import streamlit as st
from src.transcription import transcribe_video
from src.clip_detector import find_interesting_segments
from src.video_cutter import cut_clip

st.title("AI Clip Generator")
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

    # st.subheader("Transcript")
    # st.write(transcript["text"])
    st.subheader("Segments")

    for segment in transcript["segments"][:10]:
        st.write(
            f"{segment['start']:.2f} - "
            f"{segment['end']:.2f}"
        )
        st.write(segment["text"])

    clips = find_interesting_segments(transcript["segments"])

    st.subheader("Potential Clips")

    for clip in clips[:10]:

        st.write(
            f"{clip['start']:.2f} - "
            f"{clip['end']:.2f}"
        )

        st.write(clip["text"])
    if clips:

        first_clip = clips[0]

        output_path = "outputs/clip1.mp4"

        cut_clip(
            path,
            first_clip["start"],
            first_clip["end"],
            output_path
        )

        st.success("Clip generated!")

        st.video(output_path)