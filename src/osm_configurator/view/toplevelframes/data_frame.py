from __future__ import annotations

from typing import TYPE_CHECKING
import customtkinter

import src.osm_configurator.view.states.state_manager as state_manager
import src.osm_configurator.control.data_visualization_controller_interface as data_visualization_controller_interface
import src.osm_configurator.control.cut_out_controller_interface as cut_out_controller_interface
import src.osm_configurator.control.category_controller_interface as category_controller_interface
import src.osm_configurator.control.osm_data_controller_interface as osm_data_controller_interface
from src.osm_configurator.view.activatable import Activatable

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame

if TYPE_CHECKING:
    import src.osm_configurator.view.states.state_manager
    import \
        src.osm_configurator.control.data_visualization_controller_interface as data_visualization_controller_interface
    import src.osm_configurator.control.cut_out_controller_interface as cut_out_controller_interface
    import src.osm_configurator.control.category_controller_interface as category_controller_interface
    import src.osm_configurator.control.osm_data_controller_interface as osm_data_controller_interface


class DataFrame(TopLevelFrame, Activatable):
    """
    This frame lets the user edit various following Data:
    - Selection of the OSM-Data
    - Selection of the Cut-Out
    - Select, if buildings on the edge shall be included or not
    - A download button to download the OSM data after a cut-out was selected
    - Copy in category configurations
    """

    def __init__(self, _state_manager: state_manager,
                 data_visualization_controller: data_visualization_controller_interface,
                 cut_out_controller: cut_out_controller_interface, category_controller: category_controller_interface,
                 osm_data_controller: osm_data_controller_interface):
        """
        This method creates a DataFrame, that lets the User input data into the project.

        Args:
            _state_manager (state_manager.StateManager): The frame will call the StateManager, if it wants to switch states.
            data_visualization_controller (data_visualization_controller.DataVisualizationController): Respective controller
            cut_out_controller (cut_out_controller.CutOutController): Respective controller
            category_controller (category_controller.CategoryController): Respective controller
            osm_data_controller (osm_data_controller_interface.IOSMDataController): Respective controller
        """
        super().__init__()

        self._data_visualization_controller = data_visualization_controller
        self._cut_out_controller = cut_out_controller
        self._category_controller = category_controller
        self._osm_data_controller = osm_data_controller

        # Defining the grid
        self.grid_columnconfigure(0, weight=1)  # Space between top and first label
        self.grid_columnconfigure(1, weight=2)  # Space for the top labels
        self.grid_columnconfigure(2, weight=3)  # Space for the upper buttons
        self.grid_columnconfigure(3, weight=2)  # Space for the displayed buttons values
        self.grid_columnconfigure(4, weight=2)  # Space for the Checkbox
        self.grid_columnconfigure(5, weight=3)  # Space for the lower button
        self.grid_columnconfigure(6, weight=2)  # Free space

        self.grid_rowconfigure(0, weight=1)  # Free Space on the left edge
        self.grid_rowconfigure(1, weight=4)  # Space for the buttons on the left
        self.grid_rowconfigure(2, weight=2)  # Space for the middle buttons
        self.grid_rowconfigure(3, weight=2)  # Space for the middle buttons
        self.grid_rowconfigure(4, weight=4)  # Space for the buttons on the right
        self.grid_rowconfigure(5, weight=1)  # Free Space on the right edge

    def activate(self):
        pass
