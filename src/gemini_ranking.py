import json
from src.llm import get_llm , get_local_llm


def rank_chunk(chunk_text):

    llm = get_local_llm()

    prompt = f"""
        You are an expert short-form content editor.

        Rate this transcript chunk from 1-100.

        Criteria:
        - surprising insights
        - controversial opinions
        - strong predictions
        - emotional moments
        - practical advice
        - viral potential

        Return ONLY valid JSON.

        Example:
        {{
            "score": 85,
            "reason": "Strong prediction about AI jobs"
        }}

        Transcript:
        {chunk_text}
        """

    response = llm.invoke(prompt)

    cleaned = (
        response.content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned)