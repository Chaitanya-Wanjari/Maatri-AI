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

        record = docs[idx]

        if isinstance(record, dict):

            text = record.get("text", "")
            source = record.get("source", "Hindi KB")

        else:

            text = record
            source = "Hindi KB"

        candidates.append(
           {
              "text": text,
              "source": source,
              "dense_score": float(score),
           }
)
    
    
    pairs = []

    for doc in candidates:

       text = doc["text"]

       if isinstance(text, dict):
          text = text.get("text", "")

       pairs.append((query, text))

    rerank_scores = reranker.predict(pairs)

    for doc, score in zip(candidates, rerank_scores):
        doc["rerank_score"] = float(score)

    candidates.sort(
        key=lambda x: x["rerank_score"],
        reverse=True,
    )

    unique = []
    seen = set()

    for doc in candidates:
       if doc["text"] in seen:
          continue

       seen.add(doc["text"])
       unique.append(doc)

    return unique[:TOP_K]