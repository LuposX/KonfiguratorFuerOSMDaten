import pythoncode.src.osm_configurator.view.states.state_manager
import pythoncode.src.osm_configurator.control.control_interface
from pythoncode.src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class AttractivityViewFrame(TopLevelFrame):
    """
    This Frame shows a List with all Categories and their Attractivity-Attributes and how they are calculated.
    This is only a visualisation and a non edit Frame.
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates an AttractivityViewFrame that shows thze user a List of
        all Categories and their Attractivity-Attributes and how they are calculated.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (control_interface.IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
