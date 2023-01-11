import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class CategoryFrame(TopLevelFrame):
    """
    This frame lets the user create, delete and edit categories.
    It shows the name of a category, as well as their black- and white-List.
    Categories also can be turned on and off with Checkboxes.
    There will also be key-recommendations be shown for the black- and white-List.
    """

    def __init__(self, state_manager, control):
        """
        This method creates an CategoryFrame so the user can create, delete and edit categories.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, when it wants to change to another state.
            control (control_interface.IControl): The control the frame will call to get access to the model.
        """
        super().__init__(state_manager, control)
        pass
