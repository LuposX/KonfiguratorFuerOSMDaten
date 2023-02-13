from __future__ import annotations

import os.path

import pandas as pd

import src.osm_configurator.model.model_constants as model_constants_i
import matplotlib

import geopandas as gpd
import webbrowser

import matplotlib.pyplot as plt
import seaborn as sb

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.cut_out_configuration import CutOutConfiguration
    from pathlib import Path
    from geopandas import GeoDataFrame
    from pandas import DataFrame
    from folium import Map


class DataVisualizer:
    """
    This class job is to visualize the cut-out file or data of the project.
    """

    def __init__(self):
        """
        Creates a new instance of the DataVisualizer.
        """
        pass

    def create_map(self, cut_out_file: Path, map_saving_path: Path, filename: str) -> bool:
        """
        This method is used to create a map from to given cut-out config and save it.

        Args:
            cut_out_file (Path): The cut-out file path.
            map_saving_path (Path): the path where we want to save the file, doesn't include filename.
            filename (str): the name under which the file should be saved, need t ohave the ".html" extension.

        Returns:
            bool: True if creating the map works, otherwise false.
        """
        try:
            gdf: GeoDataFrame = gpd.read_file(cut_out_file)
            # get the area to visualize it
            gdf[model_constants_i.CL_AREA] = gdf.area

            # save the map
            map: Map = gdf.explore(model_constants_i.CL_AREA, legend=False)
            map.save(os.path.join(map_saving_path, filename))

        # I use "Exception" here because seaborn nor matplotlib say on their documentation page which error they throw
        except Exception:
            return False

        return True

    def create_boxplot(self, data_path: Path, map_saving_path: Path, filename: str) -> bool:
        """
        This method creates a boxplot which is saved and can later be viewed.

        Args:
            data_path (Path): The path towards our data.
            map_saving_path (Path): the path where we want to save the file, doesn't include filename.
            filename (str): the name under which the file should be saved, need to have the ".png" extension.

        Returns:
            bool: True if creating the boxplot works, otherwise false.
        """
        # try saving the figure
        try:
            data: DataFrame = pd.read_csv(data_path)
            fig = sb.boxplot(data)
            fig.get_figure().savefig(os.path.join(map_saving_path, filename))

        # I use "Exception" here because seaborn nor matplotlib say on their documentation page which error they throw
        except Exception:
            return False

        return True

    def show_map(self, path_to_map: Path) -> bool:
        """
        This function is used to visualize am already created map.

         Args:
            path_to_map (Path): the path where the map is saved we want to show.

         Returns:
            bool: True if creating the boxplot works, otherwise false.
        """
        try:
            webbrowser.open_new(path_to_map)
        except Exception:
            return False

        return True

    def show_boxplot(self, path_to_map: Path) -> bool:
        """
        This function is used to visualize am already created boxplot.

         Args:
            path_to_map (Path): the path where the boxplot is saved we want to show.

         Returns:
            bool: True if creating the boxplot works, otherwise false.
        """
        try:
            webbrowser.open_new(path_to_map)
        except Exception:
            return False

        return True