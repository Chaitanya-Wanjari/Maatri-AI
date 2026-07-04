"""
Main Hindi Knowledge Engine
"""

import time

from backend.memory.store import (
    get_history,
    add_message,
)

from backend.routing.query_rewriter import rewrite_query

from .retrieval_service import retrieve
from .generation_service import generate_answer


def answer(
    query: str,
    session_id: str,
):
    # -----------------------------
    # Load conversation history
    # -----------------------------

    history = get_history(session_id)

    # -----------------------------
    # Rewrite follow-up question
    # -----------------------------

    rewritten_query = rewrite_query(
        query=query,
        history=history,
    )

    print("\n========== QUERY REWRITE ==========")
    print("Original :", query)
    print("Rewritten:", rewritten_query)
    print("===================================\n")

    # -----------------------------
    # Start timer
    # -----------------------------

    start = time.perf_counter()

    # -----------------------------
    # Retrieve documents
    # -----------------------------

    documents = retrieve(rewritten_query)

    # -----------------------------
    # Generate grounded answer
    # -----------------------------

    response = generate_answer(
        query=rewritten_query,
        retrieved_docs=documents,
        history=history,
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
        "language": "Hindi",
        "knowledge_engine": "Hindi RAG",
        "documents_used": len(documents),
        "source_distribution": source_counts,
        "latency_ms": latency_ms,
    }

    # -----------------------------
    # Save conversation
    # -----------------------------

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