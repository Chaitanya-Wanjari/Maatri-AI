from pathlib import Path

from backend.llm.provider import generate


PROMPT_PATH = (
    Path(__file__).parent.parent
    / "prompts"
    / "planner_prompt.txt"
)


def classify(question: str):

    prompt = PROMPT_PATH.read_text(
        encoding="utf-8"
    )

    prompt = prompt.replace(
        "{{QUESTION}}",
        question,
    )

    result = generate(prompt)

    # -----------------------------
    # LLM unavailable
    # -----------------------------

    if result is None:

        q = question.lower()

        if any(word in q for word in [
            "eat",
            "food",
            "diet",
            "nutrition",
            "fruit",
            "vegetable",
            "orange",
            "banana",
            "milk",
            "egg",
        ]):
            return "nutrition"

        if any(word in q for word in [
            "bleeding",
            "blood",
            "emergency",
            "pain",
            "severe",
            "accident",
        ]):
            return "emergency"

        return "health"

    # -----------------------------
    # Provider now returns dict
    # -----------------------------

    if isinstance(result, dict):

        label = result.get(
            "text",
            ""
        ).strip().lower()

    else:

        label = str(result).strip().lower()

    allowed = {
        "health",
        "nutrition",
        "emergency",
        "general",
    }

    if label not in allowed:
        return "health"

    return label