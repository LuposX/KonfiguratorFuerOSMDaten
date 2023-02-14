from __future__ import annotations

from src.osm_configurator.view.activatable import Activatable

import src.osm_configurator.control.settings_controller_interface as settings_controller_i

# Constants
import src.osm_configurator.view.constants.button_constants as button_constants_i
import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.constants.text_box_constants as text_constants_i
import src.osm_configurator.view.constants.label_constants as label_constants_i

from pathlib import Path
import customtkinter
from tkinter import filedialog

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.control.settings_controller_interface import ISettingsController
    from src.osm_configurator.view.activatable import Activatable
    from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp


class SettingsApplicationFrame(customtkinter.CTkFrame, Activatable):
    """
    This frame shows the settings of the application.
    """

    def __init__(self, parent, settings_controller: ISettingsController):
        """
        This method creates a SettingsApplicationFrame, showing the settings of the application.

        Args:
            parent (settings_frame.SettingsFrame): The parent of this frame where this frame will be located.
            settings_controller (settings_controller.SettingsController): Respective controller.
        """
        super().__init__(
            master=None,
            width=frame_constants_i.FrameConstants.HEAD_FRAME_WIDTH.value,
            height=frame_constants_i.FrameConstants.HEAD_FRAME_HEIGHT.value / 2,
            corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
            fg_color=frame_constants_i.FrameConstants.HEAD_FRAME_FG_COLOR.value
        )

        self._parent = parent
        self._settings_controller = settings_controller

        self._project_default_folder: Path = self._settings_controller.get_project_default_folder()

        # Defining the grid-structure
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header = \
            customtkinter.CTkLabel(master=self,
                                   text="General Settings")
        self.header.grid(row=0, column=0, columnspan=1, rowspan=1, padx=10, pady=10)

        self.path_default_header = \
            customtkinter.CTkLabel(master=self,
                                   text="Default Folder",
                                   corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                   fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                   text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                   anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value)
        self.path_default_header.grid(row=1, column=0, columnspan=1, rowspan=1, padx=10, pady=10)

        self.path_default_label = \
            customtkinter.CTkLabel(master=self,
                                   text=str(self._project_default_folder),
                                   corner_radius=label_constants_i.LabelConstants.LABEL_CONSTANTS_CORNER_RADIUS.value,
                                   fg_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_FG_COLOR.value,
                                   text_color=label_constants_i.LabelConstants.LABEL_CONSTANTS_TEXT_COLOR.value,
                                   anchor=label_constants_i.LabelConstants.LABEL_CONSTANTS_ANCHOR.value)
        self.path_default_label.grid(row=2, column=0, padx=10, pady=10)  # Creates a read-only textbox showing the default-filepath

        self.change_default_path_button = \
            customtkinter.CTkButton(master=self,
                                    text="Change Default Folder",
                                    command=self.__change_default_folder,
                                    corner_radius=button_constants_i.ButtonConstants.BUTTON_CORNER_RADIUS.value,
                                    border_width=button_constants_i.ButtonConstants.BUTTON_BORDER_WIDTH.value,
                                    fg_color=button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value,
                                    hover_color=button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value,
                                    border_color=button_constants_i.ButtonConstants.BUTTON_BORDER_COLOR.value,
                                    text_color=button_constants_i.ButtonConstants.BUTTON_TEXT_COLOR.value
                                    )
        self.change_default_path_button.grid(row=3, column=0, padx=10, pady=10)  # button to browse for a new default folder

    def activate(self) -> bool:
        """
        Tells the current frame to activate and collect all the data it needs.

        Returns:
            bool: True, if activation was successful, otherwise false.
        """
        self._project_default_folder = ISettingsController.get_project_default_folder(self._settings_controller)

        if self._project_default_folder != "":
            return True
        return False

    def __change_default_folder(self):
        """
        Opens the explorer making the user choose a new path for the default folder
        Changes the default folder to the path that was chosen.
        Checks if the path is valid and confirms changes if so.
        If the path is not valid a popup will be shown reloading the page
        """
        new_path = Path(self.__browse_files())

        if new_path.exists():
            self._project_default_folder = new_path
            self._settings_controller.set_project_default_folder(new_path)  # Updates the path
            self.path_default_label.configure(text=new_path.name)  # Updates the textbox
            return
        popup = AlertPopUp("Please enter a valid path!")
        popup.mainloop()  # shows the popup
        self.activate()  # reloads the page

    def __browse_files(self) -> str:
        """
        Opens the explorer starting from the default-folder making the user browse for the searched path
        Returns:
            str: Name of the chosen path
        """
        new_path = \
            filedialog.askopenfilename(initialdir=self._project_default_folder,
                                       title="Select a File",
                                       filetypes=".geojson")
        return new_path
