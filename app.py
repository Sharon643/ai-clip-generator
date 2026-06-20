import os
import streamlit as st
from src.transcription import transcribe_video
from src.clip_detector import find_interesting_segments
from src.video_cutter import cut_clip , get_clip_segments
from src.caption_generator import create_srt , add_captions
from src.chunker import create_chunks
from src.gemini_ranking import rank_chunk
from src.hook_generator import generate_hook


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
    # st.subheader("Segments")

    # for segment in transcript["segments"][:10]:
    #     st.write(
    #         f"{segment['start']:.2f} - "
    #         f"{segment['end']:.2f}"
    #     )
    #     st.write(segment["text"])

    chunks = create_chunks(transcript["segments"])
    # st.subheader("Chunks")

    # for chunk in chunks[:3]:

    #     st.write(
    #         f"{chunk['start']:.1f}s "
    #         f"→ "
    #         f"{chunk['end']:.1f}s"
    #     )

    #     st.write(chunk["text"])
    #     st.write(f"Total chunks: {len(chunks)}")

    #     st.divider()

    # clips = find_interesting_segments(transcript["segments"])
    ranked_chunks = []

    for chunk in chunks[:5]:

        result = rank_chunk(
            chunk["text"]
        )

        chunk["score"] = result["score"]
        chunk["reason"] = result["reason"]

        ranked_chunks.append(chunk)

    ranked_chunks.sort(key=lambda x: x["score"],reverse=True)
    for chunk in ranked_chunks[:5]:
        st.write(
            chunk["score"],
            chunk["start"],
            chunk["end"]
        )

    st.subheader("Gemini Test")

    # st.write(result)

    # for chunk in ranked_chunks:
    #     st.write(chunk)

    top_chunks = ranked_chunks[:3]

    

    st.subheader("Potential Clips")

    # for clip in clips[:10]:

    #     st.write(f"Matched keyword: {clip['keyword']}")

    #     st.write(
    #         f"{clip['start']:.2f} - "
    #         f"{clip['end']:.2f}"
    #     )

    #     st.write(clip["text"])

    if not ranked_chunks:
        st.warning("No clips found")
        st.stop()

    for i, chunk in enumerate(top_chunks):

        output_path = f"outputs/clip_{i}.mp4"


        cut_clip(
            path,
            chunk["start"],
            chunk["end"],
            output_path
        )
        hook = generate_hook(
            chunk["text"]
        )



        clip_segments = get_clip_segments(transcript["segments"],chunk["start"],chunk["end"])
        srt_path = f"outputs/clip_{i}.srt"

        create_srt(clip_segments,chunk["start"],srt_path)
        captioned_path = (f"outputs/captioned_{i}.mp4")

        add_captions(output_path,srt_path,captioned_path)


        st.subheader(f"Clip {i+1}")
        st.write(f"Hook: {hook}")

        st.write(
            f"{chunk['start']:.1f}s → {chunk['end']:.1f}s"
        )
        st.metric("Score",chunk["score"])

        st.write(chunk["text"])
        st.video(captioned_path)


