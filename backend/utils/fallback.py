def evidence_summary(documents):

    if not documents:
        return (
            "No relevant medical evidence was retrieved."
        )

    seen = set()

    bullets = []

    for doc in documents:

        text = doc["text"].strip()

        if text.lower() in seen:
            continue

        seen.add(text.lower())

        bullets.append(f"• {text}")

        if len(bullets) == 3:
            break

    return "\n\n".join(bullets)