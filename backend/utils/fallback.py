def evidence_summary(documents):

    answer = []

    for i, doc in enumerate(documents[:3], start=1):

        answer.append(
            f"{i}. {doc['text']}"
        )

    return "\n\n".join(answer)