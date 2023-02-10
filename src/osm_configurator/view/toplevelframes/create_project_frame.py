from __future__ import annotations

import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.project_controller_interface
from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
import src.osm_configurator.view.states.state_name_enum as sne

# Constants
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i

# Other
from typing import TYPE_CHECKING
import customtkinter
from pathlib import Path
from tkinter import filedialog

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

    def __init__(self, state_manager: StateManager, project_controller: IProjectController):
        """
        This method creates a CreateProjectFrame where a user can create a new project.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, if it wants to change to another State.
            project_controller (project_controller.ProjectController): Respective controller
        """

        # Creating the window
        window = super().__init__(master=None,
                                  width=frame_constants_i.FrameConstants.HEAD_FRAME_WIDTH.value,
                                  height=frame_constants_i.FrameConstants.HEAD_FRAME_HEIGHT.value,
                                  corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                                  fg_color=frame_constants_i.FrameConstants.HEAD_FRAME_FG_COLOR.value)

        self._state_manager = state_manager
        self._project_controller = project_controller

        self._project_description: str
        self._project_name: str
        self._project_path: Path

        # Configuring the rows and columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.name_field = \
            customtkinter.CTkEntry(master=self,
                                   text="Project Name: ",
                                   title="ProjectName",
                                   name=self._project_name) \
            .grid(row=0, column=0, rowspan=1, columnspan=1)

        self.description_field = \
            customtkinter.CTkEntry(master=self,
                                   text="Description: ",
                                   title="Description",
                                   description=self._project_description) \
            .grid(row=1, column=0, rowspan=1, columnspan=1)

        self.destination_button = \
            customtkinter.CTkButton(master=self,
                                    name="Choose Destination",
                                    command=self._choose_destination,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value
                                    ) \
            .grid(row=2, column=0, rowspan=1, columnspan=1)

        self.create_button = \
            customtkinter.CTkButton(master=self,
                                    name="Create",
                                    command=self.__create_pressed,
                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value) \
            .grid(row=3, column=3, rowspan=1, columnpan=1)

        self.cancel_button = \
            customtkinter.CTkButton(master=self,
                                    name="Cancel",
                                    command=self.__cancel_pressed,
                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_RED.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value) \
            .grid(row=3, column=4, rowspan=1, columnspan=1)

    def activate(self):
        pass

    def _choose_destination(self) -> bool:
        """
        Opens the explorer making the user choose the wanted destination
        Returns:
            bool: True, if a valid path was chosen and project-loading process was given to the controller, else false
        """
        new_path = Path(self.__browse_files())

        if not new_path.exists():
            # No valid Path chosen
            popup = AlertPopUp("No valid Path chosen! Please enter a valid Path.")
            popup.mainloop()
            self.activate()
            return False

        # valid Path was chosen => project will be loaded
        self._project_path = new_path
        self._project_controller.load_project(new_path)
        return True

    def __create_pressed(self) -> bool:
        """
        The create-button was pressed, the project is created, the user is redirected to the data-phase-window
        Returns:
            bool: True, if project has all valid attributes and creation was given to the controller, false else
        """
        self._project_name = self.name_field.get()

        if self._project_name == "":
            # No projectname entered
            popup = AlertPopUp("No Projectname entered. Please enter a valid Projectname.")
            popup.mainloop()  # Displays the popup
            self.__reload()  # Reloads the page
            return False

        if not self._project_path.exists():
            # No valid path chosen
            popup = AlertPopUp("No valid Path entered. Please choose a valid Path.")
            popup.mainloop()
            self.__reload()
            return False

        self._project_description = self.description_field.get()
        self._state_manager.change_state(sne.StateName.DATA.value)

        self._project_controller.create_project(
            name=self._project_name,
            destination=self._project_path
        )

        return True

    def __cancel_pressed(self):
        """
        The cancel button was pressed, the user is redirected to the main menu
        """
        self._state_manager.change_state(sne.StateName.MAIN_MENU.value)

    def __reload(self):
        self._state_manager.change_state(sne.StateName.CREATE_PROJECT.value)

    def __browse_files(self) -> str:
        """
        Opens the explorer starting from the default-folder making the user browse for the searched path
        Return:
            str: Name of the chosen path
        """
        new_path = filedialog.askopenfilename(title="Select a project to load",
                                              filetypes=".geojson")  # opens the file explorer in the current dir
        return new_path
