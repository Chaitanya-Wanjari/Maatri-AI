import os

from .gemma_provider import GemmaProvider
from .gemini_provider import GeminiProvider


def get_llm():
    provider = os.getenv("LLM_PROVIDER", "gemma").lower()

    if provider == "gemma":
        return GemmaProvider()

    return GeminiProvider()


def generate(prompt: str):
    llm = get_llm()
    return llm.generate(prompt)