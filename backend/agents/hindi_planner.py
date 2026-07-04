from backend.hindi_rag.rag_service import answer


class HindiPlanner:

    def run(self, query, session_id,):

        return answer(query, session_id,)