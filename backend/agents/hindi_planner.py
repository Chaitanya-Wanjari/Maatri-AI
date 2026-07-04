from backend.hindi_rag.rag_service import answer

from .base_agent import BaseAgent


class HindiPlanner(BaseAgent):

    def __init__(self):
        super().__init__("Hindi Planner")

    def run(
        self,
        query,
        session_id: str,
    ):
        result = answer(
            query,
            session_id,
        )

        result["agent"] = self.name

        result["metadata"]["agent_type"] = "Hindi Healthcare"

        return result