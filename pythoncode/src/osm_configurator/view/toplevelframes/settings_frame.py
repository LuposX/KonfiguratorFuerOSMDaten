from src.osm_configurator.view.states.state_manager import StateManager
from src.osm_configurator.control.control_interface import IControl
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class SettingsFrame(TopLevelFrame):
    """
    This Frame shows the User the Settings for:
    - The Application
    - The current Project

    It either can be both or only the Application Settings.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates a SettingsFrame, that lets the user set the Settings, for Application
        and the current Project.

        Args:
            state_manager (StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
