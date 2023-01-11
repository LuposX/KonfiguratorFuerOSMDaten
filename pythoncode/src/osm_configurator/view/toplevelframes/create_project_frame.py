import pythoncode.src.osm_configurator.view.states.state_manager
import pythoncode.src.osm_configurator.control.control_interface
from pythoncode.src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class CreateProjectFrame(TopLevelFrame):
    """
    This Frame shows the Project creation page to the User.
    A name, a description and a path for storing the project can be set here.
    The user can cancel the creation-process.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates a CreateProjectFrame where a User can create a new Project.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, if it wants to change to
            another State.
            control (control_interface.IControl): The Frame will call the Control, to gain access to the Model.
        """
        super().__init__(state_manager, control)
        pass
