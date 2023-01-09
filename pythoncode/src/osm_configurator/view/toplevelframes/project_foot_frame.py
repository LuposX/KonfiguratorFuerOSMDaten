from src.osm_configurator.view.states.state_manager import StateManager
from src.osm_configurator.control.control_interface import IControl
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class ProjectFootFrame(TopLevelFrame):
    """
    This Frame shows two arrows on the Bottom of the Window, to let the User navigate the PipeLine, by going
    left or right.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates a ProjectFootFrame, that lets the User navigate throug the PipeLine through two
        arrows, for left and right.

        Args:
            state_manager (StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
