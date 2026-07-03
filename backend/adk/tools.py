from backend.english_rag.rag_service import answer


def knowledge_engine_tool(question: str):
    """
    Tool exposed to ADK.
    """

    return answer(question)