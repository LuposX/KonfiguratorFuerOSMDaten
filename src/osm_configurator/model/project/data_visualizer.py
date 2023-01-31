from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING

import src.osm_configurator.model.project.configuration.cut_out_configuration
import matplotlib

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.cut_out_configuration import CutOutConfiguration
    from matplotlib.axes import Axes



class DataVisualizer:
    """
    This class job is to visualize the cut-out file or data of the project.
    """

    def __init__(self):
        """
        Creates a new instance of the DataVisualizer.
        """
        pass

    def create_map(self, cut_out: CutOutConfiguration, destination: pathlib.Path) -> bool:
        """
        This method to create a map from to given cut-out.

        Args:
            cut_out (cut_out_configuration.CutOutConfiguration): The cut-out configuration from which the map should be created.
            destination (pathlib.Path): The path, where the map should be saved.

        Returns:
            bool: True if creating the map works, otherwise false.
        """
        pass

    def create_boxplot(self, data: Axes) -> bool:
        """
        This method is to visualize the data by creating a boxplot.
        It is used to visualize the calculated end result via a boxplot.

        Args:
            data (matplotlib.axes.Axes): A plot of the data which we want to visualize.

        Returns:
            bool: True if creating the boxplot works, otherwise false.
        """
        pass

    def _save_map(self, destination_path: pathlib.Path) -> bool:
        """
        This method so to save the map after creating it at a given path.
        The map in an HTML file format.

        Args:
            destination_path (pathlib.Path): The path, where the map should be saved.

        Returns:
            bool: True if saving the map works, otherwise false.
        """
        pass
