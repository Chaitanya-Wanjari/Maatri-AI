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

from pathlib import Path
from functools import lru_cache
from sentence_transformers import CrossEncoder

BASE_DIR = Path(__file__).resolve().parent


from functools import lru_cache
import os
from sentence_transformers import CrossEncoder

@lru_cache(maxsize=1)
def get_cross_encoder():
    print("Loading Hindi fine-tuned cross encoder...")
    return CrossEncoder(
        "Chaitanya30/maatri-hindi-crossencoder",
        token=os.getenv("HF_TOKEN"),
    )

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