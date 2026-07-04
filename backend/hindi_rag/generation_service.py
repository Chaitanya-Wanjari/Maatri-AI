from backend.llm.gemini_client import generate

from .config import MEDICAL_DISCLAIMER


def generate_answer(query, documents):

    context = "\n\n".join(
        doc["text"]
        for doc in documents
    )

    prompt = f"""
आप मातृ AI हैं।

नीचे दिए गए साक्ष्यों के आधार पर उत्तर दें।

यदि जानकारी उपलब्ध नहीं है,
तो स्पष्ट रूप से कहें कि जानकारी उपलब्ध नहीं है।

उत्तर सरल और प्राकृतिक हिन्दी में दें।

साक्ष्य:

{context}

प्रश्न:

{query}
"""

    answer = generate(prompt)

    if answer is None:

        evidence = "\n\n".join(
            f"{i+1}. {doc['text']}"
            for i, doc in enumerate(documents[:3])
        )

        answer = (
            "⚠️ भाषा मॉडल इस समय उपलब्ध नहीं है।\n\n"
            "ज्ञान आधार से प्राप्त जानकारी:\n\n"
            f"{evidence}"
        )

    return {
        "answer": answer,
        "disclaimer": MEDICAL_DISCLAIMER,
    }