from google.adk.tools import FunctionTool

from backend.english_rag.rag_service import answer as english_answer
from backend.hindi_rag.rag_service import answer as hindi_answer


def english_rag_tool(
    query: str,
    session_id: str,
):
    """
    Search the English maternal health knowledge base.
    """

    return english_answer(
        query=query,
        session_id=session_id,
    )


def hindi_rag_tool(
    query: str,
    session_id: str,
):
    """
    Search the Hindi maternal health knowledge base.
    """

    return hindi_answer(
        query=query,
        session_id=session_id,
    )


english_tool = FunctionTool(english_rag_tool)

hindi_tool = FunctionTool(hindi_rag_tool)