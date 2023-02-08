from __future__ import annotations

from src.osm_configurator.view.toplevelframes.settings_frame import SettingsFrame
from src.osm_configurator.control.settings_controller_interface import ISettingsController
from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp

from pathlib import Path
import customtkinter
from tkinter import filedialog

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.view.toplevelframes.settings_frame import SettingsFrame
    from src.osm_configurator.control.settings_controller_interface import ISettingsController
    from src.osm_configurator.view.activatable import Activatable
    from src.osm_configurator.view.popups.alert_pop_up import AlertPopUp


class SettingsApplicationFrame(customtkinter.CTkFrame, Activatable):
    """
    This frame shows the settings of the application.
    """

    # TODO: Adjust customtkinter attributes to the given enums

    def __init__(self, parent, settings_controller: ISettingsController):
        """
        This method creates a SettingsApplicationFrame, showing the settings of the application.

        Args:
            parent (settings_frame.SettingsFrame): The parent of this frame where this frame will be located.
            settings_controller (settings_controller.SettingsController): Respective controller.
        """
        frame = super().__init__()

        self._parent = parent
        self._settings_controller = settings_controller

        self._project_default_folder = ISettingsController.get_project_default_folder(self._settings_controller)

        self.header = customtkinter.CTkLabel(self, text="General Settings")
        self.header.grid(row=0, line=0, xpad=30, ypad=30)

        self.path_default_header = customtkinter.CTkLabel(self, text="Default Folder") \
            .grid(row=1, line=0, xpad=20, ypad=20)

        self.path_default_box = customtkinter.CTkTextbox(self, text=self._project_default_folder.name, state="disabled") \
            .grid(row=2, line=0, xpad=20, ypad=20)  # Creates a read-only textbox showing the default-filepath

        self.change_default_path_button = customtkinter.CTkButton(self, text="Change Default Folder",
                                                                  command=self.__change_default_folder) \
            .grid(row=3, line=0, xpad=20, ypad=20)  # button to browse for a new default folder

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

    def __change_default_folder(self) -> bool:
        """
        Opens the explorer making the user choose a new path for the default folder
        Changes the default folder to the path that was chosen.
        Checks if the path is valid and confirms changes if so.
        If the path is not valid a popup will be shown reloading the page
        Returns:
            bool: True if change was successful, else False
        """
        new_path = Path(self.__browse_files())

        if new_path.exists():
            self._project_default_folder = new_path
            self._settings_controller.set_project_default_folder(new_path)  # Updates the path
            self.path_default_box.configure(text=new_path.name)  # Updates the textbox
            return True
        popup = AlertPopUp("Please enter a valid path!")
        popup.mainloop()  # shows the popup
        self.activate()  # reloads the page
        return False

    def __browse_files(self) -> str:
        """
        Opens the explorer starting from the default-folder making the user browse for the searched path
        Returns:
            str: The path-name
        """
        new_path = filedialog.askopenfilename(initialdir=self._project_default_folder,
                                              title="Select a File",
                                              filetypes=".geojson")
        return new_path
