import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class AggregationFrame(TopLevelFrame):
    """
    This frame shows the aggregation page the user will interact on.
    This window provides the checkboxes to choose calculation methods and methods on how the aggregation will be calculated.
    """

    def __init__(self, state_manager, control):
        """
        This method creates an AggregationFrame, that will be used to edit the aggregation method.

        Args:
            state_manager (state_manager.StateManager): The StateManager, the frame will call, when it wants to change to another state.
            control (control_interface.IControl): The control, the Frame will call, to get access to the model.
        """
        super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
