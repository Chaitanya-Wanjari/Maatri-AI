from dataclasses import dataclass


@dataclass
class ConversationTurn:
    question: str
    answer: str