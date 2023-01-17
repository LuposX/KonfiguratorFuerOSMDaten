import src.osm_configurator.view.states.state_manager

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class ReductionFrame(TopLevelFrame):
    """
    This frame lets the user edit the reduction of all the categories.
    It will consist of a list on the left to choose a category.
    On the right will be two sub-frames to change inbetween.
    On the right are two interchangeable sub-frames: One frame provides the configuration-options on how to
    calculate the Reduction. The other frame provides the default calculation-values.
    """

    def __init__(self, state_manager, control):
        """
        This method creates a ReductionFrame that lets the user edit the reduction of all the categories.

        Args:
            state_manager (state_manager.StateManager): The frame will call the StateManager, if it wants to switch states.
            control (control_interface.IControl): The control the frame will call to get access to the model.
        """
        super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
