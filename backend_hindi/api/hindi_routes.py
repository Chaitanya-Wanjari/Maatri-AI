from fastapi import APIRouter

from backend_hindi.agents.hindi_agent import HindiAgent

from backend_hindi.english_rag.schemas import (
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