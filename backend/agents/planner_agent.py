from backend.routing.language_detector import detect_language
from backend.routing.classifier import classify
from backend.routing.risk_assessment import assess_risk

from .health_agent import HealthAgent
from .nutrition_agent import NutritionAgent
from .emergency_agent import EmergencyAgent
from .hindi_planner import HindiPlanner
from .risk_agent import RiskAssessmentAgent


class PlannerAgent:

    def __init__(self):

        self.health = HealthAgent()
        self.nutrition = NutritionAgent()
        self.emergency = EmergencyAgent()
        self.hindi = HindiPlanner()
        self.risk = RiskAssessmentAgent()

    def run(
        self,
        query,
        session_id,
    ):

        # -----------------------------------
        # Language Detection
        # -----------------------------------

        language = detect_language(query)

        # -----------------------------------
        # Risk Assessment
        # -----------------------------------

        risk = self.risk.run(query)

        # -----------------------------------
        # Planner Logs
        # -----------------------------------

        print("\n" + "=" * 55)
        print("PLANNER")
        print("=" * 55)
        print(f"Query      : {query}")
        print(f"Language   : {language}")
        print(f"Risk Agent : {risk['agent']}")

        print(f"Risk Level : {risk['risk']}")

        if risk["reason"]:

            print(f"Reason     : {risk['reason']}")
        # -----------------------------------
        # Hindi Route
        # -----------------------------------

        if language == "hi":

            print("Agent      : Hindi Planner")
            print("Route      : Hindi RAG")
            print("=" * 55)

            result = self.hindi.run(
                query,
                session_id,
            )

            result["metadata"]["risk"] = risk

            return result

        # -----------------------------------
        # English Classification
        # -----------------------------------

        route = classify(query)

        print(f"Intent     : {route}")

        # -----------------------------------
        # High-Risk Escalation
        # -----------------------------------

        if route == "emergency" or risk["risk"] == "high":

            print("Escalation : Emergency Agent")
            print("=" * 55)

            result = self.emergency.run(
                query,
                session_id,
            )

            result["metadata"]["risk"] = risk

            return result

        # -----------------------------------
        # Nutrition
        # -----------------------------------

        if route == "nutrition":

            print("Agent      : Nutrition Agent")
            print("=" * 55)

            result = self.nutrition.run(
                query,
                session_id,
            )

            result["metadata"]["risk"] = risk

            return result

        # -----------------------------------
        # Default Health Agent
        # -----------------------------------

        print("Agent      : Health Agent")
        print("=" * 55)

        result = self.health.run(
            query,
            session_id,
        )

        result["metadata"]["risk"] = risk

        return result