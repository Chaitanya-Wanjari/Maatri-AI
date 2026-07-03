from fastapi import APIRouter

from backend.agents.planner_agent import PlannerAgent
from backend.english_rag.schemas import (
    ChatRequest,
    ChatResponse,
)

router = APIRouter()

planner = PlannerAgent()


@router.get("/")
def health():
    return {
        "status": "running",
        "service": "Maatri AI"
    }


@router.post(
    "/ask",
    response_model=ChatResponse,
)
def ask(request: ChatRequest):

    response = planner.run(request.question)

    return response