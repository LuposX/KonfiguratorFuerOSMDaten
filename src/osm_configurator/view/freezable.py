from abc import ABC, abstractmethod


class Freezable(ABC):
    @abstractmethod
    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        pass

    @abstractmethod
    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        pass
