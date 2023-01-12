import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class ProjectFootFrame(TopLevelFrame):
    """
    This frame shows two arrows on the bottom of the Window. The user can navigate the pipeline by going left or right.
    """

    def __init__(self, state_manager, control):
        """
        This method creates a ProjectFootFrame, that lets the user navigate the pipeline by going left or right.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, if it wants to switch states.
            control (control_interface.IControl): The control the frame will call to get access to the model.
        """
        super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
