from __future__ import annotations

import src.osm_configurator.model.application.application_interface
import pathlib


class OSMDataController:
    """
    The OSMDataController is responsible for consistently forwarding requests
    regarding the OSM-data of the currently selected project.
    """

    def __init__(self, model):
        """
        Creates a new instance of the OSMDataController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def set_osm_data_reference(self, path):
        """
        Sets the reference to the osm-data for the selected project.
        The reference contains the osm-data used in the calculations of the project. This method does not check if the given data is valid.

        Args:
            path (pathlib.Path): The reference to the osm-data.

        Returns:
            bool: True, if the new reference was set successfully; False, if an error occurred while setting the reference.
        """
        pass

    def get_osm_data_reference(self):
        """
        Returns the path to the osm-data, that is used in the currently selected project.

        Returns:
            pathlib.Path: The path to the osm-data of the currently selected project.
        """
        pass

    def download_osm_data(self, path):
        """
        Downloads osm-data
        The osm-data to be downloaded are defined by a geojson-file. The data is downloaded and the reference to the correct osm-files is stored.

        Args:
            path (pathlib.Path): The path to the geojson-file.

        Returns:
            bool: True on success, False otherwise
        """
        pass
