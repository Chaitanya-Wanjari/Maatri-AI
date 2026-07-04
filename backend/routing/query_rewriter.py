FOLLOWUPS = {
    "every day",
    "everyday",
    "daily",
    "what about daily",
    "why",
    "how much",
    "is it safe",
    "is this normal",
    "can i",
    "what about",
    "रोज़",
    "रोज",
    "हर दिन",
    "क्यों",
    "कितना",
    "क्या यह सामान्य है",
}


def rewrite_query(query, history):

    q = query.strip().lower()

    if q not in FOLLOWUPS:
        return query

    for msg in reversed(history):

        if msg["role"] == "user":

            return msg["content"] + " " + query

    return query