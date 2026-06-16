import whisper

def transcribe_video(video_path):

    model = whisper.load_model("base")

    result = model.transcribe(
        video_path,
        word_timestamps=True
    )

    return result