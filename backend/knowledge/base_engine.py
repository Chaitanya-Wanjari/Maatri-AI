from abc import ABC, abstractmethod


class BaseKnowledgeEngine(ABC):

    @abstractmethod
    def answer(self, question: str):
        pass