from __future__ import annotations

from src.osm_configurator.model.application.passive_project import PassiveProject
from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
import src.osm_configurator.view.states.state_name_enum as sne

# Constants
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i

# Other
import customtkinter
from tkinter import filedialog
from pathlib import Path

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.model.application.passive_project import PassiveProject


class MainMenuFrame(TopLevelFrame, Activatable):
    """
    This frame shows the application's main menu.
    The user can create a new project, or load an already existing project. Projects stored in the default folder
    will be shown in a list and can be selected / opened.
    """

    def __init__(self, state_manager: StateManager, project_controller: IProjectController):
        """
        This method creates a MainMenuFrame showing the MainMenu of the application.

        Args:
            state_manager (state_manager.StateManager): Frame will call the StateManager, if it wants to switch states
            project_controller (project_controller.ProjectController): Respective controller
        """

        super().__init__(master=None,
                         width=frame_constants_i.FrameConstants.HEAD_FRAME_WIDTH.value,
                         height=frame_constants_i.FrameConstants.HEAD_FRAME_HEIGHT.value,
                         corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
                         fg_color=frame_constants_i.FrameConstants.HEAD_FRAME_FG_COLOR.value)

        self._project_controller = project_controller
        self._state_manager = state_manager
        self._passive_projects = []

        # Configuring the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=1)

        # Implementing the buttons

        self.main_buttons_left = [
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
                text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value
            )

            button.grid(row=i, column=0, rowspan=1, columnspan=1, padx=10, pady=10)

        # showing all entries in custom boxes
        for i, passive_project in enumerate(self._passive_projects):
            name = passive_project.get_name()  # name of the shown project
            description = passive_project.get_description()  # description of the shown project

            customtkinter.CTkButton(master=self,
                                    name=name,
                                    text=name,
                                    description=description,
                                    command=self.__load_project(passive_project),
                                    rder_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value
                                    ) \
                .grid(column=3, row=i, rowspan=1, columnspan=1, padx=10, pady=10)  # creates and places the button

    def activate(self) -> bool:
        """
        Overwrites the activate function from the Activatable-Interface
        Fetches all the data needed to update the window accordingly
        Returns:
            bool: True if activation was successful, else false
        """
        self._passive_projects = self._project_controller.get_list_of_passive_projects()
        return True

    def __load_project(self, passive_project: PassiveProject):
        """
        Loads the given project
        Args:
            passive_project (PassiveProject): Project that will be loaded
        """
        project_path = passive_project.get_project_folder_path()
        self._project_controller.load_project(project_path)

    def __create_project(self):
        """
        Calls the create_project-window switching states
        """
        self._state_manager.change_state(sne.StateName.CREATE_PROJECT.value)

    def __call_settings(self):
        """
        Calls the settings-menu switching states
        """
        self._state_manager.change_state(sne.StateName.SETTINGS.value)

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
        self._project_controller.load_project(new_path)

    def __browse_files(self) -> str:
        """
        Opens the explorer starting from the current directory
        Returns:
            str: Name of the chosen path
        """
        new_path = \
            filedialog.askopenfilename(title="Please select Your File",
                                       filetypes=".geojson")
        return new_path

