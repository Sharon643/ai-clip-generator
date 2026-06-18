from src.scorer import score_segment

def find_interesting_segments(segments):

    clips = []

    window_size = 5

    for i in range(len(segments) - window_size + 1): 
        window = segments[
            i : i + window_size
        ]

        combined_text = " ".join(
            s["text"]
            for s in window
        )

        score = score_segment(
            combined_text
        )

        if score > 0:

            clips.append({
                "start": max(
                    0,
                    window[0]["start"] - 10
                ),

                "end": (
                    window[-1]["end"] + 20
                ),

                "text": combined_text,

                "score": score
            })

    clips.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return clips