import subprocess

def cut_clip(input_video, start, end, output_file):

    command = [
        "ffmpeg",
        "-y",
        "-i", input_video,
        "-ss", str(start),
        "-to", str(end),
        "-c:v", "libx264",
        "-c:a", "aac",
        output_file
    ]

    subprocess.run(command)

def get_clip_segments(all_segments,start_time,end_time):

    return [
        s for s in all_segments
        if s["start"] >= start_time
        and s["end"] <= end_time
    ]