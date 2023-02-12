from __future__ import annotations

import os
import pathlib
from pathlib import Path

from typing import TYPE_CHECKING

import src.osm_configurator.model.project.configuration.download_data as download_data

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.download_data import DownloadData
    from pathlib import Path


class OSMDataConfiguration:
    """
    The job of the OSMDataConfiguration is to store the path pointing towards the OSM data file.
    """

    def __init__(self):
        """
        Creates a new instance of the "OSMDataConfiguration" class.
        """
        self._osm_data_path: Path = None
        self._downloader: DownloadData = download_data.DownloadData()

    def get_osm_data(self) -> Path:
        """
        Gives back the path pointing towards the OSM data file.

        Returns:
            pathlib.Path: The path pointing towards the OSM data.
        """
        return self._osm_data_path

    def set_osm_data(self, new_osm_data: Path) -> bool:
        """
        Edits the path pointing towards the OSM data file.

        Args:
            new_osm_data (pathlib.Path): The new path towards the osm data file.

        Returns:
            bool: True if changing the path works, otherwise false.
        """
        if os.path.exists(new_osm_data):
            self._osm_data_path = new_osm_data
            return True
        return False

    def get_download_data(self) -> DownloadData:
        """
        Getter for the download data class.

        Returns:
            download_data.DownloadData: The download data class.
        """
        return self._downloader
