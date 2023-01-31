from __future__ import annotations

from src.osm_configurator.model.application.passive_project import PassiveProject
from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
from src.osm_configurator.view.states.state_manager import StateManager

import src.osm_configurator.view.states.state_name_enum as sne

import customtkinter


class MainMenuFrame(Activatable, customtkinter.CTkToplevel):
    """
    This frame shows the application's main menu.
    The user can create a new project, or load an already existing project. Projects stored in the default folder
    will be shown in a list and can be selected / opened.
    """

    def __init__(self, _state_manager: state_manager.StateManager, project_controller, control):
        """
        This method creates a MainMenuFrame showing the MainMenu of the application.

        Args:
            _state_manager (state_manager.StateManager): The frame will call the StateManager, if it wants to switch states.
            project_controller (project_controller.ProjectController): Respective controller
        """
        window = super().__init__(state_manager, control)

        customtkinter.CTkButton(self, text="New Project", command=self.__create_project) \
            .pack(side="left", padx=40, pady=40)

        customtkinter.CTkButton(self, text="Load external Project") \
            .pack(side="left", padx=40, pady=40)

        customtkinter.CTkButton(self, text="Load selected Project") \
            .pack(side="left", padx=40, pady=40)

        customtkinter.CTkButton(self, text="Settings", command=self.__call_settings()) \
            .pack(side="left", padx=40, pady=40)

        # showing all entries in custom boxes
        for passive_project in self._passive_projects:
            name = passive_project.get_name()  # name of the shown project
            description = passive_project.get_description()  # description of the shown project
            customtkinter.CTkButton(master=window, name=name, description=description,
                                    command=self.__load_project(passive_project)) \
                .pack(side="right", padx=20, pady=10)  # creates and places the button

    def activate(self):
        pass
