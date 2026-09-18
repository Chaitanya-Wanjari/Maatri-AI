import os
from pathlib import Path
from dotenv import load_dotenv

# Explicitly load backend/.env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Current provider
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemma")

# Google-hosted Gemma
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMMA_MODEL = os.getenv("GEMMA_MODEL", "gemma-3-4b-it")

# Gemini (optional fallback)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Ollama (future)
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")