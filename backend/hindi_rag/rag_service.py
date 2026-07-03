from .retrieval_service import retrieve
from .generation_service import generate_answer


def answer(query: str):

    documents = retrieve(query)

    response = generate_answer(
        query,
        documents,
    )

    response["sources"] = documents

    response["metadata"] = {
        "language": "Hindi",
        "knowledge_engine": "Hindi RAG",
        "documents_used": len(documents),
    }

    return response