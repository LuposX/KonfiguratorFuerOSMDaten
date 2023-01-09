from src.osm_configurator.view.toplevelframes.settings_frame import SettingsFrame
from src.osm_configurator.control.control_interface import IControl


class SettingsApplicationFrame:
    """
    This Frame shows the Settings for the Application.
    """

    def __init__(self, parent, control):
        """
        This Method Creates a SettingsApplicationFrame, that shows the Settings for the Application.

        Args:
            parent (SettingsFrame): The Parent of this Frame, where this Frame will be located.
            control (IControl): The Control the Frame will call, to get access to the Model and Application Settings.
        """
        pass
