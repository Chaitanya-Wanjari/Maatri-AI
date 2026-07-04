from pydantic import BaseModel
from typing import List


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
    