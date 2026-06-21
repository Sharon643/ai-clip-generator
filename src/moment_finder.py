import json
from llm import get_local_llm

def find_best_moment(chunk_text):

    llm = get_local_llm()

    prompt = f"""
You are an expert YouTube Shorts editor.

Analyze the transcript below.

Find the BEST moment for a short-form clip.

Rules:
- 20 to 40 seconds
- Most surprising, emotional, insightful, or viral moment
- Return ONLY valid JSON

Example:

{{
    "start_percent": 20,
    "end_percent": 70,
    "reason": "Strong insight occurs here"
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