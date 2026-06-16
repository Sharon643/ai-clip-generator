def find_interesting_segments(segments):

    keywords = [
        "secret",
        "mistake",
        "important",
        "crazy",
        "never",
        "best",
        "future",
        "ai",
        "million",
        "success"
    ]

    clips = []

    for segment in segments:

        text = segment["text"].lower()

        if any(word in text for word in keywords):

            clips.append({
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            })

    return clips