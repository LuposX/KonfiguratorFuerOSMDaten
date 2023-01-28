from __future__ import annotations

import geopandas as gpd

import osm_configurator.model.parser.osm_data_handler as osm_data_handler
from src.osm_configurator.model.parser.osm_data_parser_interface import OSMDataParserInterface

import src.osm_configurator.model.project.configuration.cut_out_mode_enum as cut_out_mode_enum
import src.osm_configurator.model.parser.cut_out_parser as cut_out_parser
import src.osm_configurator.model.model_constants as model_constants

import src.osm_configurator.model.parser.custom_expceptions.osm_data_wrongly_formatted_Exception as osm_data_wrongly_formatted_i

from osm_configurator.model.parser.custom_expceptions.osm_data_wrongly_formatted_Exception import OSMDataWronglyFormatted

import src.osm_configurator.model.project.calculation.osm_file_format_enum as osm_file_format_enum_i

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
        if cut_out_mode_p == cut_out_mode_enum.CutOutMode.BUILDINGS_ON_EDGE_ACCEPTED:
            # get the name of the file without the suffix
            # current_traffic_cell_name: str = data_file_path.split("/")[-1]
            current_traffic_cell_name: str = data_file_path.stem

            if data_file_path.suffix not in [osm_file_format_enum_i.OSMFileFormat.OSM.get_file_extension(),
                                             osm_file_format_enum_i.OSMFileFormat.OSM.BZ2.get_file_extension(),
                                             osm_file_format_enum_i.OSMFileFormat.OSM.PBF.get_file_extension()]:
                raise OSMDataWronglyFormatted

            # create a new cutout parser and parse the cutout file
            cut_out_parser_o = cut_out_parser.CutOutParser()
            cut_out_data: GeoDataFrame = cut_out_parser_o.parse_cutout_file(cut_out_path)

            # get the entry in tha dataframe which corresponds to the file we are currently working on
            # get the index the file references, naming scheme: "index_name"
            idx = current_traffic_cell_name.split("_")
            if len(idx) == 0:
                raise OSMDataWronglyFormatted

            idx = int(idx[0])

            osm_handler = osm_data_handler.DataOSMHandler(categories,
                                                          cut_out_data[model_constants.CL_LOCATION].loc[idx])

        elif cut_out_mode_p == cut_out_mode_enum.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED:
            osm_handler = osm_data_handler.DataOSMHandler(categories)

        else:
            pass
            # TODO: throw error here?

        # Process the data
        osm_handler.apply_file(data_file_path)

        # transform the data from osm_handler into  geoDataFrame
        # TODO: not final, check what we need to save
        data_col_names = [model_constants.CL_OSM_TYPE,
                          model_constants.CL_OSM_ELEMENT_NAME,
                          model_constants.CL_LOCATION,
                          model_constants.CL_TAGS,
                          model_constants.CL_CATEGORIES]

        df_osm = gpd.GeoDataFrame(osm_handler.get_osm_data(), columns=data_col_names)

        return df_osm
