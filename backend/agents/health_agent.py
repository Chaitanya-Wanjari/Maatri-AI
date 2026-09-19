from .base_agent import BaseAgent


class HealthAgent(BaseAgent):

    def __init__(self):
        super().__init__("Health Agent")

    def run(self, query, session_id: str):

        # Lazy import
        from backend.english_rag.rag_service import answer

        result = answer(query, session_id)

        result["agent"] = self.name
        result["metadata"]["agent_type"] = "Healthcare"

        return result