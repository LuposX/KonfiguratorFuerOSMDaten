import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.export_controller
import src.osm_configurator.control.project_controller

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

    This frame is always on the top of the window. Below it there will be presented a frame to edit some part of the project
    and below that one there will be a FootFrame.
    Exceptions are the MainMenu and the creation of a new project without this header.
    """

    def __init__(self, state_manager, export_controller, project_controller):
        """
        This method creates a ProjectHeadFrame, letting the user navigate the pipeline and exit back to the main menu.
        The user can also open the settings, save the project or export the project.

        Args:
            state_manager (state_manager.StateManager): The frame will call the StateManager, if it wants to switch states.
            export_controller (export_controller.ExportController): Respective controller
            project_controller (project_controller.ProjectController): Respective controller
        """
        # super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
