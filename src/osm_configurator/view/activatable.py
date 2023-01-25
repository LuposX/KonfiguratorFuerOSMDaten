from abc import ABC, abstractmethod


class Activatable(ABC):

    @classmethod
    def activate(self):
        pass
