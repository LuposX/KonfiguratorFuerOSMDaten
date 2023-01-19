import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.aggregation_controller

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class AggregationFrame(TopLevelFrame):
    """
    This frame shows the aggregation page the user will interact on.
    This window provides the checkboxes to choose calculation methods and methods on how the aggregation will be calculated.
    """

    def __init__(self, state_manager, aggregation_controller):
        """
        This method creates an AggregationFrame that will be used to edit the aggregation method.

        Args:
            state_manager (state_manager.StateManager): The StateManager, the frame will call, when it wants to change to another state.
           aggregation_controller (aggregation_controller.AggregationController): Respective controller
        """
        #super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
