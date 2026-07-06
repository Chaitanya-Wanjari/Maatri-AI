from typing import Any, Dict, List

from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str
    session_id: str = "default"


class RetrievedDocument(BaseModel):
    text: str
    source: str
    dense_score: float
    rerank_score: float


class ChatResponse(BaseModel):
    answer: str
    disclaimer: str

    sources: List[RetrievedDocument]

    # Explainability
    metadata: Dict[str, Any]

    trace: Dict[str, Any]

    agent: str

    class Config:
        extra = "allow"