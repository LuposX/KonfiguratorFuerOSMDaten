from __future__ import annotations

import os
import sys
import shutil
from pathlib import Path
import subprocess
from geopandas.geodataframe import GeoDataFrame
import src.osm_configurator.model.model_constants as model_constants
import src.osm_configurator.model.project.calculation.osm_file_format_enum as osm_file_format_enum



OSMIUM_STARTING_ARGS_NOT_FROZEN_VIA_CONDA: list = ["osmium", "extract", "-b"]
OSMIUM_STARTING_ARGS_NOT_FROZEN_VIA_BINARY: list = ["../../data/osmium/osmium.exe", "extract", "-b"]
OSMIUM_STARTING_ARGS_FROZEN: list = ["data/osmium/osmium.exe", "extract", "-b"]

OSMIUM_COORDINATE_PATTERN: str = "{},{},{},{}"
OSMIUM_O_OPTION: str = "-o"


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

        if model_constants.CL_TRAFFIC_CELL_NAME not in cells.columns:
            return False

        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        # noinspection PyProtectedMember
        # pylint: disable=protected-access
        is_frozen: bool = False
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # check that we are on windows
            if not hasattr(sys, 'getwindowsversion'):
                raise OSError("We don't support the Operating System you use!")

            is_frozen = True

        # Split up the files
        for i in range(len(cells[model_constants.CL_GEOMETRY])):
            child = subprocess.Popen(self.get_osmium_command_args(cells, i),
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            streamdata = child.communicate()[0]
            if child.returncode != 0:
                return False
        return True

    def get_osmium_command_args(self, is_frozen: bool, cells: GeoDataFrame, i: int) -> list:
        if is_frozen:
            args = list(OSMIUM_STARTING_ARGS_FROZEN)

        else:
            # Check if we have the program installed e.g. via conda.
            if shutil.which("osmium") is not None:
                args = list(OSMIUM_STARTING_ARGS_NOT_FROZEN_VIA_CONDA)

            # Try to use the bundled binaries.
            else:
                if not hasattr(sys, 'getwindowsversion'):
                    raise OSError("We don't support the Operating System you use!")

                args = list(OSMIUM_STARTING_ARGS_NOT_FROZEN_VIA_BINARY)

        # Calculates the arguments for the osmium tool, that split the OSM-file up correctly
        args.append(OSMIUM_COORDINATE_PATTERN.format(*cells[model_constants.CL_GEOMETRY][i].bounds))
        args.append(str(self._origin_path))
        args.append(OSMIUM_O_OPTION)
        args.append(str(self._result_folder) + "/" + str(cells[model_constants.CL_TRAFFIC_CELL_NAME][i])
                    + osm_file_format_enum.OSMFileFormat.PBF.get_file_extension())
        return args
