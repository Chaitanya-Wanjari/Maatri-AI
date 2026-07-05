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
    agent_type: str = "health",
):
    context = "\n\n".join(
        doc["text"]
        for doc in retrieved_docs
    )

    history_text = ""

    for msg in history:

        role = (
            "उपयोगकर्ता"
            if msg["role"] == "user"
            else "सहायक"
        )

        history_text += (
            f"{role}: {msg['content']}\n"
        )

    # ----------------------------------------------------
    # Agent-specific prompt
    # ----------------------------------------------------

    if agent_type == "emergency":

        system_prompt = """
आप मातृ AI हैं।

आप मातृ स्वास्थ्य आपातकालीन सहायक हैं।

नियम:

- केवल दिए गए साक्ष्यों का उपयोग करें।
- यदि साक्ष्य से लगे कि स्थिति गंभीर हो सकती है,
  तो तुरंत चिकित्सीय सहायता लेने की सलाह दें।
- शब्दशः समान प्रश्न की आवश्यकता नहीं है।
- केवल तभी कहें कि जानकारी उपलब्ध नहीं है
  जब कोई भी साक्ष्य उपयोगी न हो।
- कोई चिकित्सा जानकारी स्वयं न बनाएं।
"""

    elif agent_type == "nutrition":

        system_prompt = """
आप मातृ AI हैं।

आप मातृ पोषण विशेषज्ञ हैं।

नियम:

- केवल दिए गए साक्ष्यों का उपयोग करें।
- यदि भोजन सामान्यतः सुरक्षित है,
  तो स्वाभाविक रूप से उत्तर दें।
- केवल तभी कहें कि जानकारी उपलब्ध नहीं है
  जब कोई उपयुक्त साक्ष्य न हो।
"""

    else:

        system_prompt = """
आप मातृ AI हैं।

आप एक सहानुभूतिपूर्ण मातृ स्वास्थ्य सहायक हैं।

नियम:

- बातचीत के इतिहास का उपयोग करें।
- केवल दिए गए साक्ष्यों के आधार पर उत्तर दें।
- यदि साक्ष्य प्रश्न से पर्याप्त रूप से संबंधित हों,
  तो उनका उपयोग करें।
- केवल तभी कहें कि जानकारी उपलब्ध नहीं है
  जब कोई भी साक्ष्य उपयोगी न हो।
- कोई चिकित्सा जानकारी स्वयं न बनाएं।
"""

    prompt = f"""
{system_prompt}

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
            "⚠️ भाषा मॉडल इस समय उपलब्ध नहीं है।\\n\\n"
            "ज्ञान आधार से प्राप्त जानकारी:\\n\\n"
            + evidence_summary(retrieved_docs)
        )

    return {
        "answer": answer,
        "disclaimer": MEDICAL_DISCLAIMER,
    }