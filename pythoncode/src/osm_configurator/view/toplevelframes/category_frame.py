from src.osm_configurator.view.states.state_manager import StateManager
from src.osm_configurator.control.control_interface import IControl
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class CategoryFrame(TopLevelFrame):
    """
    This Frame lets the User create Categories, delete them and edit them.
    It shows the name of a Category, as well as their Black- and White-List.
    Categories also can be turned on adn of with Checkboxes.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates an CategoryFrame so the user can create, delete and edit Categories.

        Args:
            state_manager (StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
