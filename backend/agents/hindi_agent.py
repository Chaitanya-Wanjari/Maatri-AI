from backend.hindi_rag.rag_service import answer


class HindiAgent:

    def run(self, query, session_id,):

        return answer(query, session_id,)