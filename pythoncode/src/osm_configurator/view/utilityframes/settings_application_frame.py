import src.osm_configurator.view.toplevelframes.settings_frame
import src.osm_configurator.control.settings_controller

from src.osm_configurator.view.activatable import Activatable


class SettingsApplicationFrame(Activatable):
    """
    This frame shows the settings of the application.
    """

    def __init__(self, parent, settings_controller):
        """
        This method creates a SettingsApplicationFrame, showing the settings of the application.

        Args:
            parent (settings_frame.SettingsFrame): The parent of this frame where this frame will be located.
            settings_controller (settings_controller.SettingsController): Respective controller.
        """
        pass

    def activate(self):
        """
        Tells the current frame to activate and collect all the data it needs.

        Returns:
            bool: True, if activation was successful, otherwise false.
        """
        pass
