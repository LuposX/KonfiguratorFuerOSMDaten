from src.osm_configurator.view.states.state_manager import StateManager
from src.osm_configurator.control.control_interface import IControl
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class AggregationFrame(TopLevelFrame):
    """
    This Frame shows the Aggregation page the user will interact on, to define the Aggregation will be calculated, via
    checkboxes, to turn on and off calculation methods.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates an AggregationFrame, to edit the aggregation method.

        Args:
            state_manager (StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
