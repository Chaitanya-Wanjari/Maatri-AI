"""
Resource Loader for the English RAG Pipeline.

Loads heavyweight resources only once and exposes them
through cached accessor functions.
"""

from functools import lru_cache
import json

import faiss
from sentence_transformers import SentenceTransformer, CrossEncoder

from .config import (
    EMBEDDING_MODEL,
    CROSS_ENCODER_PATH,
    QA_INDEX_FILE,
    QA_TEXT_FILE,
    ARTICLE_INDEX_FILE,
    ARTICLE_TEXT_FILE,
    BOOK_INDEX_FILE,
    BOOK_TEXT_FILE,
)


# ------------------------------------------------------------------
# Embedding Model
# ------------------------------------------------------------------

@lru_cache(maxsize=1)
def get_encoder():
    print("Loading embedding model...")
    return SentenceTransformer(EMBEDDING_MODEL)


# ------------------------------------------------------------------
# Cross Encoder
# ------------------------------------------------------------------

@lru_cache(maxsize=1)
def get_cross_encoder():
    print("Loading cross encoder...")
    return CrossEncoder(str(CROSS_ENCODER_PATH))


# ------------------------------------------------------------------
# FAISS Loader
# ------------------------------------------------------------------

def load_faiss_index(index_path, texts_path):
    """
    Loads a FAISS index and its corresponding text corpus.
    """

    index = faiss.read_index(str(index_path))

    with open(texts_path, "r", encoding="utf-8") as f:
        texts = json.load(f)

    return index, texts


# ------------------------------------------------------------------
# Vector Stores
# ------------------------------------------------------------------

@lru_cache(maxsize=1)
def get_vectorstores():
    """
    Loads all English FAISS indexes only once.
    """

    qa_index, qa_texts = load_faiss_index(
        QA_INDEX_FILE,
        QA_TEXT_FILE,
    )

    article_index, article_texts = load_faiss_index(
        ARTICLE_INDEX_FILE,
        ARTICLE_TEXT_FILE,
    )

    book_index, book_texts = load_faiss_index(
        BOOK_INDEX_FILE,
        BOOK_TEXT_FILE,
    )

    return {
        "qa": {
            "index": qa_index,
            "texts": qa_texts,
        },
        "article": {
            "index": article_index,
            "texts": article_texts,
        },
        "book": {
            "index": book_index,
            "texts": book_texts,
        },
    }