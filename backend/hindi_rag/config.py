from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODELS_DIR = BASE_DIR.parent / "models"

BI_ENCODER_PATH = MODELS_DIR / "hi_biencoder"

CROSS_ENCODER_PATH = MODELS_DIR / "hi_crossencoder"

FAISS_INDEX = BASE_DIR / "embeddings" / "index.faiss"

METADATA_FILE = BASE_DIR / "embeddings" / "meta.json"

TOP_K = 5
RERANK_CANDIDATES = 15

MEDICAL_DISCLAIMER = (
    "⚠️ यह जानकारी केवल शैक्षिक उद्देश्य के लिए है। "
    "चिकित्सीय सलाह के लिए अपने डॉक्टर से संपर्क करें।"
)