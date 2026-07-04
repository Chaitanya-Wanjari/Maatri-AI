from backend.hindi_rag.rag_service import answer


class HindiAgent:

    def run(self, query):

        return answer(query)