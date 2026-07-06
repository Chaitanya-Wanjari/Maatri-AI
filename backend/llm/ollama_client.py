import requests

from backend.core.settings import (
    OLLAMA_MODEL,
    OLLAMA_URL,
)


def generate(prompt: str):

    url = f"{OLLAMA_URL}/api/generate"

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=120,
        )

        response.raise_for_status()

        return {
            "text": response.json()["response"],
            "provider": f"Ollama ({OLLAMA_MODEL})",
        }

    except Exception as e:

        print("\nOllama Error")
        print(e)

        return None