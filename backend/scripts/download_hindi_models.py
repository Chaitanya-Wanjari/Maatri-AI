from sentence_transformers import SentenceTransformer, CrossEncoder
import os

MODELS_DIR = "backend/models"

os.makedirs(MODELS_DIR, exist_ok=True)

print("Downloading multilingual embedding model...")

embedder = SentenceTransformer(
    "intfloat/multilingual-e5-base"
)

embedder.save(
    os.path.join(MODELS_DIR, "hi_biencoder")
)

print("✓ Bi-encoder saved")

print("Downloading cross encoder...")

cross = CrossEncoder(
    "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"
)

cross.save(
    os.path.join(MODELS_DIR, "hi_crossencoder")
)

print("✓ Cross encoder saved")