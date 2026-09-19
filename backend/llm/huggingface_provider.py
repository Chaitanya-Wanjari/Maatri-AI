
import os
import requests


class HuggingFaceProvider:
    def __init__(self):
        self.api_token = os.getenv("HF_API_TOKEN")
        self.model = os.getenv("HF_MODEL", "google/gemma-3-4b-it")
        self.url = f"https://router.huggingface.co/v1/chat/completions"

    def generate(self, prompt: str, system_prompt: str = "") -> str:
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 512,
            "temperature": 0.2,
        }

        response = requests.post(self.url, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        return data["choices"][0]["message"]["content"]