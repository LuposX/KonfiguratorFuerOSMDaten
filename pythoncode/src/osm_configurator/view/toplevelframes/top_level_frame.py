from abc import ABC
import src.osm_configurator.control.control_interface
import src.osm_configurator.view.states.state_manager


class TopLevelFrame(ABC):
    """
    This Class describes a Frame, that has a fully developed functionality and that can be placed on a Window.
    A TopLevelFrame might have manageable Frames below him.
    """

    def __init__(self, state_manager, control):
        """
        This Method defines how a TopLevelFrame is created.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, if it wants to switch states.
            control (control_interface.IControl): The Control the Frame will call, to gain access to the Model.
        """
        pass
