from __future__ import annotations

from src.osm_configurator.view.activatable import Activatable
from src.osm_configurator.view.freezable import Freezable
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


class SettingsFrame(TopLevelFrame):
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
            width=frame_constants_i.FrameConstants.MIDDLE_FRAME_WIDTH.value,
            height=frame_constants_i.FrameConstants.MIDDLE_FRAME_HEIGHT.value,
            corner_radius=frame_constants_i.FrameConstants.FRAME_CORNER_RADIUS.value,
            fg_color=frame_constants_i.FrameConstants.MIDDLE_FRAME_FG_COLOR.value,
        )

        # Defining the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._state_manager = state_manager
        self._settings_controller = settings_controller

        self._frames = []  # holds all shown frames to allow equals styling

        self.title = "Settings Frame"

        self.settings_application_frame = \
            settings_application_frame_i.SettingsApplicationFrame(self, self._settings_controller)
        self.settings_application_frame.grid(row=0, column=0, padx=10, pady=10)
        self.settings_application_frame.configure(border_width=2, border_color="#000000")
        self._frames.append(self.settings_application_frame)

        self.create_project_frame = \
            settings_project_frame_i.SettingsProjectFrame(self, self._settings_controller)
        self.create_project_frame.grid(row=1, column=0, padx=10, pady=10)
        self.create_project_frame.configure(border_width=2, border_color="#000000")
        self._frames.append(self.create_project_frame)

    def activate(self):
        """
        Gets called if the window is called.
        Calls the activate functions of the frames
        Returns:
            bool: True, if activation was successful, else false
        """
        # TODO: CHECK IF PROJECT IS LOADED OR NOT DU PIC

        self.settings_application_frame.activate()
        self.create_project_frame.activate()

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        for frame in self._frames:
            frame.freeze()

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        for frame in self._frames:
            frame.freeze()
