import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.calculation_controller
import src.osm_configurator.control.data_visualization_controller

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class CalculationFrame(TopLevelFrame):
    """
    This frame lets the user start the calculation from a selected phase, indicated by different buttons.
    Once a calculation is started, there will be a progressbar shown, the different buttons will be deactivated
    and the current calculation-phase will be shown.
    A cancel-Button is provided to stop the calculation.
    The CalculationFrame shows popups, if an error occurs in the calculations.
    """

    def __init__(self, state_manager, calculation_controller, data_visualization_controller):
        """
        This method creates a CalculationFrame that will let the user start the calculation
        and shows the calculation progress.

        Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, if it wants to switch to another state.
             calculation_controller (calculation_controller.CalculationController): Respective controller.
             data_visualization_controller (data_visualization_controller.DataVisualizationController): Respective controller.
        """
        #super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
