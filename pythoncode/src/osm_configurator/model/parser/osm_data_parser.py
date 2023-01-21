from __future__ import annotations

import geopandas as gpd

import osm_configurator.model.parser.osm_data_handler as osm_data_handler
from src.osm_configurator.model.parser.osm_data_parser_interface import OSMDataParserInterface

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

    # TODO: wrong signature fix this
    def parse_osm_data_file(self, path, categories: CategoryManager, activated_attributes: List[Attribute]) -> GeoDataFrame:
        # Creating our osm_handler which converts the osm-data file into a list of data
        osm_handler: DataOSMHandler = osm_data_handler.DataOSMHandler(categories, activated_attributes)

        # Process the data
        osm_handler.apply_file(path.absolute())

        # transform the data from osm_handler into  geoDataFrame
        data_col_names = ['osm_type', 'ntags', 'tags', 'categories']
        df_osm = gpd.GeoDataFrame(osm_handler.get_osm_data(), columns=data_col_names)

        return df_osm


