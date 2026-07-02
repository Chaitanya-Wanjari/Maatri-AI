from backend.llm.gemini_client import generate as gemini_generate

from .config import MEDICAL_DISCLAIMER


def build_prompt(
    query: str,
    retrieved_docs,
):
    """
    Build a grounded prompt using only retrieved evidence.
    """

    evidence = []

    for i, doc in enumerate(retrieved_docs, start=1):

        evidence.append(
            f"""
Document {i}
Source: {doc["source"]}

Content:
{doc["text"]}
"""
        )

    context = "\n".join(evidence)

    return f"""
You are Maatri AI, an evidence-based maternal healthcare assistant.

IMPORTANT RULES:

1. Answer ONLY using the retrieved evidence.
2. Never invent medical facts.
3. If the evidence is insufficient, clearly state that.
4. Never claim certainty unless supported.
5. Keep the response empathetic and concise.

Retrieved Evidence:

{context}

User Question:

{query}

Answer:
"""


def generate_answer(
    query: str,
    retrieved_docs,
):

    prompt = build_prompt(
        query,
        retrieved_docs,
    )

    answer = gemini_generate(prompt)

    return {
        "answer": answer,
        "disclaimer": MEDICAL_DISCLAIMER,
    }