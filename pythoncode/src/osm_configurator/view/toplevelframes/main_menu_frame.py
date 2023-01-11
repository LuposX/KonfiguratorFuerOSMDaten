import pythoncode.src.osm_configurator.view.states.state_manager
import pythoncode.src.osm_configurator.control.control_interface
from pythoncode.src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class MainMenuFrame(TopLevelFrame):
    """
    This Frame shows the MainMenu of the Application.
    From where the User can create a new Project or load one.
    For Project that are in the default project folder, will be shown in a List to select and open from.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates a MainMenuFrame, which shows the MainMenu of the Application.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (control_interface.IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
