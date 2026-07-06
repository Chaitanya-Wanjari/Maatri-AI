from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

BI_ENCODER_PATH = "intfloat/multilingual-e5-base"

CROSS_ENCODER_PATH = (
    "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"
)

FAISS_INDEX = BASE_DIR / "embeddings" / "index.faiss"

METADATA_FILE = BASE_DIR / "embeddings" / "meta.json"

TOP_K = 5
RERANK_CANDIDATES = 15

MEDICAL_DISCLAIMER = (
    "⚠️ यह जानकारी केवल शैक्षिक उद्देश्य के लिए है। "
    "चिकित्सीय सलाह के लिए अपने डॉक्टर से संपर्क करें।"
)