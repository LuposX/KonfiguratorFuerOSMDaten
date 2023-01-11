import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class AttractivityEditFrame(TopLevelFrame):
    """
    This Frame lets the User edit, create and delete Attractivity-Attributes for the Categories.
    Two drop-down menus will be shown: One will select the Category, the other the Attractivity-Attributes.
    Editing options for the Attractivity-Attributes will be offered in a textbox to change the name. Smaller boxes
    provide the means of changing the factors for different attributes.
    Two Buttons provide creation and deletion tools.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates an AttractivityEditFrame, where the Attractivity-Attributes of categories can be edited,
        created or be deleted.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, when it wants to change to another State.
            control (control_interface.IControl): The Control the Frame will call to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
