from __future__ import annotations

import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.project_controller_interface

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class MainMenuFrame(TopLevelFrame):
    """
    This frame shows the application's main menu.
    The user can create a new project, or load an already existing project. Projects stored in the default folder
    will be shown in a list and can be selected / opened.
    """

    def __init__(self, state_manager, project_controller):
        """
        This method creates a MainMenuFrame showing the MainMenu of the application.

        Args:
            state_manager (state_manager.StateManager): The frame will call the StateManager, if it wants to switch states.
            project_controller (project_controller.ProjectController): Respective controller
            control (control_interface.IControl): The frame will call the control to gain access to the model.
        """
        # super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
