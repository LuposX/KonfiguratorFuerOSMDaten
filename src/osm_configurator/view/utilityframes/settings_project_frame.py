from __future__ import annotations

import customtkinter

from src.osm_configurator.view.toplevelframes.settings_frame import SettingsFrame
from src.osm_configurator.control.settings_controller_interface import ISettingsController
from src.osm_configurator.view.activatable import Activatable


class SettingsProjectFrame(customtkinter.CTkFrame, Activatable):
    """
    This frame shows the current project settings.
    """

    def __init__(self, parent, settings_controller):
        """
        This method creates a SettingsProjectFrame, showing the current project settings.

        Args:
            parent (settings_frame.SettingsFrame): The parent of this frame where this frame will be located.
            settings_controller (settings_controller.SettingsController): Respective controller.
        """
        frame = super.__init__()

        self._parent = parent
        self._settings_controller = settings_controller

        self._project_name = ISettingsController.get_project_name(self._settings_controller)

        self.header = customtkinter.CTkLabel(self, text="Current Project")
        self.header.grid(row=0, column=0, padx=10, pady=10)

        self.project_name_box = customtkinter.CTkTextbox(self, text=self._project_name)
        self.change_project_name_button = customtkinter.CTkButton(self, text="Change Project Name",
                                                                  command=self.__change_project_name)

    def activate(self):
        """
        Tells the current frame to activate and collect all the data it needs.

        Returns:
            bool: True, if activation was successful, otherwise false.
        """
        pass

    def __change_project_name(self):
        """
        Changes the current project name to whatever was entered in the textbox
        Reads the textbox-entry and changes the name by calling the given settings-controller
        """
        self._project_name = self.project_name_box.get("0.0", "end")  # Read everything submitted to the textbox
        ISettingsController.set_project_name(self._settings_controller, self._project_name)
