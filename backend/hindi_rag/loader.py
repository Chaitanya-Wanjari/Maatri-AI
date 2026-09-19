from functools import lru_cache
from pathlib import Path
import json
import os
import gc
import requests
import faiss
import numpy as np
from huggingface_hub import InferenceClient

from .config import (
    FAISS_INDEX,
    METADATA_FILE,
)

BASE_DIR = Path(__file__).resolve().parent


# -----------------------------
# Shared HF Client
# -----------------------------

HF_CLIENT = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("HF_TOKEN"),
)


# -----------------------------
# Hindi Embedding (Serverless)
# -----------------------------

class HFHindiEncoder:

    def __init__(self):
        self.url = (
            "https://router.huggingface.co/"
            "hf-inference/models/intfloat/multilingual-e5-base"
        )

        self.headers = {
            "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
            "Content-Type": "application/json",
        }

    def encode(
        self,
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ):
        embeddings = []

        for text in texts:
            response = requests.post(
                self.url,
                headers=self.headers,
                json={
                    "inputs": f"query: {text}",
                    "options": {"wait_for_model": True},
                },
                timeout=120,
            )

            response.raise_for_status()

            data = response.json()

# Handle different HF response formats
            if isinstance(data, dict):
                if "embeddings" in data:
                    vec = np.array(data["embeddings"][0], dtype=np.float32)
                elif "data" in data:
                    vec = np.array(data["data"][0]["embedding"], dtype=np.float32)
                else:
                     raise RuntimeError(f"Unexpected HF response: {data}")
            else:
                vec = np.array(data, dtype=np.float32)

            if normalize_embeddings:
                norm = np.linalg.norm(vec)
                if norm > 0:
                    vec = vec / norm

            embeddings.append(vec)

        return np.vstack(embeddings)

# -----------------------------
# Hindi Cross Encoder (Serverless)
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
# Cached Accessors
# -----------------------------

@lru_cache(maxsize=1)
def get_encoder():
    print("Using HF Serverless Hindi encoder...")
    return HFHindiEncoder()


@lru_cache(maxsize=1)
def get_cross_encoder():
    print("Using HF Serverless Hindi CrossEncoder...")
    return HFHindiCrossEncoder()


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
    get_encoder.cache_clear()
    get_cross_encoder.cache_clear()
    gc.collect()