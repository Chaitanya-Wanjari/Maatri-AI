from fastapi import APIRouter

from backend_hindi.agents.planner_agent import PlannerAgent
from backend_hindi.english_rag.schemas import (
    ChatRequest,
    ChatResponse,
)

router = APIRouter()

print("Creating PlannerAgent...")
planner = PlannerAgent()
print("PlannerAgent created.")


@router.get("/")
def health():
    return {
        "status": "running",
        "service": "Maatri AI",
    }


@router.post(
    "/ask",
    response_model=ChatResponse,
)
def ask(request: ChatRequest):

    response = planner.run(
        request.question,
        request.session_id,
    )
    print("Planner finished")
    return response

    # Do NOT overwrite trace here.
    # It is already created by the RAG service.

    return response