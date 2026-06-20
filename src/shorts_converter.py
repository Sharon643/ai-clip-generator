import subprocess

def convert_to_vertical(
    input_video,
    output_video
):

    cmd = [
        "ffmpeg",
        "-i", input_video,
        "-vf",
        "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920",
        "-y",
        output_video
    ]

    subprocess.run(cmd)