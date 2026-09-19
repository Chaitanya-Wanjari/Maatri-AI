from functools import lru_cache
from pathlib import Path
import json
import os
import gc

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

    def encode(
        self,
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ):
        embeddings = []

        for text in texts:
            vec = np.array(
                HF_CLIENT.feature_extraction(
                    model="intfloat/multilingual-e5-base",
                    text=f"query: {text}",
                ),
                dtype=np.float32,
            )

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

    def predict(self, sentence_pairs):
        scores = []

        for query, passage in sentence_pairs:
            result = HF_CLIENT.sentence_similarity(
                model="Chaitanya30/maatri-hindi-crossencoder",
                sentence=query,
                other_sentences=[passage],
            )
            scores.append(float(result[0]))

        return scores


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