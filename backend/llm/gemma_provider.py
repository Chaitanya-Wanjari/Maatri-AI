from .gemma_client import generate as gemma_generate


class GemmaProvider:
    def generate(self, prompt: str):
        return gemma_generate(prompt)