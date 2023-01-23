from __future__ import annotations

from abc import ABC, abstractmethod

import pathlib
import matplotlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication


class IDataVisualizationController(ABC):
    """
    The DataVisualizationController is responsible for forwarding requests to the model,
    regarding the visualization of data from the model.
    """

    @abstractmethod
    def generate_cut_out_map(self):
        """
        Generates a map of the data of the currently selected project.
        Using the cut-out file of the project, this function creates a map as a html-file of the project. The path to the html-file is returned.

        Returns:
            pathlib.Path: The path to the file where the map is stored.
        """
        pass

    @abstractmethod
    def get_calculation_visualization(self):
        """
        Generates a graphic that visualizes the results of the calculations of the currently selected project.

        Returns:
            matplotlib.axes.Axes: The resulting visualization as axes of the matplotlib library.
        """
        pass
