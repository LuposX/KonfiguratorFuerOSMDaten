from __future__ import annotations

import os
import tkinter
from functools import partial

from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
import src.osm_configurator.view.states.state_name_enum as sne

# Constants
import src.osm_configurator.view.constants.label_constants as label_constants_i
import src.osm_configurator.view.constants.main_window_constants as main_window_constants_i
import src.osm_configurator.model.project.config_phase_enum as config_phase_enum_i

import src.osm_configurator.view.utility_methods as utility_methods_i

import src.osm_configurator.view.states.state_name_enum as state_name_enum_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.scrollbar_constants as scrollbar_constants_i

from src.osm_configurator.model.parser.custom_exceptions.not_valid_name_Exception import NotValidName

# Other
import customtkinter
from tkinter import filedialog
from pathlib import Path

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.settings_controller_interface import ISettingsController
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.model.application.passive_project import PassiveProject

# Finals
ELEMENT_BORDER_DISTANCE: Final = 124

BUTTON_DESCRIPTION_LINE_LENGTH: Final = 42
BUTTON_DESCRIPTION_ROWS: Final = 3
BUTTON_DESCRIPTION_DOTS: Final = True


def find_matching_state(config_step: config_phase_enum_i.ConfigPhase) -> state_name_enum_i.StateName:
    match config_step:
        case config_phase_enum_i.ConfigPhase.DATA_CONFIG_PHASE:
            return state_name_enum_i.StateName.DATA
        case config_phase_enum_i.ConfigPhase.CATEGORY_CONFIG_PHASE:
            return state_name_enum_i.StateName.CATEGORY
        case config_phase_enum_i.ConfigPhase.REDUCTION_CONFIG_PHASE:
            return state_name_enum_i.StateName.REDUCTION
        case config_phase_enum_i.ConfigPhase.ATTRACTIVITY_CONFIG_PHASE:
            return state_name_enum_i.StateName.ATTRACTIVITY_EDIT
        case config_phase_enum_i.ConfigPhase.AGGREGATION_CONFIG_PHASE:
            return state_name_enum_i.StateName.AGGREGATION
        case config_phase_enum_i.ConfigPhase.CALCULATION_CONFIG_PHASE:
            return state_name_enum_i.StateName.CALCULATION

