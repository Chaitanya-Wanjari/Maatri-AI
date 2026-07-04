from backend.routing.language_detector import detect_language
from backend.routing.classifier import classify

from .health_agent import HealthAgent
from .nutrition_agent import NutritionAgent
from .emergency_agent import EmergencyAgent
from .hindi_planner import HindiPlanner


class PlannerAgent:

    def __init__(self):

        self.health = HealthAgent()
        self.nutrition = NutritionAgent()
        self.emergency = EmergencyAgent()

        self.hindi = HindiPlanner()

    def run(
        self,
        query,
        session_id,
    ):

        language = detect_language(query)

        print("\n" + "=" * 55)
        print("PLANNER")
        print("=" * 55)
        print(f"Query    : {query}")
        print(f"Language : {language}")

        # -------------------------
        # Hindi
        # -------------------------

        if language == "hi":

            print("Agent    : Hindi Planner")
            print("Route    : Hindi RAG")
            print("=" * 55)

            return self.hindi.run(
                query,
                session_id,
            )

        # -------------------------
        # English
        # -------------------------

        route = classify(query)

        print(f"Intent   : {route}")

        if route == "nutrition":

            print("Agent    : Nutrition Agent")
            print("=" * 55)

            return self.nutrition.run(
                query,
                session_id,
            )

        if route == "emergency":

            print("Agent    : Emergency Agent")
            print("=" * 55)

            return self.emergency.run(
                query,
                session_id,
            )

        print("Agent    : Health Agent")
        print("=" * 55)

        return self.health.run(
            query,
            session_id,
        )