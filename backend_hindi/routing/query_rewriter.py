"""
Hybrid Query Rewriter

Uses the configured LLM when available.

Falls back to a heuristic rewriter if the LLM
is unavailable.
"""



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
    Rewrite short follow-up questions
    using the previous user question.
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
    standalone questions using only
    conversation history.
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

    # Short follow-up questions inherit context
    if (
        len(q.split()) <= 3
        or any(q.startswith(prefix) for prefix in FOLLOWUP_PREFIXES)
    ):
        return f"{last_user} {query}"

    return query