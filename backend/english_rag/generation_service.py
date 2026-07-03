"""
Generation Service

Uses Gemini to generate grounded answers from retrieved evidence.
Falls back to evidence-only mode if Gemini is unavailable.
"""

from backend.llm.provider import generate
from backend.utils.fallback import evidence_summary

from .config import MEDICAL_DISCLAIMER


def generate_answer(query: str, retrieved_docs: list):

    context = "\n\n".join(
        doc["text"]
        for doc in retrieved_docs
    )

    prompt = f"""
You are Maatri AI.

You are an empathetic maternal healthcare assistant.

Answer ONLY using the evidence below.

If the evidence is insufficient,
say that you don't know.

Keep the answer concise and medically safe.

========================

Evidence:

{context}

========================

Question:

{query}
"""

    answer = generate(prompt)

    # ----------------------------------------------------
    # Gemini unavailable
    # ----------------------------------------------------

    if answer is None:

        answer = (
            "⚠️ The language model is temporarily unavailable.\n\n"
            "The following evidence was retrieved from the medical knowledge base:\n\n"
            + evidence_summary(retrieved_docs)
        )

    return {
        "answer": answer,
        "disclaimer": MEDICAL_DISCLAIMER,
    }