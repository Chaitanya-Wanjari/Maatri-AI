from .retrieval_service import retrieve
from .generation_service import generate_answer


def answer(query: str):

    documents = retrieve(query)

    response = generate_answer(
        query,
        documents,
    )

    response["sources"] = documents

    source_counts = {}

    for doc in documents:
        source = doc["source"]
        source_counts[source] = (
            source_counts.get(source, 0) + 1
        )

    response["metadata"] = {
        "language": "Hindi",
        "knowledge_engine": "Hindi RAG",
        "documents_used": len(documents),
        "source_distribution": source_counts,
    }

    return response