import pythoncode.src.osm_configurator.view.states.state_manager
import pythoncode.src.osm_configurator.control.control_interface
from pythoncode.src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class ProjectFootFrame(TopLevelFrame):
    """
    This Frame shows two arrows on the Bottom of the Window. The User can navigate the Pipeline by going left or right.
    """

    def __init__(self, state_manager, control):
        """
        This Method creates a ProjectFootFrame, that lets the User navigate the PipeLine by going left or right.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, if it wants to switch States.
            control (control_interface.IControl): The Frame will call the Control, to gain access to the Model.
        """
        super().__init__(state_manager, control)
        pass
