from __future__ import annotations

from src.osm_configurator.view.states.state_manager import StateManager
from src.osm_configurator.control.settings_controller_interface import ISettingsController
from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
from src.osm_configurator.view.utilityframes.settings_application_frame import SettingsApplicationFrame
from src.osm_configurator.view.utilityframes.settings_project_frame import SettingsProjectFrame

from typing import TYPE_CHECKING
import customtkinter

if TYPE_CHECKING:
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.settings_controller_interface import ISettingsController
    from src.osm_configurator.view.activatable import Activatable
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
    from src.osm_configurator.view.utilityframes.settings_project_frame import SettingsProjectFrame
    from src.osm_configurator.view.utilityframes.settings_application_frame import SettingsApplicationFrame


class SettingsFrame(Activatable, customtkinter.CTkToplevel):
    """
    This frame shows the user the settings for:
    - The application
    - The current project

    It either can be both or only the application settings.
    """

    def __init__(self, state_manager, settings_controller):
        """
        This method creates a SettingsFrame, that lets the user set the application and  project settings.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, if it wants to switch states.
            settings_controller (settings_controller.SettingsController): Respective controller
        """
        window = super().__init__()

        self._state_manager = state_manager
        self._settings_controller = settings_controller

        self.title = "Settings Frame"

        self.settings_application_frame = \
            SettingsApplicationFrame(self, self._settings_controller) \
            .pack(side="top")

        self.create_project_frame = \
            SettingsProjectFrame(self, self._settings_controller) \
            .pack(side="bottom")

    def activate(self):
        pass
