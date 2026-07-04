import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
from mcp.server.fastmcp import FastMCP

from backend.routing.language_detector import detect_language
from backend.english_rag.rag_service import answer as english_answer
from backend.hindi_rag.rag_service import answer as hindi_answer
from backend.memory.store import get_history

mcp = FastMCP("Maatri MCP")


@mcp.tool()
def detect_query_language(query: str) -> str:
    """
    Detect the language of a query.
    """
    return detect_language(query)


@mcp.tool()
def ask_english_maatri(
    question: str,
    session_id: str = "mcp",
):
    """
    Ask the English maternal healthcare agent.
    """
    return english_answer(
        query=question,
        session_id=session_id,
    )


@mcp.tool()
def ask_hindi_maatri(
    question: str,
    session_id: str = "mcp",
):
    """
    Ask the Hindi maternal healthcare agent.
    """
    return hindi_answer(
        query=question,
        session_id=session_id,
    )


@mcp.tool()
def conversation_history(session_id: str):
    """
    Return conversation history.
    """
    return get_history(session_id)


if __name__ == "__main__":
    mcp.run()

