from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController

import pathlib
import matplotlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication


class DataVisualizationController(IDataVisualizationController):
    __doc__ = IDataVisualizationController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the DataVisualizationController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def generate_cut_out_map(self) -> pathlib.Path:
        pass

    def get_calculation_visualization(self) -> matplotlib.axes.Axes:
        pass
