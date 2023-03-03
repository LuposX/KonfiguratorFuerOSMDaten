from __future__ import annotations

import os.path

import pandas as pd

import src.osm_configurator.model.model_constants as model_constants_i

import geopandas as gpd
import seaborn as sb
import glob
import pathlib

from typing import TYPE_CHECKING

import shutil

if TYPE_CHECKING:
    from pathlib import Path
    from geopandas import GeoDataFrame
    from folium import Map
    from typing import Final


TITLE_BOXPLOT: Final = "Attractivities of the Traffic Cells via Aggregation method: "
X_LABEL_BOXPLOT: Final = "Attractivities"
FILE_TYPE_TO_LOAD: Final = ".csv"
NAME_COLUMN_TO_DROP: Final = "traffic_cell_name"


class DataVisualizer:
    """
    This class job is to visualize the cut-out file or data of the project.
    """

    def __init__(self):
        """
        Creates a new instance of the DataVisualizer.
        """
        pass

    @staticmethod
    def create_map(cut_out_file: Path, map_saving_path: Path, filename: str) -> bool:
        """
        This method is used to create a map from to given cut-out config and save it.

        Args:
            cut_out_file (Path): The cut-out file path.
            map_saving_path (Path): the path where we want to save the file, doesn't include filename.
            filename (str): the name under which the file should be saved, need to have the ".html" extension.

        Returns:
            bool: True if creating the map works, otherwise false.
        """
        try:
            gdf: GeoDataFrame = gpd.read_file(cut_out_file)
            # get the area to visualize it
            gdf[model_constants_i.CL_AREA] = gdf.area

            # save the map
            cut_out_map: Map = gdf.explore(model_constants_i.CL_AREA, legend=False)
            cut_out_map.save(os.path.join(map_saving_path, filename))

        # I use "Exception" here because seaborn nor matplotlib say on their documentation page which error they throw
        except Exception:
            return False

        return True

    @staticmethod
    def create_boxplot(data_path: Path, boxplot_saving_path: Path) -> bool:
        """
        This method creates a boxplot which is saved and can later be viewed.

        Args:
            data_path (Path): The path towards our data.
            boxplot_saving_path (Path): the path where we want to save the file, doesn't include filename.

        Returns:
            bool: True if creating the boxplot works, otherwise false.
        """
        # create old folder if it exists.
        shutil.rmtree(boxplot_saving_path, ignore_errors=True)

        # create folder if it doesn't exist
        boxplot_saving_path.mkdir(parents=True, exist_ok=True)

        # try saving the figure
        for file in glob.glob(str(data_path) + "/*" + FILE_TYPE_TO_LOAD):
            try:
                data = pd.read_csv(file, index_col=[0])
            except OSError:
                return False

            file_name = pathlib.Path(file).stem
            data = data.drop([NAME_COLUMN_TO_DROP], axis=1)

            title = str(TITLE_BOXPLOT + file_name)
            ax = sb.boxplot(data=data)
            ax.set(xlabel=X_LABEL_BOXPLOT, title=title)

            try:
                ax.get_figure().savefig(os.path.join(str(boxplot_saving_path), file_name))
            except OSError:
                return False

        return True
