from __future__ import annotations

from src.osm_configurator.view.states.state_manager import StateManager
from src.osm_configurator.control.settings_controller_interface import ISettingsController
from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
from src.osm_configurator.view.utilityframes.settings_application_frame import SettingsApplicationFrame
from src.osm_configurator.view.utilityframes.settings_project_frame import SettingsProjectFrame
from src.osm_configurator.view.constants.frame_constants import FrameConstants

from typing import TYPE_CHECKING
import customtkinter

if TYPE_CHECKING:
    from src.osm_configurator.view.states.state_manager import StateManager
    from src.osm_configurator.control.settings_controller_interface import ISettingsController
    from src.osm_configurator.view.activatable import Activatable
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
    from src.osm_configurator.view.utilityframes.settings_project_frame import SettingsProjectFrame
    from src.osm_configurator.view.utilityframes.settings_application_frame import SettingsApplicationFrame


class SettingsFrame(TopLevelFrame, Activatable):
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
        super().__init__()

        self._state_manager = state_manager
        self._settings_controller = settings_controller

        self.title = "Settings Frame"

        self.settings_application_frame = \
            SettingsApplicationFrame(self, self._settings_controller) \
            .pack(side="top", padx=10, pady=10)

        self.create_project_frame = \
            SettingsProjectFrame(self, self._settings_controller) \
            .pack(side="bottom", padx=10, pady=10)

    def activate(self) -> bool:
        """
        Gets called if the window is called.
        Calls the activate functions of the frames
        Returns:
            bool: True, if activation was successful, else false
        """
        settings_activation = self.settings_application_frame.activate()
        create_project_activation = self.create_project_frame.activate()

        if settings_activation and create_project_activation:
            return True  # Activation successful
        return False
