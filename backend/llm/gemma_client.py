from functools import lru_cache

from google import genai
from backend.core.settings import GOOGLE_API_KEY, GEMMA_MODEL


@lru_cache(maxsize=1)
def get_client():
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not found.")
    return genai.Client(api_key=GOOGLE_API_KEY)


def generate(prompt: str):
    try:
        client = get_client()

        response = client.models.generate_content(
            model=GEMMA_MODEL,
            contents=prompt,
        )

        if not response.text:
            return None

        return {
            "text": response.text.strip(),
            "provider": "Gemma",
        }

    except Exception as e:
        print("\nGemma Error")
        print(type(e).__name__)
        print(e)
        return None