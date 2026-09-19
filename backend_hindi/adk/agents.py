from google.adk.agents import Agent

from .tools import (
    english_tool,
    hindi_tool,
)


english_agent = Agent(
    name="EnglishMedicalAgent",
    description=(
        "Answers maternal healthcare questions in English "
        "using the English medical knowledge base."
    ),
    tools=[english_tool],
)

hindi_agent = Agent(
    name="HindiMedicalAgent",
    description=(
        "Answers maternal healthcare questions in Hindi "
        "using the Hindi medical knowledge base."
    ),
    tools=[hindi_tool],
)

root_agent = Agent(
    name="MaatriPlanner",
    description=(
        "Routes maternal healthcare questions to the correct specialist agent."
    ),
    sub_agents=[
        english_agent,
        hindi_agent,
    ],
)