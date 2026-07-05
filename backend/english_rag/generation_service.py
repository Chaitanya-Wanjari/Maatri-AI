"""
Generation Service

Uses Gemini to generate grounded answers from retrieved evidence.
Falls back to evidence-only mode if Gemini is unavailable.
"""

from backend.llm.provider import generate
from backend.utils.fallback import evidence_summary

from .config import MEDICAL_DISCLAIMER


def generate_answer(
    query: str,
    retrieved_docs: list,
    history: list,
    agent_type: str = "health",
):
    context = "\n\n".join(
        doc["text"]
        for doc in retrieved_docs
    )

    history_text = ""

    for msg in history:
        history_text += (
            f"{msg['role']}: {msg['content']}\n"
        )

    # ----------------------------------------------------
    # Agent-specific system prompt
    # ----------------------------------------------------

    if agent_type == "emergency":

        system_prompt = """
You are Maatri AI.

You are an emergency maternal healthcare assistant.

Rules:

- Stay calm and reassuring.
- Use ONLY the evidence.
- If the evidence reasonably supports urgent medical attention,
  clearly advise the user to seek immediate medical care.
- Do NOT require exact wording.
- Only answer "I don't know" if none of the evidence is useful.
- Never invent medical information.
"""

    elif agent_type == "nutrition":

        system_prompt = """
You are Maatri AI.

You are a maternal nutrition expert.

Rules:

- Use ONLY the evidence.
- Be practical and encouraging.
- If foods are generally safe according to the evidence,
  say so naturally.
- Do not answer "I don't know" unless no relevant evidence exists.
"""

    else:

        system_prompt = """
You are Maatri AI.

You are an empathetic maternal healthcare assistant.

Rules:

- Use the conversation history for follow-up questions.
- Answer ONLY using the evidence.
- If the evidence is reasonably relevant,
  use it even if the wording is not identical.
- Only say "I don't know" if NONE of the evidence helps.
- Never invent medical advice.
- Keep answers concise and medically safe.
"""

    prompt = f"""
{system_prompt}

========================

Conversation History:

{history_text}

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