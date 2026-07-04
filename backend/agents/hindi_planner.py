from backend.hindi_rag.rag_service import answer


class HindiPlanner:

    def run(self, query):

        return answer(query)