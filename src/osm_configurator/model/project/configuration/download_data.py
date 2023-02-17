from __future__ import annotations
from typing import TYPE_CHECKING

import pyrosm

if TYPE_CHECKING:
    from pathlib import Path


class DownloadData:
    """
    This class manages the download of OSM data depending on a list of coordinates.
    """

    def __init__(self):
        """
        Creates a new instance of the DownloadData.
        """

    @classmethod
    def download_data(cls, region_to_download: str, data_path: Path) -> bool:
        """
        Downloads the OSM data which the coordinates dictate.

        Args:
            region_to_download (str): The name of the region we want to download. (pyrosm.data.available) shows all available regions.
            data_path (Path): where to save the data
        Returns:
            bool: True when the download works, otherwise false.
        """
        try:
            pyrosm.get_data(region_to_download, data_path)

            return True

        except:
            return False

