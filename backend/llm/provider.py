from backend.core.settings import LLM_PROVIDER

from .gemini_client import generate as gemini_generate
from .ollama_client import generate as ollama_generate


def generate(prompt: str):

    if LLM_PROVIDER == "ollama":
        return ollama_generate(prompt)

    return gemini_generate(prompt)