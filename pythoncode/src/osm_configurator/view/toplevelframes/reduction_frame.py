import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class ReductionFrame(TopLevelFrame):
    """
    This Frame lets the User edit the reduction of all the Categories.
    It will consist of a list on the left to choose a category and on the rigth will be two subframes to change
    inbetween.
    One for providing configuration options on how to calculate the reduction.
    And one for providing default values to calculate with.
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
