import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.data_visualization_controller
import src.osm_configurator.control.cut_out_controller
import src.osm_configurator.control.category_controller

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class DataFrame(TopLevelFrame):
    """
    This frame lets the user edit various following Data:
    - Selection of the OSM-Data
    - Selection of the Cut-Out
    - Select, if buildings on the edge shall be included or not
    - A download button to download the OSM data after a cut-out was selected
    - Copy in category configurations
    """

    def __init__(self, state_manager, data_visualization_controller, cut_out_controller, category_controller):
        """
        This method creates a DataFrame, that lets the User input data into the project.

        Args:
            state_manager (state_manager.StateManager): The frame will call the StateManager, if it wants to switch states.
            data_visualization_controller (data_visualization_controller.DataVisualizationController): Respective controller
            cut_out_controller (cut_out_controller.CutOutController): Respective controller
            category_controller (category_controller.CategoryController): Respective controller
        """
        # super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
