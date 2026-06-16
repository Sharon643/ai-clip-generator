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

        matched_keyword = None

        for keyword in keywords:
            if keyword in text:
                matched_keyword = keyword
                break

        if matched_keyword:

            clips.append({
                "start": max(0, segment["start"] - 10),
                "end": segment["end"] + 20,
                "text": segment["text"],
                "keyword": matched_keyword
            })

    return clips