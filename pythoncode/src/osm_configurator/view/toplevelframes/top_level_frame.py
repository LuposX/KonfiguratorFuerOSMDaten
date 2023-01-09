from abc import ABC
from src.osm_configurator.control.control_interface import IControl
from src.osm_configurator.view.states.state_manager import StateManager


class TopLevelFrame(ABC):
    """
    This Class describes a Frame, that has a fully developed functionality and is a Frame that can be placed on a
    Window, to be shown.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates there to define how a TopLevelFrame is created.

        Args:
            state_manager (StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (IControl): The Control the Frame will call, to get access to the Model.
        """
        pass
