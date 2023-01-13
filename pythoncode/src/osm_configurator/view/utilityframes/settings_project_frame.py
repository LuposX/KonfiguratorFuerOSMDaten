import src.osm_configurator.view.toplevelframes.settings_frame
import src.osm_configurator.control.control_interface


class SettingsProjectFrame:
    """
    This frame shows the current project settings.
    """

    def __init__(self, parent, control):
        """
        This method creates a SettingsProjectFrame, showing the current project settings.

        Args:
            parent (settings_frame.SettingsFrame): The parent of this frame where this frame will be located.
            control (control_interface.IControl): The control the frame will call to gain access to the model.
        """
        pass

    def activate(self):
        """
        Tells the current frame to activate and collect all the data it needs.

        Returns:
            bool: True, if activation was successful, otherwise false.
        """
        pass
