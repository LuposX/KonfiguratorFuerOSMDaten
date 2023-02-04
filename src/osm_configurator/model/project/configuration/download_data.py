from __future__ import annotations
from typing import TYPE_CHECKING

import osmnx as ox
import geopandas as gpd

if TYPE_CHECKING:
    from shapely import Polygon


class DownloadData:
    """
    This class manages the download of OSM data depending on a list of coordinates.
    """

    def __init__(self):
        """
        Creates a new instance of the DownloadData.
        """

    def download_data(self, coordinates: Polygon) -> bool:
        """
        Downloads the OSM data which the coordinates dictate.

        Args:
            coordinates (shapely.Polygon): The new area, which should be downloaded

        Returns:
            bool: True when the download works, otherwise false.
        """
        return True
