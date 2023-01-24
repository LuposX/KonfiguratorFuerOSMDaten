from __future__ import annotations

import shapely


class DownloadData:
    """
    This class manages the download of OSM data depending on a list of coordinates.
    """

    def __init__(self):
        """
        Creates a new instance of the DownloadData.
        """
        pass

    def download_data(self, coordinates):
        """
        Downloads the OSM data which the coordinates dictate.

        Args:
            coordinates (shapely.Polygon): The new area, which should be downloaded

        Returns:
            bool: True when the download works, otherwise false.
        """
        pass
