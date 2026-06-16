import subprocess

def seconds_to_srt_time(seconds):

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)

    return (
        f"{hours:02}:{minutes:02}:"
        f"{secs:02},{millis:03}"
    )


def create_srt(segments,clip_start,output_file):

    with open(output_file, "w", encoding="utf-8") as f:

        for i, segment in enumerate(segments):

            start = (
                segment["start"]
                - clip_start
            )

            end = (
                segment["end"]
                - clip_start
            )

            f.write(f"{i+1}\n")

            f.write(
                f"{seconds_to_srt_time(start)} --> "
                f"{seconds_to_srt_time(end)}\n"
            )

            f.write(
                segment["text"].strip()
                + "\n\n"
            )

def add_captions(video_file,srt_file,output_file):

    command = [
        "ffmpeg",
        "-y",
        "-i",
        video_file,
        "-vf",
        f"subtitles={srt_file}",
        output_file
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(result.stderr)