def create_chunks(segments,chunk_duration=120):

    chunks = []

    current_chunk = []
    chunk_start = None

    for segment in segments:

        if chunk_start is None:
            chunk_start = segment["start"]

        current_chunk.append(segment)

        duration = (
            segment["end"]
            - chunk_start
        )

        if duration >= chunk_duration:

            chunks.append({

                "start": chunk_start,

                "end": segment["end"],

                "text": " ".join(
                    s["text"]
                    for s in current_chunk
                )

            })

            current_chunk = []
            chunk_start = None

    return chunks