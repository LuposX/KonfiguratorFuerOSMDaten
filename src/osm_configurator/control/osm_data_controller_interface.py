from __future__ import annotations

import pathlib

from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication


class IOSMDataController(ABC):
    """
    The OSMDataController is responsible for consistently forwarding requests
    regarding the OSM-data of the currently selected project.
    """

    @abstractmethod
    def set_osm_data_reference(self, path: pathlib.Path) -> bool:
        """
        Sets the reference to the osm-data for the selected project.
        The reference contains the osm-data used in the calculations of the project. This method does not check if the given data is valid.

        Args:
            path (pathlib.Path): The reference to the osm-data.

        Returns:
            bool: True, if the new reference was set successfully; False, if an error occurred while setting the reference.
        """
        pass

    @abstractmethod
    def get_osm_data_reference(self) -> pathlib.Path:
        """
        Returns the path to the osm-data, that is used in the currently selected project.

        Returns:
            pathlib.Path: The path to the osm-data of the currently selected project.
        """
        pass

    @abstractmethod
    def download_osm_data(self, path: pathlib.Path) -> bool:
        """
        Downloads osm-data
        The osm-data to be downloaded are defined by a geojson-file. The data is downloaded and the reference to the correct osm-files is stored.

        Args:
            path (pathlib.Path): The path to the geojson-file.

        Returns:
            bool: True on success, False otherwise
        """
        pass
