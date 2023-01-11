from abc import ABC
import src.osm_configurator.control.control_interface
import src.osm_configurator.view.states.state_manager


class TopLevelFrame(ABC):
    """
    This class describes a frame, that has a fully developed functionality and that can be placed on a window.
    A TopLevelFrame might have manageable frames below him.
    """

    def __init__(self, state_manager, control):
        """
        This method defines how a TopLevelFrame is created.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, if it wants to switch states.
            control (control_interface.IControl): The control the frame will call, to gain access to the model.
        """
        pass
