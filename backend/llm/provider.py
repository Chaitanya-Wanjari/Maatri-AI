from backend.core.settings import LLM_PROVIDER

from .gemini_client import generate as gemini_generate
from .ollama_client import generate as ollama_generate


LAST_PROVIDER = None


def generate(prompt: str):
    """
    Unified LLM Provider.

    Returns a string or None.
    """

    global LAST_PROVIDER

    if LLM_PROVIDER.lower() == "ollama":

        LAST_PROVIDER = "Ollama"

        return ollama_generate(prompt)

    result = gemini_generate(prompt)

    if result is not None:

        LAST_PROVIDER = "Gemini 2.5 Flash"

        return result

    print("\nSwitching to Ollama fallback...\n")

    LAST_PROVIDER = "Ollama"

    return ollama_generate(prompt)


def get_last_provider():

    return LAST_PROVIDER