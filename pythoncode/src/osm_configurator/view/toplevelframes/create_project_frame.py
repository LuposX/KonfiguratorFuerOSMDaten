import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class CreateProjectFrame(TopLevelFrame):
    """
    This Frame shows the user how to create a new Project.
    As well as providing the feature to create the Project the user has defined.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates an CreateProjectFrame where a User can create a new Project.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (control_interface.IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
