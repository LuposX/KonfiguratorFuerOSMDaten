from __future__ import annotations

import geopandas as gpd

import osm_configurator.model.parser.osm_data_handler as osm_data_handler
from src.osm_configurator.model.parser.osm_data_parser_interface import OSMDataParserInterface

import osm_configurator.model.parser.dataframe_column_names as dataframe_column_names

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from osm_configurator.model.parser.osm_data_handler import DataOSMHandler
    from geopandas import GeoDataFrame


class OSMDataParser(OSMDataParserInterface):
    __doc__ = OSMDataParserInterface.__doc__

    def __init__(self):
        """
        Creates a new instance of the CategoryParser.
        """
        pass

    def parse_osm_data_file(self, path, categories: CategoryManager,
                            activated_attributes: List[Attribute], building_on_the_edge: bool) -> GeoDataFrame:
        """
        This method also implements the functionality when building are on the edge.
        """
        # Creating our osm_handler which converts the osm-data file into a list of data
        osm_handler: DataOSMHandler = osm_data_handler.DataOSMHandler(categories,
                                                                      activated_attributes,
                                                                      building_on_the_edge)

        # Process the data
        osm_handler.apply_file(path, locations=True)

        # transform the data from osm_handler into  geoDataFrame
        # TODO: not final, check what we need to save
        data_col_names = [dataframe_column_names.OSM_TYPE,
                          dataframe_column_names.LOCATION,
                          dataframe_column_names.TAGS,
                          dataframe_column_names.CATEGORIES]

        df_osm = gpd.GeoDataFrame(osm_handler.get_osm_data(), columns=data_col_names)

        return df_osm


