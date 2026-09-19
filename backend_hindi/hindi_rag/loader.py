from functools import lru_cache
from pathlib import Path
import json
import os
import gc
import requests
import faiss
from sentence_transformers import SentenceTransformer

from .config import (
    FAISS_INDEX,
    METADATA_FILE,
)

BASE_DIR = Path(__file__).resolve().parent


# -----------------------------
# Hindi Embedding (Local)
# -----------------------------

@lru_cache(maxsize=1)
def get_encoder():
    print("Loading Hindi embedding model locally...")
    return SentenceTransformer("intfloat/multilingual-e5-base")


# -----------------------------
# Hindi Cross Encoder (HF Serverless)
# -----------------------------

class HFHindiCrossEncoder:

    def __init__(self):
        self.url = (
            "https://router.huggingface.co/"
            "hf-inference/models/Chaitanya30/maatri-hindi-crossencoder"
        )

        self.headers = {
            "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
            "Content-Type": "application/json",
        }

    def predict(self, sentence_pairs):
        response = requests.post(
            self.url,
            headers=self.headers,
            json={"inputs": sentence_pairs},
            timeout=300,
        )

        response.raise_for_status()

        scores = response.json()

        return [
            s["score"] if isinstance(s, dict) else float(s)
            for s in scores
        ]


# -----------------------------
# Cached Cross Encoder
# -----------------------------

@lru_cache(maxsize=1)
def get_cross_encoder():
    print("Using HF Serverless Hindi CrossEncoder...")
    return HFHindiCrossEncoder()


# -----------------------------
# FAISS Vector Store
# -----------------------------

@lru_cache(maxsize=1)
def get_vectorstore():
    index = faiss.read_index(str(FAISS_INDEX))

    with open(METADATA_FILE, encoding="utf-8") as f:
        docs = json.load(f)

    return index, docs


# -----------------------------
# Cleanup
# -----------------------------

def unload_models():
    """
    Free cached models after each request to reduce Railway memory usage.
    """
    get_encoder.cache_clear()
    get_cross_encoder.cache_clear()
    gc.collect()