import pythoncode.src.osm_configurator.view.states.state_manager
import pythoncode.src.osm_configurator.control.control_interface
from pythoncode.src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class MainMenuFrame(TopLevelFrame):
    """
    This Frame shows the Application's Main Menu.
    The User can create a new Project, or load an already existing Project. Projects stored in the default folder
    will be shown in a list and can be selected / opened.
    """

    def __init__(self, state_manager, control):
        """
        This Method creates a MainMenuFrame showing the MainMenu of the Application.

        Args:
            state_manager (state_manager.StateManager): The Frame will call the StateManager, if it wants to switch States.
            control (control_interface.IControl): The Frame will call the Control to gain access to the Model.
        """
        super().__init__(state_manager, control)
        pass
