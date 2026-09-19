from functools import lru_cache
from pathlib import Path
import json
import os

import faiss
import requests
from sentence_transformers import SentenceTransformer

from .config import (
    BI_ENCODER_PATH,
    FAISS_INDEX,
    METADATA_FILE,
)

BASE_DIR = Path(__file__).resolve().parent


class HFHindiCrossEncoder:
    """
    Wrapper that mimics SentenceTransformers CrossEncoder.
    Existing code can continue calling .predict(sentence_pairs).
    """

    def __init__(self):
        self.model = "Chaitanya30/maatri-hindi-crossencoder"
        self.token = os.getenv("HF_TOKEN")

        self.url = (
            f"https://api-inference.huggingface.co/models/{self.model}"
        )

        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def predict(self, sentence_pairs):
        payload = {
            "inputs": sentence_pairs
        }

        response = requests.post(
            self.url,
            headers=self.headers,
            json=payload,
            timeout=300,
        )

        response.raise_for_status()

        scores = response.json()

        # Ensure we always return a simple list of floats
        if isinstance(scores, list):
            return [
                s["score"] if isinstance(s, dict) else s
                for s in scores
            ]

        raise RuntimeError(f"Unexpected HF response: {scores}")


@lru_cache(maxsize=1)
def get_cross_encoder():
    print("Using Hugging Face Serverless Hindi CrossEncoder...")
    return HFHindiCrossEncoder()


@lru_cache(maxsize=1)
def get_encoder():
    print("Loading Hindi embedding model...")
    return SentenceTransformer(str(BI_ENCODER_PATH))


@lru_cache(maxsize=1)
def get_vectorstore():
    index = faiss.read_index(str(FAISS_INDEX))

    with open(METADATA_FILE, encoding="utf-8") as f:
        docs = json.load(f)

    return index, docs