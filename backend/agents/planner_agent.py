from backend.routing.classifier import classify

from .health_agent import HealthAgent
from .nutrition_agent import NutritionAgent
from .emergency_agent import EmergencyAgent


class PlannerAgent:

    def __init__(self):

        self.health = HealthAgent()
        self.nutrition = NutritionAgent()
        self.emergency = EmergencyAgent()

    def run(self, query):

        route = classify(query)
        print(f"\nPlanner Route: {route}")
        print(f"Question: {query}\n")

        if route == "nutrition":
            return self.nutrition.run(query)

        if route == "emergency":
            return self.emergency.run(query)

        return self.health.run(query)