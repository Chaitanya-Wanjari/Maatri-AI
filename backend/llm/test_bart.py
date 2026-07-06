from backend.llm.bart_summarizer import summarize

question = "Is fever dangerous during pregnancy?"

evidence = """
Fever during pregnancy may indicate an infection.
Persistent fever should not be ignored.
Pregnant women should consult a healthcare provider
if fever persists or is accompanied by chills,
abdominal pain or vaginal bleeding.
"""

print(
    summarize(
        question,
        evidence,
    )
)