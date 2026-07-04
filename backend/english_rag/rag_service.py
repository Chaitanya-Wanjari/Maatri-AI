"""
Main English Knowledge Engine
"""

import time

from backend.memory.store import (
    get_history,
    add_message,
)

from .generation_service import generate_answer
from .retrieval_service import retrieve


def answer(query: str, session_id: str):

    # -----------------------------
    # Load conversation history
    # -----------------------------

    history = get_history(session_id)

    # -----------------------------
    # Build retrieval query
    # -----------------------------

    search_query = query

    if history:

        last_user = ""

        # Find the most recent user message
        for msg in reversed(history):

            if msg["role"] == "user":

                last_user = msg["content"]

                break

        if last_user:

            search_query = (
                last_user
                + "\n"
                + query
            )

    # -----------------------------
    # Start timer
    # -----------------------------

    start = time.perf_counter()

    # -----------------------------
    # Retrieve documents
    # -----------------------------

    documents = retrieve(search_query)

    # -----------------------------
    # Generate grounded answer
    # -----------------------------

    response = generate_answer(
        query=query,
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
        "language": "English",
        "knowledge_engine": "English RAG",
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