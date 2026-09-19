from functools import lru_cache
from pathlib import Path
import json
import os

import faiss
import numpy as np
import requests

from .config import (
    FAISS_INDEX,
    METADATA_FILE,
)

BASE_DIR = Path(__file__).resolve().parent


# -----------------------------
# Hindi Embedding (Serverless)
# -----------------------------

class HFHindiEncoder:

    def __init__(self):
        self.url = (
            "https://api-inference.huggingface.co/models/"
            "intfloat/multilingual-e5-base"
        )

        self.headers = {
            "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
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
                json={"inputs": f"query: {text}"},
                timeout=120,
            )

            response.raise_for_status()

            vec = np.array(response.json(), dtype=np.float32)

            if normalize_embeddings:
                vec = vec / np.linalg.norm(vec)

            embeddings.append(vec)

        return np.vstack(embeddings)


# -----------------------------
# Hindi Cross Encoder
# -----------------------------

class HFHindiCrossEncoder:

    def __init__(self):

        self.url = (
            "https://api-inference.huggingface.co/models/"
            "Chaitanya30/maatri-hindi-crossencoder"
        )

        self.headers = {
            "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
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
            s["score"] if isinstance(s, dict) else s
            for s in scores
        ]


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