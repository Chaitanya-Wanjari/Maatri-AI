"""
Configuration for the English RAG Pipeline
"""

from pathlib import Path

# -------------------------------------------------------------------
# Base Paths
# -------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models"
VECTORSTORE_DIR = BASE_DIR / "vectorstore"
KNOWLEDGE_BASE_DIR = BASE_DIR / "knowledge_base"

# -------------------------------------------------------------------
# Embedding Model
# -------------------------------------------------------------------

EMBEDDING_MODEL = "multi-qa-mpnet-base-dot-v1"

# -------------------------------------------------------------------
# Cross Encoder
# -------------------------------------------------------------------

CROSS_ENCODER_PATH = MODEL_DIR / "fine_tuned_cross_encoder"

# -------------------------------------------------------------------
# Generator
# -------------------------------------------------------------------

GENERATOR_MODEL_PATH = MODEL_DIR / "gemma-2b-it"

# -------------------------------------------------------------------
# Retrieval
# -------------------------------------------------------------------

TOP_K = 5

RERANK_CANDIDATES = 15

# -------------------------------------------------------------------
# Generation Parameters
# -------------------------------------------------------------------

MAX_NEW_TOKENS = 200

TEMPERATURE = 0.7

TOP_P = 0.9

# -------------------------------------------------------------------
# Vector Index Files
# -------------------------------------------------------------------

QA_INDEX_FILE = MODEL_DIR / "english" / "qa_index.faiss"
QA_TEXT_FILE = MODEL_DIR / "english" / "qa_index_texts.json"

ARTICLE_INDEX_FILE = MODEL_DIR / "english" / "doc.faiss"
ARTICLE_TEXT_FILE = MODEL_DIR / "english" / "doc_texts.json"

BOOK_INDEX_FILE = MODEL_DIR / "english" / "bookwho.faiss"
BOOK_TEXT_FILE = MODEL_DIR / "english" / "bookwho_texts.json"

# -------------------------------------------------------------------
# Disclaimer
# -------------------------------------------------------------------

MEDICAL_DISCLAIMER = (
    "⚠️ This information is for educational purposes only. "
    "Please consult a qualified healthcare provider for medical advice."
)