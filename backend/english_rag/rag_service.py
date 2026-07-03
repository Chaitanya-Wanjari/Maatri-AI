"""
Main English Knowledge Engine
"""

import time

from .generation_service import generate_answer
from .retrieval_service import retrieve


def answer(query: str):

    # -----------------------------
    # Start timer
    # -----------------------------

    start = time.perf_counter()

    # -----------------------------
    # Retrieve documents
    # -----------------------------

    documents = retrieve(query)

    # -----------------------------
    # Generate response
    # -----------------------------

    response = generate_answer(
        query=query,
        retrieved_docs=documents,
    )

    # -----------------------------
    # Calculate latency
    # -----------------------------

    latency_ms = round(
        (time.perf_counter() - start) * 1000,
        2,
    )

    # -----------------------------
    # Source statistics
    # -----------------------------

    source_counts = {}

    for doc in documents:

        source = doc["source"]

        source_counts[source] = (
            source_counts.get(source, 0) + 1
        )

    # -----------------------------
    # Build response
    # -----------------------------

    response["sources"] = documents

    response["metadata"] = {
        "language": "English",
        "knowledge_engine": "English RAG",
        "documents_used": len(documents),
        "source_distribution": source_counts,
        "latency_ms": latency_ms,
    }

    return response