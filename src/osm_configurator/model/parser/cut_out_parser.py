from __future__ import annotations

import fiona.errors

from src.osm_configurator.model.parser.cut_out_parser_interface import CutOutParserInterface

import src.osm_configurator.model.model_constants as model_constants_i

import src.osm_configurator.model.parser.custom_exceptions.illegal_cut_out_exception as illegal_cut_out_exception

from pathlib import Path

import geopandas as gpd

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geopandas import GeoDataFrame
    from typing import List
    from typing import Final


class CutOutParser(CutOutParserInterface):
    __doc__ = CutOutParserInterface.__doc__

    TRAFFIC_CELL_STANDARD_NAME: Final = "traffic_cell"

    def __int__(self):
        """
        Creates a new instance of the CutOutParser.
        """
        pass

    def parse_cutout_file(self, path: Path) -> GeoDataFrame:
        if not os.path.exists(path):
            raise illegal_cut_out_exception.IllegalCutOutException("Cut out file does not exist at the specified path.")

        try:
            df = gpd.read_file(path)
        except fiona.errors.DriverError as err:
            raise illegal_cut_out_exception.IllegalCutOutException("Could not load cut out file at the given path")

        # Create names for the traffic cells which don't have one and add idx before name
        # e.g. what function does "None" -> "0_traffic_cell" and "berlin_is_cool" -> "1_berlin_is_cool"
        traffic_cell_name_list: List = []
        if model_constants_i.CL_TRAFFIC_CELL_NAME in df.columns:
            for idx, row in df.iterrows():
                if row[model_constants_i.CL_TRAFFIC_CELL_NAME] is None:
                    traffic_cell_name_list.append(str(idx) + "_" + CutOutParser.TRAFFIC_CELL_STANDARD_NAME)
                else:
                    traffic_cell_name_list.append(str(idx) + "_" + str(row[model_constants_i.CL_TRAFFIC_CELL_NAME]))
        else:
            for idx, row in df.iterrows():
                traffic_cell_name_list.append(str(idx) + "_" + CutOutParser.TRAFFIC_CELL_STANDARD_NAME)

        df[model_constants_i.CL_TRAFFIC_CELL_NAME] = traffic_cell_name_list

        return df
