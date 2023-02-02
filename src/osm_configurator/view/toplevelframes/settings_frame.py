from __future__ import annotations

from src.osm_configurator.view.states.state_manager import StateManager
from src.osm_configurator.control.settings_controller_interface import ISettingsController
from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

from typing import TYPE_CHECKING
import customtkinter

if TYPE_CHECKING:
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.settings_controller_interface import ISettingsController
    from src.osm_configurator.view.activatable import Activatable
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


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

    def activate(self):
        pass
