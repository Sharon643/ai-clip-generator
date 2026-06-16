import whisper
import torch

def transcribe_video(video_path):

    device = "cuda" if torch.cuda.is_available() else "cpu"

    model = whisper.load_model("base",device=device)

    result = model.transcribe(
        video_path,
        word_timestamps=True
    )

    return result