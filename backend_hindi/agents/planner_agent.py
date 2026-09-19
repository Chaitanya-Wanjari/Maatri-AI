from .hindi_planner import HindiPlanner


class PlannerAgent:

    def __init__(self):
        self.hindi = HindiPlanner()

    def run(self, query, session_id):
        return self.hindi.run(query, session_id)