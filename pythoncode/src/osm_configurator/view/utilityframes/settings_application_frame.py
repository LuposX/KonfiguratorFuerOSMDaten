import src.osm_configurator.view.toplevelframes.settings_frame
import src.osm_configurator.control.control_interface


class SettingsApplicationFrame:
    """
    This frame shows the settings of the application.
    """

    def __init__(self, parent, control):
        """
        This method creates a SettingsApplicationFrame, showing the settings of the application.

        Args:
            parent (settings_frame.SettingsFrame): The parent of this frame where this frame will be located.
            control (control_interface.IControl): The control the frame will call to gain access to the model and application_settings.
        """
        pass

    def activate(self):
        """
        Tells the current frame to activate and collect all the data it needs.

        Returns:
            bool: True, if activation was successful, otherwise false.
        """
        pass
