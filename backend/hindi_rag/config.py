from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODELS_DIR = BASE_DIR / "models"

EMBEDDINGS_DIR = BASE_DIR / "embeddings"

BI_ENCODER_PATH = MODELS_DIR / "bi-encoder"

CROSS_ENCODER_PATH = MODELS_DIR / "crossencoder_finetuned"

FAISS_INDEX = EMBEDDINGS_DIR / "index.faiss"

METADATA_FILE = EMBEDDINGS_DIR / "meta.json"

TOP_K = 5

RERANK_CANDIDATES = 15

MEDICAL_DISCLAIMER = (
    "⚠️ यह जानकारी केवल शैक्षिक उद्देश्य के लिए है। "
    "चिकित्सीय सलाह के लिए अपने डॉक्टर से संपर्क करें।"
)