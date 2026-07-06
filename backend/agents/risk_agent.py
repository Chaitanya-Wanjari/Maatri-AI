from backend.routing.risk_assessment import assess_risk

from .base_agent import BaseAgent


class RiskAssessmentAgent(BaseAgent):

    def __init__(self):

        super().__init__("Risk Assessment Agent")

    def run(
        self,
        query: str,
    ):

        result = assess_risk(query)

        result["agent"] = self.name

        return result