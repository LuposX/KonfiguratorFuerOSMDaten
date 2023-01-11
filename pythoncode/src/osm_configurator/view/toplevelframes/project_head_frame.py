import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class ProjectHeadFrame(TopLevelFrame):
    """
    This frame shows the header pipeLine of the application, if a project is opened.
    Functionality the user can use:
    - Exit to the main menu
    - Save the project
    - Go to the settings
    - Change between different frames to edit configurations
    - Use exports

    This frame is always on the top of the window. below it will be presented a frame to edit some part of the project
    and below that Frame will be a FootFrame.
    Exceptions are the MainMenu and the creation of a new project without this header.
    """

    def __init__(self, state_manager, control):
        """
        This method creates a ProjectHeadFrame, letting the user navigate the pipeline and exit back to the main menu.
        The user can also open the settings, save the project or export the project.

        Args:
            state_manager (state_manager.StateManager): The frame will call the StateManager, if it wants to switch states.
            control (control_interface.IControl): The frame will call the control, to gain access to the model.
        """
        super().__init__(state_manager, control)
        pass
