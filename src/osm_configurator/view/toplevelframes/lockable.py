from abc import ABC, abstractmethod


class Lockable(ABC):
    """
    Interface used for frames, that shall be abale to be locked or unlocked, to enable and disable the interaction
    with them.
    """

    @abstractmethod
    def lock(self) -> bool:
        """
        This method locks a frame, so it can't be interacted with it anymore.

        Returns:
            bool: True if the frame was successfully locked, false if already locked or couldn't be locked
        """
        pass

    @abstractmethod
    def unlock(self) -> bool:
        """
        This method unlocks a frame, so it can be interacted with it again.

        Returns:
            bool: True if frame was successfully unlocked, false if already unlocked or couldn't be unlocked
        """
        pass
