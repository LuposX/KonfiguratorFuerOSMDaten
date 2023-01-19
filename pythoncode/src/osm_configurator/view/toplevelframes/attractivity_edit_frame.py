import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.category_controller

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class AttractivityEditFrame(TopLevelFrame):
    """
    This frame lets the user edit, create and delete attractivity attributes for the categories.
    Two drop-down menus will be shown: One will select the category, the other the attractivity attributes.
    Editing options for the attractivity attributes will be offered in a textbox to change the name. Smaller boxes
    provide the means of changing the factors for different attributes.
    Two buttons provide creation and deletion tools.
    """

    def __init__(self, state_manager, category_controller):
        """
        This method creates an AttractivityEditFrame, where the attractivity attributes of categories can be edited,
        created or be deleted.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, when it wants to change to another state.
            category_controller (category_controller.CategoryController): Respective controller
        """
        # super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
