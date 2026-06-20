from src.gemini_ranking import get_llm

def generate_hook(text):

    llm = get_llm()

    prompt = f"""
Create a viral YouTube Shorts hook.

Rules:
- Maximum 10 words
- Curiosity driven
- No clickbait
- Must be based on transcript

Transcript:
{text}

Return ONLY the hook.
"""

    response = llm.invoke(prompt)

    return response.content.strip()