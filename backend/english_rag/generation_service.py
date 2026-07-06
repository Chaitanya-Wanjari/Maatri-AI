"""
Generation Service

Uses Gemini/Ollama as the primary generator.
Falls back to a local BART summarizer.
Falls back to an evidence synthesizer if both fail.
"""

from backend.llm.provider import generate
from backend.llm.bart_summarizer import summarize
from backend.utils.fallback import evidence_summary

from .config import MEDICAL_DISCLAIMER


def generate_answer(
    query: str,
    retrieved_docs: list,
    history: list,
    agent_type: str = "health",
):
    # ----------------------------------------------------
    # Retrieved Context
    # ----------------------------------------------------

    context = "\n\n".join(
        doc["text"]
        for doc in retrieved_docs[:2]
    )

    # ----------------------------------------------------
    # Conversation History
    # ----------------------------------------------------

    history_text = ""

    for msg in history:
        history_text += (
            f"{msg['role']}: {msg['content']}\n"
        )

    # ----------------------------------------------------
    # Agent Prompt
    # ----------------------------------------------------

    if agent_type == "emergency":

        system_prompt = """
You are Maatri AI.

You are an emergency maternal healthcare assistant.

Rules:

- Stay calm and reassuring.
- Use ONLY the retrieved medical evidence.
- If the evidence indicates an emergency,
  advise the user to seek immediate medical attention.
- Never exaggerate risk.
- Never invent medical facts.
"""

    elif agent_type == "nutrition":

        system_prompt = """
You are Maatri AI.

You are a maternal nutrition expert.

Rules:

- Use ONLY the retrieved medical evidence.
- Give practical and encouraging advice.
- Never invent information.
"""

    else:

        system_prompt = """
You are Maatri AI.

You are an empathetic maternal healthcare assistant.

Rules:

- Use conversation history for follow-up questions.
- Answer ONLY using the retrieved medical evidence.
- Use relevant evidence even if wording differs.
- Never invent medical advice.
- If evidence is insufficient, clearly state that.
"""

    # ----------------------------------------------------
    # Final Prompt
    # ----------------------------------------------------

    prompt = f"""
{system_prompt}

==============================

Conversation History:

{history_text}

==============================

Medical Evidence:

{context}

==============================

User Question:

{query}

==============================

Answer:
"""

    # ----------------------------------------------------
    # Primary Generator
    # ----------------------------------------------------

    result = generate(prompt)

    generator = "Unknown"

    answer = None

    if result is not None:

        if isinstance(result, dict):

            generator = result.get(
                "provider",
                "Unknown",
            )

            answer = result.get("text")

        elif isinstance(result, str):

            generator = "Unknown"

            answer = result

    # ----------------------------------------------------
    # Local BART Fallback
    # ----------------------------------------------------

    if answer is None:

        try:

            local_answer = summarize(
                question=query,
                evidence=context,
            )

            if local_answer:

                generator = "Local BART Summarizer"

                answer = (
                    "⚠️ Cloud AI was temporarily unavailable.\n\n"
                    "The following answer was generated locally "
                    "using the retrieved medical evidence.\n\n"
                    + local_answer
                )

                print("\nUsing Local BART fallback.\n")

        except Exception as e:

            print("\nBART Error")
            print(e)

            answer = None

    # ----------------------------------------------------
    # Evidence Synthesizer Fallback
    # ----------------------------------------------------

    if answer is None:

        generator = "Evidence Synthesizer"

        answer = (
            "⚠️ Cloud AI was temporarily unavailable.\n\n"
            "Based on the retrieved medical evidence:\n\n"
            + evidence_summary(retrieved_docs)
        )

    # ----------------------------------------------------
    # Return
    # ----------------------------------------------------

    return {
        "answer": answer,
        "disclaimer": MEDICAL_DISCLAIMER,
        "generator": generator,
    }