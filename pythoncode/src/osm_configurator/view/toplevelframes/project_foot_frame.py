import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.project_controller

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class ProjectFootFrame(TopLevelFrame):
    """
    This frame shows two arrows on the bottom of the Window. The user can navigate the pipeline by going left or right.
    """

    def __init__(self, state_manager, project_controller):
        """
        This method creates a ProjectFootFrame that lets the user navigate the pipeline by going left or right.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, if it wants to switch states.
            project_controller (project_controller.ProjectController): Respective controller
        """
        super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
