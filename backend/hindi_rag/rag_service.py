"""
Main Hindi Knowledge Engine
"""

import time

from backend.memory.store import (
    get_history,
    add_message,
)

from .retrieval_service import retrieve
from .generation_service import generate_answer


def answer(
    query: str,
    session_id: str,
):
    history = get_history(session_id)

    start = time.perf_counter()

    documents = retrieve(query)

    response = generate_answer(
        query=query,
        retrieved_docs=documents,
        history=history,
    )

    latency_ms = round(
        (time.perf_counter() - start) * 1000,
        2,
    )

    source_counts = {}

    for doc in documents:
        source = doc["source"]

        source_counts[source] = (
            source_counts.get(source, 0) + 1
        )

    response["sources"] = documents

    response["metadata"] = {
        "language": "Hindi",
        "knowledge_engine": "Hindi RAG",
        "documents_used": len(documents),
        "source_distribution": source_counts,
        "latency_ms": latency_ms,
    }

    add_message(
        session_id,
        "user",
        query,
    )

    add_message(
        session_id,
        "assistant",
        response["answer"],
    )

    return response