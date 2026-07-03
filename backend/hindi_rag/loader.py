from functools import lru_cache
import json

import faiss

from sentence_transformers import (
    SentenceTransformer,
    CrossEncoder,
)

from .config import (
    BI_ENCODER_PATH,
    CROSS_ENCODER_PATH,
    FAISS_INDEX,
    METADATA_FILE,
)


@lru_cache(maxsize=1)
def get_encoder():
    print("Loading Hindi embedding model...")
    return SentenceTransformer(str(BI_ENCODER_PATH))


@lru_cache(maxsize=1)
def get_cross_encoder():
    print("Loading Hindi cross encoder...")
    return CrossEncoder(str(CROSS_ENCODER_PATH))


@lru_cache(maxsize=1)
def get_vectorstore():

    index = faiss.read_index(str(FAISS_INDEX))

    with open(METADATA_FILE, encoding="utf-8") as f:
        docs = json.load(f)

    return index, docs