from .health_agent import HealthAgent


class EmergencyAgent(HealthAgent):

    def __init__(self):

        super().__init__()

        self.name = "Emergency Agent"