import os
import time
from functools import lru_cache

from dotenv import load_dotenv
from google import genai

load_dotenv()


@lru_cache(maxsize=1)
def get_client():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found."
        )

    return genai.Client(api_key=api_key)


@lru_cache(maxsize=256)
def generate(prompt: str):

    client = get_client()

    retries = 1

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            if (
                response is None
                or response.text is None
                or not response.text.strip()
            ):
                return None

            return {
                "text": response.text.strip(),
                "provider": "Gemini 2.5 Flash",
            }

        except Exception as e:

            print("\nGemini Error")
            print(type(e).__name__)
            print(e)

            if attempt < retries - 1:

                time.sleep(1)

            else:

                return None
            