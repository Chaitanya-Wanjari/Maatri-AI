from .gemini_client import generate as gemini_generate


class GeminiProvider:
    def generate(self, prompt: str):
        return gemini_generate(prompt)