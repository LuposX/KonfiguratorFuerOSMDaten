from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame
import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.control_interface


class DataFrame(TopLevelFrame):
    """
    This Frame lets the user edit various Data as follows:
    - Selecting the OSM-Data
    - Selecting the Cut-Out, also able to select, if Buildings on the edge shall be included or not
    - Copy in Category Configurations
    """

    def __init__(self, state_manager, control):
        """
        This Method Creates a DataFrame, that lets the User input Data into the Project.

        Args:
            state_manager (state_manager.StateManager): The StateManager the Frame will call, when it wants to change to
            another State.
            control (control_interface.IControl): The Control the Frame will call, to get access to the Model.
        """
        super().__init__(state_manager, control)
        pass
