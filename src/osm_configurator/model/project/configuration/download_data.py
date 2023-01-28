from __future__ import annotations

import osmnx as ox
import geopandas as gpd


class DownloadData:
    """
    This class manages the download of OSM data depending on a list of coordinates.
    """

    def __init__(self):
        """
        Creates a new instance of the DownloadData.
        """
        self.df = gpd.read_file("../../data/partOfKarlsruhe.geojson")

    def download_data(self, coordinates):
        """
        Downloads the OSM data which the coordinates dictate.

        Args:
            coordinates (shapely.Polygon): The new area, which should be downloaded

        Returns:
            bool: True when the download works, otherwise false.
        """
        karl = ox.geometries_from_polygon(self.df["geometry"][0], tags={"building": True})
        return True
