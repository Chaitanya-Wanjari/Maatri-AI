from backend.llm.provider import generate


def rewrite_query(
    query: str,
    history: list,
):
    """
    Rewrite short follow-up questions into standalone questions.
    """

    if not history:
        return query

    history_text = ""

    for msg in history[-6:]:
        history_text += (
            f"{msg['role']}: {msg['content']}\n"
        )

    prompt = f"""
You are a query rewriting assistant.

Rewrite the user's latest question into a complete standalone question.

Rules:

- Preserve the original meaning.
- Use the conversation history.
- Do NOT answer the question.
- Output ONLY the rewritten question.
- If the question is already complete,
return it unchanged.

Conversation:

{history_text}

Latest Question:

{query}
"""

    rewritten = generate(prompt)

    if rewritten is None:
        return query

    return rewritten.strip()