import os
import time
from functools import lru_cache

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

load_dotenv()


@lru_cache(maxsize=1)
def get_client():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found in environment variables."
        )

    return genai.Client(api_key=api_key)


@lru_cache(maxsize=256)
def generate(prompt: str):

    client = get_client()

    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )

            return response.text

        except ClientError as e:

            print(f"\nGemini Error ({attempt+1}/{retries})")
            print(e)

            if attempt < retries - 1:

                wait = 2 ** attempt

                print(f"Retrying in {wait} seconds...\n")

                time.sleep(wait)

            else:

                print("\nSwitching to fallback mode.\n")

                return None