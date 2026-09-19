from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Base class for every agent in Maatri AI.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, query: str):
        pass