from pathlib import Path

PROMPT_PATH = (
    Path(__file__).parent.parent
    / "prompts"
    / "planner_prompt.txt"
)

NUTRITION_KEYWORDS = [
    "eat", "food", "diet", "nutrition", "fruit", "vegetable",
    "banana", "papaya", "milk", "egg", "water", "iron",
    "खाना", "भोजन", "आहार", "दूध", "फल", "सब्ज़ी", "आयरन",
]

EMERGENCY_KEYWORDS = [
    "bleeding", "blood", "severe pain", "baby stopped moving",
    "emergency", "accident", "रक्तस्राव", "खून",
    "बच्चा हिल नहीं रहा", "तेज़ दर्द",
]


def classify(question: str):
    q = question.lower()

    if any(k in q for k in EMERGENCY_KEYWORDS):
        return "emergency"

    if any(k in q for k in NUTRITION_KEYWORDS):
        return "nutrition"

    return "health"