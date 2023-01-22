from __future__ import annotations

import geopandas as gpd

import osm_configurator.model.parser.osm_data_handler as osm_data_handler
from src.osm_configurator.model.parser.osm_data_parser_interface import OSMDataParserInterface

import src.osm_configurator.model.project.configuration.cut_out_mode_enum as cut_out_mode_enum
import src.osm_configurator.model.parser.cut_out_parser as cut_out_parser
import src.osm_configurator.model.parser.dataframe_column_names as dataframe_column_names

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from osm_configurator.model.parser.osm_data_handler import DataOSMHandler
    from geopandas import GeoDataFrame
    from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode
    from pathlib import Path


class OSMDataParser(OSMDataParserInterface):
    __doc__ = OSMDataParserInterface.__doc__

    def __init__(self):
        """
        Creates a new instance of the CategoryParser.
        """
        pass

    def parse_osm_data_file(self, data_file_path: Path, categories: CategoryManager,
                            cut_out_mode_p: CutOutMode, cut_out_path: Path) -> GeoDataFrame:

        # Creating our osm_handler which converts the osm-data file into a list of data
        # depending on if we want building on edges removed we initialize the object differently
        osm_handler: DataOSMHandler
        if cut_out_mode_p == cut_out_mode_enum.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED:
            # get the name of the file without the suffix
            current_traffic_cell_name: str = data_file_path.stem

            # create a new cutout parser and parse the cutout file
            cut_out_parser_o = cut_out_parser.CutOutParser()
            cut_out_data: GeoDataFrame = cut_out_parser_o.parse_cutout_file(cut_out_path)

            # get the entry in tha dataframe which corresponds to the file we are currently working on
            # get the index the file references, naming scheme: "index_name"
            idx: int = int(current_traffic_cell_name.split("_")[0])

            osm_handler = osm_data_handler.DataOSMHandler(categories,
                                                          cut_out_data[dataframe_column_names.GEOMETRY].loc[idx])

        elif cut_out_mode_p == cut_out_mode_enum.CutOutMode.BUILDINGS_ON_EDGE_ACCEPTED:
            osm_handler = osm_data_handler.DataOSMHandler(categories)

        else:
            pass
            # TODO: throw error here?

        # Process the data
        osm_handler.apply_file(data_file_path.resolve())

        # transform the data from osm_handler into  geoDataFrame
        # TODO: not final, check what we need to save
        data_col_names = [dataframe_column_names.OSM_TYPE,
                          dataframe_column_names.LOCATION,
                          dataframe_column_names.TAGS,
                          dataframe_column_names.CATEGORIES]

        df_osm = gpd.GeoDataFrame(osm_handler.get_osm_data(), columns=data_col_names)

        return df_osm
