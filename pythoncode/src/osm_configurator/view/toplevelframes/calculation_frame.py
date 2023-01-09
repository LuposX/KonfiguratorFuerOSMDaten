import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class CalculationFrame(TopLevelFrame):
    """
    This Frame lets the User start the Calculation and shows the progress of said Calculation.
    """

    def __init__(self, state_manager, control):
        """
        This Method creates a CalculationFrame that will let the user start the Calculation and shows the progress
        of said Calculation.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (control_interface.IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
