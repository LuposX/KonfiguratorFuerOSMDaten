from __future__ import annotations

import customtkinter

import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.project_controller_interface
from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

import src.osm_configurator.view.states.state_name_enum as sne

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.view.activatable import Activatable
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class CreateProjectFrame(customtkinter.CTkToplevel, Activatable):
    """
    This frame shows the project creation page to the User.
    A name, a description and a path for storing the project can be set here.
    The user can cancel the creation-process.
    """

    # TODO: Change CTk-values to standardized enum-values

    def __init__(self, state_manager: StateManager, project_controller: IProjectController):
        """
        This method creates a CreateProjectFrame where a user can create a new project.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, if it wants to change to another State.
            project_controller (project_controller.ProjectController): Respective controller
        """
        window = super().__init__()  # Creates the window

        self._state_manager = state_manager
        self._project_controller = project_controller

        self._project_description = ""
        self._project_name = ""
        self._project_path = ""

        self.name_field = customtkinter.CTkEntry(master=window, text="Project Name: ", title="ProjectName") \
            .configure(name=self._project_name) \
            .pack(padx=20, pady=20)

        self.description_field = customtkinter.CTkEntry(master=window, text="Description: ", title="Description") \
            .configure(description=self._project_description) \
            .pack(padx=20, pady=20)

        self.destination_button = customtkinter.CTkButton(master=window, name="Choose Destination",
                                                          command=self._choose_destination) \
            .pack(side="left", padx=40, pady=40)

        self.create_button = customtkinter.CTkButton(master=window, name="Create", command=self.__create_pressed) \
            .pack(side="bottom", padx=40, pady=40)

        self.cancel_button = customtkinter.CTkButton(master=window, name="Cancel", command=self.__cancel_pressed,
                                                     bg_color="red") \
            .pack(side="bottom", padx=40, pady=40)

    def activate(self):
        pass

    def _choose_destination(self):
        """
        Opens the explorer making the user choose the wanted destination
        """
        #  TODO: Implement procedure for choosing the project's path
        self._project_path = "Insert Path Here"

    def __create_pressed(self):
        """
        The create-button was pressed, the project is created, the user is redirected to the data-phase-window
        """
        #  TODO: Initialize Project-Creation

        self._project_name = self.name_field.get()

        if self._project_name == "":
            popup = AlertPopUp("No project-name entered. Please try again.")
            popup.mainloop() # Displays the popup
            self.__reload()  # Reloads the page
            return

        self._project_description = self.description_field.get()
        self._state_manager.change_state(sne.StateName.DATA.value)

    def __cancel_pressed(self):
        """
        The cancel button was pressed, the user is redirected to the main menu
        """
        self._state_manager.change_state(sne.StateName.MAIN_MENU.value)

    def __reload(self):
        self._state_manager.change_state(sne.StateName.CREATE_PROJECT.value)
