from .session_memory import memory
from .models import ConversationTurn


class MemoryService:

    def add(self, session_id, question, answer):

        memory[session_id].append(
            ConversationTurn(
                question=question,
                answer=answer,
            )
        )

    def history(self, session_id):

        return memory.get(session_id, [])

    def clear(self, session_id):

        memory.pop(session_id, None)