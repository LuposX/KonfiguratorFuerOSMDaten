import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class ReductionFrame(TopLevelFrame):
    """
    This Frame lets the User edit the reduction of all the Categories.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates a ReductionFrame, that lets the user edit the Reduction of all the Categories.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (control_interface.IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
