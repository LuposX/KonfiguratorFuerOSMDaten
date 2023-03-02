from __future__ import annotations

import os
import pathlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class OSMDataConfiguration:
    """
    The job of the OSMDataConfiguration is to store the path pointing towards the OSM data file.
    """

    def __init__(self):
        """
        Creates a new instance of the "OSMDataConfiguration" class.
        """
        self._osm_data_path: Path | None = None

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
