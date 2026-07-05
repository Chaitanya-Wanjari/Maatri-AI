"""
Hybrid Query Rewriter

Uses Gemini when available.

Falls back to a heuristic rewriter when Gemini
is unavailable or quota is exhausted.
"""

from backend.llm.provider import generate


FOLLOWUP_PREFIXES = [
    "yes",
    "no",
    "why",
    "how",
    "what",
    "when",
    "where",
    "which",
    "who",
    "everyday",
    "every day",
    "daily",
    "should i",
    "can i",
    "is it",
    "are they",
    "how much",
    "how often",
    "how long",
    "really",
]


def heuristic_rewrite(
    query: str,
    history: list,
):
    """
    Rewrite short follow-up questions using
    the previous user question.
    """

    if not history:
        return query

    last_user = None

    for msg in reversed(history):

        if msg["role"] == "user":

            last_user = msg["content"]

            break

    if last_user is None:
        return query

    q = query.strip().lower()

    if (
        len(q.split()) <= 3
        or any(
            q.startswith(prefix)
            for prefix in FOLLOWUP_PREFIXES
        )
    ):

        return f"{last_user} {query}"

    return query


def rewrite_query(
    query: str,
    history: list,
):
    """
    Rewrite follow-up questions into
    standalone questions.
    """

    if not history:
        return query

    history_text = ""

    for msg in history[-6:]:

        history_text += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    prompt = f"""
You rewrite conversational questions.

Rules:

- Rewrite ONLY the latest user question.
- Preserve meaning.
- Use conversation history.
- Do NOT answer.
- Output ONLY the rewritten question.
- If already standalone,
return it unchanged.

Conversation:

{history_text}

Latest Question:

{query}
"""

    rewritten = generate(prompt)

    # ------------------------------
    # Gemini unavailable
    # ------------------------------

    if rewritten is None:

        return heuristic_rewrite(
            query,
            history,
        )

    rewritten = rewritten.strip()

    if not rewritten:

        return heuristic_rewrite(
            query,
            history,
        )

    return rewritten