from __future__ import annotations

import subprocess
import os
import shapely
from pathlib import Path
import subprocess
from geopandas.geodataframe import GeoDataFrame
from src.osm_configurator.model.parser import dataframe_column_names
import src.osm_configurator.model.project.calculation.osm_file_format_enum as osm_file_format_enum


class SplitUpFile:
    """
    This class is responsible to split up osm-data files, into multiple smaller osm-data files.
    This is useful since an osm-data file loaded into the ram can be bigger than the capacity of the RAM.
    """

    def __init__(self, origin_path: Path, result_folder: Path):
        """
        Creates a new instance of "SplitUpFile".

        Args:
            origin_path (pathlib.Path): The path pointing towards the osm_data file we want to split.
            result_folder (pathlib.Path): The path pointing towards the folder, where we want the split up files to land
        """
        self._origin_path: Path = origin_path
        self._result_folder: Path = result_folder

    def split_up_files(self, cells: GeoDataFrame) -> bool:
        """
        This method splits up the file into multiple smaller ones based on the coordinates it receives.
        The split up is based on a DataFrame. The dataframe must contain a row for each splitting. It must have the
        column geometry, which contains a GeoSeries and a column name, which contains the name of the file of the
        split up.

        Args:
            cells (GeoDataFrame): The above-mentioned data frame

        Returns:
            bool: True if successful, otherwise false.
        """

        if not os.path.exists(self._origin_path) or not os.path.exists(self._result_folder):
            return False

        if dataframe_column_names.TRAFFIC_CELL_NAME not in cells.columns:
            return False

        for i in range(len(cells[dataframe_column_names.GEOMETRY])):
            result = subprocess.run(["osmium", "extract", "-b", "{},{},{},{}".format(*cells[
                dataframe_column_names.GEOMETRY][i].bounds),
                                     str(self._origin_path), "-o",
                                     str(self._result_folder) + "/" +
                                     str(cells[dataframe_column_names.TRAFFIC_CELL_NAME][i])
                                     + osm_file_format_enum.OSMFileFormat.PBF.get_file_extension()],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                return False
        return True
