import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.settings_controller

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


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
        super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
