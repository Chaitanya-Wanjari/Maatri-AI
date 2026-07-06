"""
Hindi Generation Service

Uses Gemini as the primary generator.
Falls back to a local BART summarizer.
Falls back to an evidence synthesizer if both fail.
"""

from backend.llm.provider import generate
from backend.llm.bart_summarizer import summarize
from backend.utils.fallback import evidence_summary

from .config import MEDICAL_DISCLAIMER


def generate_answer(
    query: str,
    retrieved_docs: list,
    history: list,
    agent_type: str = "health",
):
    # ----------------------------------------------------
    # Build retrieved context
    # ----------------------------------------------------

    context = "\n\n".join(
        doc["text"]
        for doc in retrieved_docs[:2]
    )

    # ----------------------------------------------------
    # Conversation history
    # ----------------------------------------------------

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

- केवल दिए गए चिकित्सा साक्ष्यों का उपयोग करें।
- यदि साक्ष्य से लगे कि स्थिति गंभीर हो सकती है,
  तो तुरंत चिकित्सीय सहायता लेने की सलाह दें।
- कोई चिकित्सा जानकारी स्वयं न बनाएं।
- शांत, स्पष्ट और सहानुभूतिपूर्ण उत्तर दें।
"""

    elif agent_type == "nutrition":

        system_prompt = """
आप मातृ AI हैं।

आप मातृ पोषण विशेषज्ञ हैं।

नियम:

- केवल दिए गए चिकित्सा साक्ष्यों का उपयोग करें।
- व्यावहारिक और सरल सलाह दें।
- कोई अतिरिक्त जानकारी स्वयं न बनाएं।
"""

    else:

        system_prompt = """
आप मातृ AI हैं।

आप एक सहानुभूतिपूर्ण मातृ स्वास्थ्य सहायक हैं।

नियम:

- बातचीत के इतिहास का उपयोग करें।
- केवल दिए गए चिकित्सा साक्ष्यों के आधार पर उत्तर दें।
- यदि साक्ष्य पर्याप्त रूप से संबंधित हों,
  तो उनका उपयोग करें।
- कोई चिकित्सा जानकारी स्वयं न बनाएं।
- उत्तर सरल, सुरक्षित और स्पष्ट रखें।
"""

    # ----------------------------------------------------
    # Prompt
    # ----------------------------------------------------

    prompt = f"""
{system_prompt}

========================

बातचीत का इतिहास:

{history_text}

========================

चिकित्सा साक्ष्य:

{context}

========================

प्रश्न:

{query}

========================

उत्तर:
"""

    # ----------------------------------------------------
    # Primary Generator (Gemini)
    # ----------------------------------------------------

    result = generate(prompt)

    generator = "Gemini 2.5 Flash"

    if result is not None:

        generator = result.get(
            "provider",
            "Gemini 2.5 Flash",
        )

        answer = result["text"]

    else:

        answer = None

    # ----------------------------------------------------
    # Local BART fallback
    # ----------------------------------------------------

    if answer is None:

        try:

            local_answer = summarize(
                question=query,
                evidence=context,
            )

            if local_answer:

                generator = "Local BART Summarizer"

                answer = (
                    "⚠️ क्लाउड AI इस समय उपलब्ध नहीं है।\n\n"
                    "नीचे दिया गया उत्तर प्राप्त चिकित्सा साक्ष्यों "
                    "का स्थानीय सारांश है।\n\n"
                    + local_answer
                )

                print("\nUsing Local BART fallback.\n")

        except Exception as e:

            print("\nBART Error")
            print(e)

            answer = None

    # ----------------------------------------------------
    # Final Evidence Fallback
    # ----------------------------------------------------

    if answer is None:

        generator = "Evidence Synthesizer"

        answer = (
            "⚠️ क्लाउड AI इस समय उपलब्ध नहीं है।\n\n"
            "प्राप्त चिकित्सा साक्ष्यों के आधार पर:\n\n"
            + evidence_summary(retrieved_docs)
        )

    # ----------------------------------------------------
    # Return
    # ----------------------------------------------------

    return {
        "answer": answer,
        "disclaimer": MEDICAL_DISCLAIMER,
        "generator": generator,
    }