class MainMenuFrame(TopLevelFrame):
    """
    This frame shows the application's main menu.
    The user can create a new project, or load an already existing project. Projects stored in the default folder
    will be shown in a list and can be selected / opened.
    """

    def __init__(self, state_manager: StateManager, project_controller: IProjectController,
                 settings_controller: ISettingsController):
        """
        This method creates a MainMenuFrame showing the MainMenu of the application.

        Args:
            state_manager (state_manager.StateManager): Frame will call the StateManager, if it wants to switch states
            project_controller (project_controller.ProjectController): Respective controller
        """

        super().__init__(master=None,
                         width=frame_constants_i.FrameConstants.FULL_FRAME_WIDTH.value,
                         height=frame_constants_i.FrameConstants.FULL_FRAME_HEIGHT.value,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.FULL_FRAME_FG_COLOR.value)

        self._project_controller = project_controller
        self._settings_controller = settings_controller
        self._state_manager = state_manager
        self._passive_projects: list[PassiveProject] = self._project_controller.get_list_of_passive_projects()

        self.main_buttons_left: list[
            customtkinter.CTkButton] = []  # holds all buttons on the left to allow uniform styling
        # holds all entries formatted as buttons to allow uniform styling
        self.entries: list[customtkinter.CTkButton] = []

        # Configuring the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=9)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self._title_label: customtkinter.CTkLabel = \
            customtkinter.CTkLabel(master=self,
                                   width=frame_constants_i.FrameConstants.FULL_FRAME_WIDTH.value,
                                   height=frame_constants_i.FrameConstants.FULL_FRAME_HEIGHT.value * (1/5),
                                   corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                   fg_color=label_constants_i.LabelConstants.LABEL_TITLE_FG_COLOR.value,
                                   text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                   anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR_CENTER.value,
                                   text=main_window_constants_i.MainWindowConstants.WINDOW_TITLE.value)
        self._title_label.grid(row=0, column=0, rowspan=1, columnspan=2, sticky="NSEW")

        # Implementing the buttons

        self.main_buttons_left: list[customtkinter.CTkButton] = [
            customtkinter.CTkButton(master=self,
                                    text="New Project",
                                    command=self.__create_project),
            customtkinter.CTkButton(master=self,
                                    text="Load external Project",
                                    command=self.__load_external_project),
            customtkinter.CTkButton(master=self,
                                    text="Settings",
                                    command=self.__call_settings)
        ]

        # Align the buttons and give them the standard style-attributes
        for i, button in enumerate(self.main_buttons_left):
            button.configure(
                border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                width=button_constants_i.ButtonConstants.BUTTON_BASE_WIDTH_BIG.value,
                height=button_constants_i.ButtonConstants.BUTTON_BASE_HEIGHT_BIG.value
            )

            button.grid(row=i + 1, column=0, rowspan=1, columnspan=1, padx=10, pady=10)

        self._entry_subframe: customtkinter.CTkScrollableFrame = \
            customtkinter.CTkScrollableFrame(
                master=self,
                width=frame_constants_i.FrameConstants.FULL_FRAME_WIDTH.value * (9 / 10) - ELEMENT_BORDER_DISTANCE,
                height=frame_constants_i.FrameConstants.FULL_FRAME_HEIGHT.value * (4 / 5) - ELEMENT_BORDER_DISTANCE,
                corner_radius=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_CORNER_RADIUS.value,
                fg_color=scrollbar_constants_i.ScrollbarConstants.SCROLLBAR_FG_COLOR.value
            )
        self._entry_subframe.grid(row=1, column=1, rowspan=4, columnspan=1)

    def activate(self):
        """
        Overwrites the activate function from the Activatable-Interface
        Fetches all the data needed to update the window accordingly
        """
        self._passive_projects = self._project_controller.get_list_of_passive_projects()

        self.entries: list[customtkinter.CTkButton] = []
        # showing all entries in custom boxes
        for i, passive_project in enumerate(self._passive_projects):
            name = passive_project.get_name()  # name of the shown project
            description = passive_project.get_description()  # description of the shown project
            #reformatted_description = utility_methods_i.reformat_string(description)

            button_text: str = name + "\n\n" + description

            entry = customtkinter.CTkButton(master=self._entry_subframe,
                                            text=button_text,
                                            command=partial(self.__load_project, i),
                                            border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                            fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                            hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                            border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                            text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value,
                                            width=(frame_constants_i.FrameConstants.FULL_FRAME_WIDTH.value * (9 / 10) - ELEMENT_BORDER_DISTANCE) - ELEMENT_BORDER_DISTANCE,
                                            height=button_constants_i.ButtonConstants.BUTTON_BASE_HEIGHT_BIG.value
                                            )
            entry.grid(column=0, row=i, rowspan=1, columnspan=1, padx=10, pady=10)  # creates and places the button
            self.entries.append(entry)

    def __load_project(self, index: int):
        """
        Loads the given project

        Args:
            index (int): Project that will be loaded
        """
        project_name = self._passive_projects[index].get_name()

        try:
            default_path: Path = Path(os.path.join(self._project_controller.get_default_project_folder(), project_name))
            if not self._project_controller.load_project(default_path):
                popup = AlertPopUp("This is not a valid project.")
                popup.mainloop()
                self.activate()
                return

            # Loads the last edit step in the configuration
            config_phase: config_phase_enum_i.ConfigPhase = self._project_controller.get_current_config_phase()
            self._state_manager.change_state(find_matching_state(config_phase))

        except NotValidName as err:
            popup = AlertPopUp(str(err.args))
            popup.mainloop()
            self.activate()
            return

    def __create_project(self):
        """
        Calls the create_project-window switching states
        """
        self._state_manager.change_state(sne.StateName.CREATE_PROJECT)

    def __call_settings(self):
        """
        Calls the settings-menu switching states
        """
        self._state_manager.change_state(sne.StateName.SETTINGS_NO_PROJECT)

    def __load_external_project(self):
        """
        Loads a project from an external source. opens the explorer and lets the user choose the project.
        if the chosen project-path is not valid, an error occurs
        """
        new_path = Path(self.__browse_files())

        if not new_path.exists():
            # No valid Path was chosen: popup will be shown, page will reload
            popup = AlertPopUp("No valid Path entered. Please choose a valid Path")
            popup.mainloop()
            self.activate()
            return

        # Correct path was chosen, loading process will be initialised
        if not self._project_controller.load_project(new_path):
            popup = AlertPopUp("You selected a not valid project.")
            popup.mainloop()
            self.activate()
            return

        # Loads the last edit step in the configuration
        config_phase: config_phase_enum_i.ConfigPhase = self._project_controller.get_current_config_phase()
        self._state_manager.change_state(find_matching_state(config_phase))

    def __browse_files(self) -> str:
        """
        Opens the explorer starting from the current directory
        Returns:
            str: Name of the chosen path
        """
        new_path = \
            filedialog.askdirectory(title="Please select Your File",
                                    initialdir=self._settings_controller.get_project_default_folder())
        return new_path

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        for button in self.main_buttons_left:
            button.configure(state=tkinter.DISABLED)

        for entry in self.entries:
            entry.configure(state=tkinter.DISABLED)

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        for button in self.main_buttons_left:
            button.configure(state=tkinter.NORMAL)

        for entry in self.entries:
            entry.configure(state=tkinter.NORMAL)
