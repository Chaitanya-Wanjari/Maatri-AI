"""
Hindi Generation Service

Uses Gemini to generate grounded answers from retrieved evidence.
Falls back to evidence-only mode if Gemini is unavailable.
"""

from backend.llm.provider import generate
from backend.utils.fallback import evidence_summary

from .config import MEDICAL_DISCLAIMER


def generate_answer(
    query: str,
    retrieved_docs: list,
    history: list,
):
    context = "\n\n".join(
        doc["text"]
        for doc in retrieved_docs
    )

    history_text = ""

    for msg in history:
        role = "उपयोगकर्ता" if msg["role"] == "user" else "सहायक"

        history_text += (
            f"{role}: {msg['content']}\n"
        )

    prompt = f"""
आप मातृ AI हैं।

आप एक सहानुभूतिपूर्ण मातृ स्वास्थ्य सहायक हैं।

यदि उपयोगकर्ता कोई अगला प्रश्न पूछता है
(जैसे "हाँ?", "हर दिन?", "क्यों?", "कितना?")
तो पहले बातचीत के इतिहास को समझें।

केवल नीचे दिए गए साक्ष्यों के आधार पर उत्तर दें।

यदि पर्याप्त जानकारी उपलब्ध नहीं है,
तो स्पष्ट रूप से कहें कि जानकारी उपलब्ध नहीं है।

उत्तर सरल, प्राकृतिक और सुरक्षित हिन्दी में दें.

========================

बातचीत का इतिहास:

{history_text}

========================

साक्ष्य:

{context}

========================

प्रश्न:

{query}
"""

    answer = generate(prompt)

    if answer is None:

        answer = (
            "⚠️ भाषा मॉडल इस समय उपलब्ध नहीं है।\n\n"
            "ज्ञान आधार से प्राप्त जानकारी:\n\n"
            + evidence_summary(retrieved_docs)
        )

    return {
        "answer": answer,
        "disclaimer": MEDICAL_DISCLAIMER,
    }