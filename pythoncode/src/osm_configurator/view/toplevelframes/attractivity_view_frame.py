import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class AttractivityViewFrame(TopLevelFrame):
    """
    This frame shows a list with all categories, their attractivity attributes and how they are calculated.
    This is only a visualisation and therefore a non-edit Frame.
    """

    def __init__(self, state_manager, control):
        """
        This method creates an AttractivityViewFrame showing a lList of containing all categories,
        their according attractivity attributes and how they are calculated.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, if it tries to switch to another atate.
            control (control_interface.IControl): The control the frame will call to get access to the model.
        """
        super().__init__(state_manager, control)
        pass
