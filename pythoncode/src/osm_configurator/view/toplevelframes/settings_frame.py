import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
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
        This Method creates a SettingsFrame, that lets the user set the Application and Project-Settings.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, if it wants to switch States.
            control (control_interface.IControl): The Control the Frame will call, to gain access to the Model.
        """
        super().__init__(state_manager, control)
        pass
