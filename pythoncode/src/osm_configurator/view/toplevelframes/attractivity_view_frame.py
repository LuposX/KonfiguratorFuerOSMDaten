import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface
from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class AttractivityViewFrame(TopLevelFrame):
    """
    This Frame shows a List with all Categories, their Attractivity-Attributes and how they are calculated.
    This is only a visualisation and therefore a non-edit Frame.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates an AttractivityViewFrame showing a List of containing all Categories,
        their according Attractivity-Attributes and how they are calculated.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, if it tries to switch to another State.
            control (control_interface.IControl): The Frame will call the Control to gain access to the Model.
        """
        super().__init__(state_manager, control)
        pass
