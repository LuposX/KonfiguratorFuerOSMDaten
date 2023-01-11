import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class CalculationFrame(TopLevelFrame):
    """
    This Frame lets the User start the Calculation from a selected phase, indicated by different Buttons.
    Once a calculation is started, there will be a Progressbar shown, the different buttons will be deactivated
    and the current calculation-phase will be shown.
    A Cancel-Button is provided to stop the Calculation.
    """

    def __init__(self, state_manager, control):
        """
        This Method creates a CalculationFrame that will let the user start the Calculation
        and shows the Calculation-Progress.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, if it wants to switch to
            another State.
            control (control_interface.IControl): The Frame will call the Control to gain access to the Model.
        """
        super().__init__(state_manager, control)
        pass
