from abc import ABC
import src.osm_configurator.control.control_interface
import src.osm_configurator.view.states.state_manager


class TopLevelFrame(ABC):
    """
    This Class describes a Frame, that has a fully developed functionality and is a Frame that can be placed on a
    Window, to be shown.
    A TopLevelFrame might have Frames below him, that it can manage.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates there to define how a TopLevelFrame is created.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (control_interface.IControl): The Control the Frame will call, to get access to the Model.
        """
        pass
