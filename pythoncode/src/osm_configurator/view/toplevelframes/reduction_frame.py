import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class ReductionFrame(TopLevelFrame):
    """
    This Frame lets the User edit the Reduction of all the Categories.
    It will consist of a list on the left to choose a category.
    On the right will be two sub-frames to change
    inbetween.
    On the right are two interchangeable sub-frames: One frame provides the configuration-Options on how to
    Calculate the Reduction. The Other Frame Provides the default Calculation-Values.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates a ReductionFrame, that lets the user edit the Reduction of all the Categories.

        Args:
            state_manager (state_manager.StateManager): The Frame will call the StateManager, if it wants to switch States.
            control (control_interface.IControl): The Frame will call the Control, to gain access to the Model.
        """
        super().__init__(state_manager, control)
        pass
