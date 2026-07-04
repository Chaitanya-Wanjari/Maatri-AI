from fastapi import APIRouter

from backend.agents.hindi_agent import HindiAgent

from backend.english_rag.schemas import (
    ChatRequest,
    ChatResponse,
)

router = APIRouter()

agent = HindiAgent()


@router.post(
    "/ask-hindi",
    response_model=ChatResponse,
)
def ask(request: ChatRequest):

    return agent.run(request.question)