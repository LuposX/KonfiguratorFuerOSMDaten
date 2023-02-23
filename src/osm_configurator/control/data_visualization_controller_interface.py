from __future__ import annotations

from abc import ABC, abstractmethod

import pathlib
import matplotlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication
    from pathlib import Path, List


class IDataVisualizationController(ABC):
    """
    The DataVisualizationController is responsible for forwarding requests to the model,
    regarding the visualization of data from the model.
    """

    @abstractmethod
    def generate_cut_out_map(self) -> pathlib.Path | None:
        """
        Generates a map of the data of the currently selected project.
        Using the cut-out file of the project, this function creates a map as a html-file of the project.
        The path to the html-file is returned.

        Returns:
            pathlib.Path: The path to the file where the map is stored.
            None: If the saving of the map failed.
        """
        pass

    @abstractmethod
    def generate_calculation_visualization(self) -> List[str] | None:
        """
        Generates a graphic that visualizes the results of the calculations of the currently selected project.

         Returns:
            List[str]:  A list of paths each pointing towards one boxplot image.
            None: If the saving/generating of the image failed.
        """
        pass
