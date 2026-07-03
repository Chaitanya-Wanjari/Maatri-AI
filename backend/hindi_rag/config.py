from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODELS_DIR = BASE_DIR / "models"

EMBEDDING_MODEL = "backend/models/hi_biencoder"

BI_ENCODER_PATH = MODELS_DIR / "bi-encoder"

CROSS_ENCODER = "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"
FAISS_INDEX = "backend/hindi_rag/embeddings/index.faiss"
METADATA = "backend/hindi_rag/embeddings/meta.json"
TOP_K = 5

RERANK_CANDIDATES = 15

MEDICAL_DISCLAIMER = (
    "⚠️ यह जानकारी केवल शैक्षिक उद्देश्य के लिए है। "
    "चिकित्सीय सलाह के लिए अपने डॉक्टर से संपर्क करें।"
)