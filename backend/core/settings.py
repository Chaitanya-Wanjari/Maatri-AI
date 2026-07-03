import os
from dotenv import load_dotenv

load_dotenv()

# Current provider
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Ollama
OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434",
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:3b",
)