import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class CategoryFrame(TopLevelFrame):
    """
    This Frame lets the User create, delete and edit Categories.
    It shows the name of a Category, as well as their Black- and White-List.
    Categories also can be turned on and off with Checkboxes.
    There will also be Key-Recommendations be shown for the Black- and White-List.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates an CategoryFrame so the user can create, delete and edit Categories.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (control_interface.IControl): The Frame will call the Control, to gain access to the Model.
        """
        super().__init__(state_manager, control)
        pass
