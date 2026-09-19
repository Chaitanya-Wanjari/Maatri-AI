from functools import lru_cache

from transformers import pipeline

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"


@lru_cache(maxsize=1)
def get_summarizer():

    print("\nLoading BART Summarizer...\n")

    return pipeline(
        "summarization",
        model=MODEL_NAME,
    )


def summarize(
    question: str,
    evidence: str,
):

    summarizer = get_summarizer()

    prompt = f"""
Question:
{question}

Medical Evidence:
{evidence}

Provide a medically safe summary that answers the user's question using ONLY the evidence.
"""

    summary = summarizer(

        prompt,

        max_length=180,

        min_length=50,

        do_sample=False,

    )

    return summary[0]["summary_text"]