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

    def run(self, query):

        language = detect_language(query)

        print(f"\nLanguage: {language}")

        # Hindi queries
        if language == "hi":

            print("Routing → Hindi RAG")

            return self.hindi.run(query)

        # English queries
        route = classify(query)

        print(f"Planner Route: {route}")

        if route == "nutrition":
            return self.nutrition.run(query)

        if route == "emergency":
            return self.emergency.run(query)

        return self.health.run(query)