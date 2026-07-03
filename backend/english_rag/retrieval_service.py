from .loader import (
    get_encoder,
    get_cross_encoder,
    get_vectorstores,
)

from .config import (
    TOP_K,
    RERANK_CANDIDATES,
)


def retrieve(query: str):
    """
    Hybrid retrieval with cross-encoder reranking.
    """

    encoder = get_encoder()
    reranker = get_cross_encoder()

    vectorstores = get_vectorstores()

    query_embedding = encoder.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    candidates = []

    # Search all vector stores
    for source_name, store in vectorstores.items():

        index = store["index"]
        texts = store["texts"]

        scores, ids = index.search(
            query_embedding,
            TOP_K * 3,
        )

        for score, idx in zip(scores[0], ids[0]):

            candidates.append(
                {
                    "text": str(texts[idx]),
                    "source": source_name,
                    "dense_score": float(score),
                }
            )

    # Sort by dense retrieval score
    candidates.sort(
        key=lambda x: x["dense_score"],
        reverse=True,
    )

    # Keep only top candidates for reranking
    candidates = candidates[:RERANK_CANDIDATES]

    # Cross-encoder reranking
    unique = {}
    for doc in candidates:
       unique.setdefault(doc["text"], doc)

    candidates = list(unique.values())

    pairs = [
        (query, doc["text"])
        for doc in candidates
]

    rerank_scores = reranker.predict(pairs)

    for doc, score in zip(candidates, rerank_scores):
        doc["rerank_score"] = float(score)

    # Final ranking
    candidates.sort(
        key=lambda x: x["rerank_score"],
        reverse=True,
    )

    return candidates[:TOP_K]