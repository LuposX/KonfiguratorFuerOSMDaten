from __future__ import annotations

import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.project_controller

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class CreateProjectFrame(TopLevelFrame):
    """
    This frame shows the project creation page to the User.
    A name, a description and a path for storing the project can be set here.
    The user can cancel the creation-process.
    """

    def __init__(self, state_manager, project_controller):
        """
        This method creates a CreateProjectFrame where a user can create a new project.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, if it wants to change to another State.
            project_controller (project_controller.ProjectController): Respective controller
        """
        # super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
