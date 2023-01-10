import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class AttractivityEditFrame(TopLevelFrame):
    """
    This Frame lets the User edit, create and delete Attractivity-Attributes for the Categories.
    There will be 2 drop sown menus be shown, one to select a Category and one to select its Attractivity-Attributes.
    Editing options for the Attractivity-Attributes will be a textbox to change the name as well as smaller
    textboxes to change the factors for different attributes.
    For creation and deletion, there will be 2 Buttons.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates an AttractivityEditFrame, where the Attractivity-Attributes of categories can be edited,
        created or be deleted.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (control_interface.IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
