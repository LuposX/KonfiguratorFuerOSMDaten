from pythoncode.src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
import pythoncode.src.osm_configurator.view.states.state_manager
import pythoncode.src.osm_configurator.control.control_interface


class DataFrame(TopLevelFrame):
    """
    This Frame lets the user edit various following Data:
    - Selection of the OSM-Data
    - Selection of the Cut-Out
    - Select, if Buildings on the edge shall be included or not
    - A download button to download the OSM data after a Cut-Out was selected
    - Copy in Category Configurations
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates a DataFrame, that lets the User input Data into the Project.

        Args:
            state_manager (state_manager.StateManager): The Frame will call the StateManager, if it wants to switch States.
            control (control_interface.IControl): The Frame will call the Control, to gain access to the Model.
        """
        super().__init__(state_manager, control)
        pass
