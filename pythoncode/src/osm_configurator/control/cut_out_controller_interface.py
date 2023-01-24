from __future__ import annotations

from abc import ABC, abstractmethod

import pathlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication
    from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode


class ICutOutController(ABC):
    """
    The CutOutController is responsible for consistently forwarding requests to the model,
    concerning the cut-out filter of the currently selected project.
    """

    @abstractmethod
    def get_cut_out_mode(self) -> CutOutMode:
        """
        Gets the method of how the geofilter shall cut out on the OSM-Data.

        Returns:
            cut_out_mode_enum.CutOutMode: The cut-out-mode of the currently selected project.
        """
        pass

    @abstractmethod
    def set_cut_out_mode(self, mode: CutOutMode) -> bool:
        """
        Sets the method of how the geofilter shall cut out on the OSM-Data.

        Args:
            mode (cut_out_mode_enum.CutOutMode): The mode to be set.

        Returns:
            bool: True, if the CutOutMode was set successfully; False, if an error occurred or no project is currently selected.
        """
        pass

    @abstractmethod
    def set_cut_out_reference(self, path: pathlib.Path) -> bool:
        """
        Sets the reference to the cut-out file of the currently selected project.
        This file is later used to calculate the geofilter.

        Args:
            path (pathlib.Path): The path to the file containing the cut-out-geometries.

        Returns:
            bool: True, if the reference was set successfully; False, if an error occurred. An error occurs, if no project is currently selected or if the given path is not valid or occupied.
        """
        pass

    @abstractmethod
    def get_cut_out_reference(self) -> pathlib.Path:
        """"
        Gets the reference to the cut-out file of the currently selected project.

        Returns:
            pathlib.Path: The current reference to the cut-out file.
        """
        pass
