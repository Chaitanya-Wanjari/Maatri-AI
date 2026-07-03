import numpy as np

from .config import (
    TOP_K,
    RERANK_CANDIDATES,
)

from .loader import (
    get_encoder,
    get_cross_encoder,
    get_vectorstore,
)


def retrieve(query: str):

    encoder = get_encoder()

    reranker = get_cross_encoder()

    index, docs = get_vectorstore()

    embedding = encoder.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    scores, ids = index.search(
        embedding,
        RERANK_CANDIDATES,
    )

    candidates = []

    for score, idx in zip(scores[0], ids[0]):

        if idx < 0:
            continue

        candidates.append(
            {
                "text": docs[idx],
                "source": "Hindi KB",
                "dense_score": float(score),
            }
        )

    pairs = [
        (query, doc["text"])
        for doc in candidates
    ]

    rerank_scores = reranker.predict(pairs)

    for doc, score in zip(
        candidates,
        rerank_scores,
    ):
        doc["rerank_score"] = float(score)

    candidates.sort(
        key=lambda x: x["rerank_score"],
        reverse=True,
    )

    return candidates[:TOP_K]