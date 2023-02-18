from __future__ import annotations

from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


import src.osm_configurator.view.constants.frame_constants as frame_constants_i
import src.osm_configurator.view.utilityframes.settings_application_frame as settings_application_frame_i
import src.osm_configurator.view.utilityframes.settings_project_frame as settings_project_frame_i


from typing import TYPE_CHECKING
import customtkinter

if TYPE_CHECKING:
    from src.osm_configurator.view.activatable import Activatable
    from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
    from src.osm_configurator.view.utilityframes.settings_project_frame import SettingsProjectFrame


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
        super().__init__(
            master=None,
            width=frame_constants_i.FrameConstants.HEAD_FRAME_WIDTH.value,
            height=frame_constants_i.FrameConstants.HEAD_FRAME_HEIGHT.value,
            corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
            fg_color=frame_constants_i.FrameConstants.HEAD_FRAME_FG_COLOR.value
        )

        # Defining the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._state_manager = state_manager
        self._settings_controller = settings_controller

        self.title = "Settings Frame"

        self.settings_application_frame = \
            settings_application_frame_i.SettingsApplicationFrame(self, self._settings_controller)
        self.settings_application_frame.grid(row=0, column=0, padx=10, pady=10)

        self.create_project_frame = \
            settings_project_frame_i.SettingsProjectFrame(self, self._settings_controller)
        self.create_project_frame.grid(row=1, column=0, padx=10, pady=10)

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
