from __future__ import annotations

from src.osm_configurator.model.parser.cut_out_parser_interface import CutOutParserInterface
import src.osm_configurator.model.parser.dataframe_column_names as dataframe_column_names

import geopandas as gpd
import os

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geopandas import GeoDataFrame


class CutOutParser(CutOutParserInterface):
    __doc__ = CutOutParserInterface.__doc__

    def __int__(self):
        """
        Creates a new instance of the CutOutParser.
        """
        pass

    def parse_cutout_file(self, path) -> GeoDataFrame:
        df = gpd.read_file(path)
        if dataframe_column_names.TRAFFIC_CELL_NAME not in df.columns:
            df[dataframe_column_names.TRAFFIC_CELL_NAME] = "traffic_cell_" + str(df.index)

        return df
