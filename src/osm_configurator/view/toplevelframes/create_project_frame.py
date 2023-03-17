from __future__ import annotations

import os
import tkinter

from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

# Constants
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.states.state_name_enum as view_states_i
import src.osm_configurator.view.constants.label_constants as label_constants_i
import src.osm_configurator.view.constants.entry_constants as entry_constants_i
import src.osm_configurator.view.constants.text_box_constants as text_box_constants_i

from src.osm_configurator.model.parser.custom_exceptions.not_valid_name_Exception import NotValidName

import src.osm_configurator.view.popups.alert_pop_up as alert_pop_up_i

# Other
from typing import TYPE_CHECKING, Final
import customtkinter
from pathlib import Path
from tkinter import filedialog

if TYPE_CHECKING:
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.settings_controller_interface import ISettingsController
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

# Finals
ELEMENT_BORDER_DISTANCE: Final = 42
PROJECT_NAME_ENTRY_WIDTH: Final = frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value / 2 \
                                  - ELEMENT_BORDER_DISTANCE
PROJECT_DESCRIPTION_WIDTH: Final = PROJECT_NAME_ENTRY_WIDTH

PADY: Final = 4
PADX: Final = 4


class CreateProjectFrame(TopLevelFrame):
    """
    This frame shows the project creation page to the User.
    A name, a description and a path for storing the project can be set here.
    The user can cancel the creation-process.
    """

    def __init__(self, state_manager: StateManager, project_controller: IProjectController,
                 settings_controller: ISettingsController):
        """
        This method creates a CreateProjectFrame where a user can create a new project.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, if it wants to
                change to another State.
            project_controller (project_controller.ProjectController): Respective controller
        """

        # Creating the window
        super().__init__(master=None,
                         width=frame_constants_i.FrameConstants.HEAD_FRAME_WIDTH.value,
                         height=frame_constants_i.FrameConstants.HEAD_FRAME_HEIGHT.value,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.FULL_FRAME_FG_COLOR.value
                         )

        self._state_manager = state_manager
        self._project_controller = project_controller
        self._settings_controller = settings_controller

        self._project_description: str = ""
        self._project_name: str = ""
        self._project_path: Path = self._settings_controller.get_project_default_folder()

        self._frozen: bool = False  # indicates whether the window is frozen or not

        self._buttons: list[customtkinter.CTkButton] = []  # holds all buttons to make uniform styling easier
        self._entries: list[customtkinter.CTkEntry] = []  # holds all entries to make uniform styling easier

        # Configuring the rows and columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=2)

        self._title_label: customtkinter.CTkLabel = \
            customtkinter.CTkLabel(master=self,
                                   width=frame_constants_i.FrameConstants.FULL_FRAME_WIDTH.value,
                                   height=frame_constants_i.FrameConstants.FULL_FRAME_HEIGHT.value * (1 / 5),
                                   corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                   fg_color=label_constants_i.LabelConstants.LABEL_TITLE_FG_COLOR.value,
                                   text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                   anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
                                   text="Create a new Project")
        self._title_label.grid(row=0, column=0, rowspan=1, columnspan=5, sticky="NSEW",
                               pady=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_Y.value,
                               padx=label_constants_i.LabelConstants.LABEL_CONSTANTS_PAD_X.value)

        self.name_field = \
            customtkinter.CTkEntry(master=self,
                                   placeholder_text="Project Name",
                                   corner_radius=entry_constants_i.EntryConstants.ENTRY_CORNER_RADIUS.value,
                                   fg_color=entry_constants_i.EntryConstants.ENTRY_FG_COLOR.value,
                                   text_color=entry_constants_i.EntryConstants.ENTRY_TEXT_COLOR.value,
                                   height=entry_constants_i.EntryConstants.ENTRY_BASE_HEIGHT_BIG.value,
                                   width=int(PROJECT_NAME_ENTRY_WIDTH))
        self.name_field.grid(row=1, column=0, rowspan=1, columnspan=1)
        self._entries.append(self.name_field)

        self.description_field = customtkinter.CTkTextbox(
            master=self,
            width=int(PROJECT_DESCRIPTION_WIDTH),
            height=frame_constants_i.FrameConstants.FULL_FRAME_HEIGHT.value * (2/7) - ELEMENT_BORDER_DISTANCE,
            corner_radius=text_box_constants_i.TextBoxConstants.TEXT_BOX_CORNER_RADIUS.value,
            border_width=text_box_constants_i.TextBoxConstants.TEXT_BOX_BORDER_WITH.value,
            fg_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_FG_COLOR.value,
            border_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_BORDER_COLOR.value,
            text_color=text_box_constants_i.TextBoxConstants.TEXT_BOX_TEXT_COLOR.value,
            wrap='word')

        self.description_field.grid(row=2, column=0, rowspan=1, columnspan=1)

        self.destination_button = \
            customtkinter.CTkButton(master=self,
                                    text="Choose Destination",
                                    command=self._choose_destination,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                    width=button_constants_i.ButtonConstants.BUTTON_BASE_WIDTH_BIG.value,
                                    height=button_constants_i.ButtonConstants.BUTTON_BASE_HEIGHT_BIG.value
                                    )
        self.destination_button.grid(row=3, column=0, rowspan=1, columnspan=1)
        self._buttons.append(self.destination_button)

        self.create_button = \
            customtkinter.CTkButton(master=self,
                                    text="Create",
                                    command=self.__create_pressed,
                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                    width=button_constants_i.ButtonConstants.BUTTON_BASE_WIDTH_BIG.value,
                                    height=button_constants_i.ButtonConstants.BUTTON_BASE_HEIGHT_BIG.value
                                    )
        self.create_button.grid(row=3, column=3, rowspan=1, columnspan=1, padx=PADX)
        self._buttons.append(self.create_button)

        self.cancel_button = \
            customtkinter.CTkButton(master=self,
                                    text="Cancel",
                                    command=self.__cancel_pressed,
                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_RED.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                    width=button_constants_i.ButtonConstants.BUTTON_BASE_WIDTH_BIG.value,
                                    height=button_constants_i.ButtonConstants.BUTTON_BASE_HEIGHT_BIG.value
                                    )
        self.cancel_button.grid(row=3, column=4, rowspan=1, columnspan=1, padx=PADX)
        self._buttons.append(self.cancel_button)

    def activate(self):
        self._project_description: str = ""
        self._project_name: str = ""
        self._project_path: Path = self._settings_controller.get_project_default_folder()

        self.name_field.delete(0, tkinter.END)
        self.description_field.delete(1.0, "end-1c")

    def _choose_destination(self):
        """
        Opens the explorer making the user choose the wanted destination
        """
        path_str = self.__browse_files()

        if path_str == "":
            return  # Don't change the destination when file dialog was canceled

        new_path = Path(path_str)

        if not new_path.exists():
            # No valid Path chosen
            popup = AlertPopUp("No valid Path chosen! Please enter a valid Path.")
            popup.mainloop()
            self.activate()
            return

        # valid Path was chosen => project will be loaded
        self._project_path = new_path
        self._project_controller.load_project(new_path)

    def __create_pressed(self):
        """
        The create-button was pressed, the project is created, the user is redirected to the data-phase-window
        """
        self._project_name = self.name_field.get()

        if self._project_name == "":
            # No projectname entered
            popup = AlertPopUp("No Projectname entered. Please enter a valid Projectname.")
            popup.mainloop()  # Displays the popup
            self.__reload()  # Reloads the page
            return

        if not os.path.exists(self._project_path):
            # No valid path chosen
            popup = AlertPopUp("No valid Path entered. Please choose a valid Path.")
            popup.mainloop()
            self.__reload()
            return

        self._project_description = self.description_field.get(1.0, "end-1c")

        try:
            self._project_controller.create_project(
                name=self._project_name,
                destination=self._project_path,
                description=self._project_description,
            )
        except NotValidName as err:
            popup = alert_pop_up_i.AlertPopUp(str(err.args))
            popup.mainloop()
            self.activate()
            return

        self._state_manager.change_state(view_states_i.StateName.DATA)

    def __cancel_pressed(self):
        """
        The cancel button was pressed, the user is redirected to the main menu
        """
        self._state_manager.change_state(view_states_i.StateName.MAIN_MENU)

    def __reload(self):
        self._state_manager.change_state(view_states_i.StateName.CREATE_PROJECT)

    def __browse_files(self) -> str:
        """
        Opens the explorer starting from the default-folder making the user browse for the searched path
        Return:
            str: Name of the chosen path
        """
        # opens the file explorer in the project default folder
        new_path = filedialog.askdirectory(title="Select a project to load",
                                           initialdir=self._project_path)

        return new_path

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        for button in self._buttons:
            button.configure(state=tkinter.DISABLED)

        for entry in self._entries:
            entry.configure(state=tkinter.DISABLED)

        self._frozen = True

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        for button in self._buttons:
            button.configure(state=tkinter.NORMAL)

        for entry in self._entries:
            entry.configure(state=tkinter.NORMAL)

        self._frozen = False
