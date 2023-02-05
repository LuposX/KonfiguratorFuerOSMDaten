from __future__ import annotations

import os.path

import src.osm_configurator.model.model_constants as model_constants_i
import matplotlib

import geopandas as gpd

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

    def create_map(self, cut_out_config: CutOutConfiguration, map_saving_path: Path, filename: str):
        """
        This method to create a map from to given cut-out.

        Args:
            cut_out_config (cut_out_configuration.CutOutConfiguration): The cut-out configuration from which the map should be created.
            map_saving_path (Path): the path where we want to save the file, doesn't include filename.
            filename (str): the name under which the file should be saved, need t ohave the ".html" extension.

        Returns:
            bool: True if creating the map works, otherwise false.
        """
        # Get the cut out file
        cut_out_file: Path = cut_out_config.get_cut_out_path()

        # read in the cut_out file
        gdf: GeoDataFrame = gpd.read_file(cut_out_file)

        #get the area to visualize it
        gdf[model_constants_i.CL_AREA] = gdf.area

        # save the map
        map: Map = gdf.explode(model_constants_i.CL_AREA, legend=False)

        try:
            map.save(os.path.join(map_saving_path, filename))
        except Exception:
            return False

        return True

    def create_boxplot(self, data: DataFrame, map_saving_path: Path, filename: str):
        """
        This method creates a boxplot which can later be viewed.

        Args:
            data (DataFrame): The data which we want to visualize, should come from the aggregation phase.
            map_saving_path (Path): the path where we want to save the file, doesn't include filename.
            filename (str): the name under which the file should be saved, need to have the ".png" extension.

        Returns:
            bool: True if creating the boxplot works, otherwise false.
        """
        fig = sb.boxplot(data)
        fig.get_figure().savefig(os.path.join(map_saving_path, filename))
