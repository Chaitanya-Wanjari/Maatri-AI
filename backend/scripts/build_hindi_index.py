import os
import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

MODEL_PATH = "backend/models/hi_biencoder"

CORPUS = "backend/data/hindi/merged_corpus_meta.json"

OUTPUT = "backend/hindi_rag/embeddings"

os.makedirs(OUTPUT, exist_ok=True)

print("Loading model...")

model = SentenceTransformer(MODEL_PATH)

print("Loading corpus...")

with open(CORPUS, encoding="utf-8") as f:
    docs = json.load(f)

texts = [
    doc["text"]
    for doc in docs
]

print(f"Embedding {len(texts)} documents...")

embeddings = model.encode(
    texts,
    normalize_embeddings=True,
    convert_to_numpy=True,
    show_progress_bar=True
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(
    embeddings.astype(np.float32)
)

faiss.write_index(
    index,
    os.path.join(OUTPUT, "index.faiss")
)

with open(
    os.path.join(OUTPUT, "meta.json"),
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        docs,
        f,
        ensure_ascii=False,
        indent=2
    )

print("✓ Hindi FAISS index built")