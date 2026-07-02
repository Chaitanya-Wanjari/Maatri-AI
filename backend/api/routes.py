from fastapi import APIRouter

from backend.english_rag.schemas import (
    ChatRequest,
    ChatResponse,
)

from backend.english_rag.rag_service import answer

router = APIRouter()


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

    response = answer(
        request.question
    )

    return response