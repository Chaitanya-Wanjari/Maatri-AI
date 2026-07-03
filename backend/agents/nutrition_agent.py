from .health_agent import HealthAgent


class NutritionAgent(HealthAgent):

    def __init__(self):

        super().__init__()

        self.name = "Nutrition Agent"