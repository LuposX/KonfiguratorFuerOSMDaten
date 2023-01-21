from __future__ import annotations

import subprocess
import os
import shapely
import pathlib
import subprocess
import shapely.geometry
import geopandas as gpd


class SplitUpFile:
    """
    This class is responsible to split up osm-data files, into multiple smaller osm-data files.
    This is useful since an osm-data file loaded into the ram can be bigger than the capacity of the RAM.
    """

    def __init__(self, origin_path, result_folder):
        """
        Creates a new instance of "SplitUpFile".

        Args:
            origin_path (pathlib.Path): The path pointing towards the osm_data file we want to split.
            result_folder (pathlib.Path): The path pointing towards the folder, where we want the split up files to land
        """
        self.origin_path = origin_path
        self.result_folder = result_folder

    def split_up_files(self, coordinates):
        """
        This method splits up the file into multiple smaller ones based on the coordinates it receives.

        Args:
            coordinates (List[geopandas.geoseries.GeoSeries]): A list of polygon. Each polygon ist the bounding box of one traffic cell we want to split up.

        Returns:
            bool: True if successful, otherwise false.
        """

        if not os.path.exists(self.origin_path) or not os.path.exists(self.result_folder):
            return False

        for i in range(len(coordinates)):
            result = subprocess.run(["osmium", "extract", "-b", "{},{},{},{}".format(*coordinates[i].bounds),
                                     str(self.origin_path), "-o", str(self.result_folder) + "/" + str(i) + ".pbf"],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                return False
        return True
