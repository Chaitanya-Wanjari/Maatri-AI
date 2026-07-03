from backend.llm.gemini_client import generate

from .config import MEDICAL_DISCLAIMER


def generate_answer(query, documents):

    context = "\n\n".join(
        doc["text"]
        for doc in documents
    )

    prompt = f"""
आप मातृ AI हैं।

केवल नीचे दिए गए साक्ष्यों के आधार पर उत्तर दें।

यदि पर्याप्त जानकारी उपलब्ध नहीं है,
तो स्पष्ट रूप से कहें कि जानकारी उपलब्ध नहीं है।

साक्ष्य:

{context}

प्रश्न:

{query}
"""

    answer = generate(prompt)

    if answer is None:

        answer = (
            "माफ़ कीजिए, भाषा मॉडल इस समय उपलब्ध नहीं है।\n\n"
            "कृपया नीचे दिए गए संदर्भ देखें।"
        )

    return {
        "answer": answer,
        "disclaimer": MEDICAL_DISCLAIMER,
    }