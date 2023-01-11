import pythoncode.src.osm_configurator.view.states.state_manager
import pythoncode.src.osm_configurator.control.control_interface
from pythoncode.src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class ProjectHeadFrame(TopLevelFrame):
    """
    This Frame shows the Header-PipeLine of the Application, if a Project is opened.
    Functionality the User can use:
    - Exit to the MainMenu
    - Save Project
    - Go to Settings
    - Change between different Frames to edit Configurations
    - Use Exports

    This Frame is always on the top of the Window. Below it will be presented a Frame to edit some part of the Project
    and below that Frame will be a FootFrame.
    Exceptions are the MainMenu and the Creation of a new Project without this header.
    """

    def __init__(self, state_manager, control):
        """
        This Method creates a ProjectHeadFrame, letting the User navigate the Pipeline and exit back to the Main Menu.
        The User can also open the Settings, save the Project or export the Project.

        Args:
            state_manager (state_manager.StateManager): The Frame will call the StateManager, if it wants to switch States.
            control (control_interface.IControl): The Frame will call the Control, to gain access to the Model.
        """
        super().__init__(state_manager, control)
        pass
