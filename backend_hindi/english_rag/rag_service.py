"""
Main English Knowledge Engine
"""

import time

from backend_hindi.memory.store import (
    get_history,
    add_message,
)

from backend_hindi.routing.query_rewriter import rewrite_query

from .retrieval_service import retrieve
from .generation_service import generate_answer
from .loader import unload_models


def answer(
    query: str,
    session_id: str,
):
    """
    English RAG pipeline with automatic model cleanup after each request.
    """

    history = get_history(session_id)

    rewritten_query = rewrite_query(
        query=query,
        history=history,
    )

    print("\n========== QUERY REWRITE ==========")
    print("Original :", query)
    print("Rewritten:", rewritten_query)
    print("===================================\n")

    try:
        # ----------------------------------
        # Retrieval + Generation
        # ----------------------------------

        start = time.perf_counter()

        documents = retrieve(rewritten_query)

        response = generate_answer(
            query=rewritten_query,
            retrieved_docs=documents,
            history=history,
        )

        latency_ms = round(
            (time.perf_counter() - start) * 1000,
            2,
        )

        # ----------------------------------
        # Source statistics
        # ----------------------------------

        source_counts = {}

        for doc in documents:
            source = doc["source"]

            source_counts[source] = (
                source_counts.get(source, 0) + 1
            )

        response["sources"] = documents

        response["metadata"] = {
            "language": "English",
            "knowledge_engine": "English RAG",
            "documents_used": len(documents),
            "source_distribution": source_counts,
            "latency_ms": latency_ms,
            "llm": "Gemini 2.5 Flash",
            "retriever": "FAISS",
            "reranker": "Cross Encoder",
        }

        # ----------------------------------
        # Conversation Memory
        # ----------------------------------

        memory = []

        for msg in history[-4:]:
            memory.append(
                {
                    "role": msg["role"],
                    "content": msg["content"],
                }
            )

        response["trace"] = {
            "original_query": query,
            "rewritten_query": rewritten_query,
            "retrieved_documents": len(documents),
            "conversation_memory": memory,
            "retriever": "FAISS",
            "reranker": "Cross Encoder",
            "generator": response["generator"],
        }

        # ----------------------------------
        # Save Conversation
        # ----------------------------------

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

    finally:
        # Always free the heavy transformer models,
        # even if an exception occurs.
        unload_models()