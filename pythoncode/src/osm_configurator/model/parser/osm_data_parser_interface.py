from __future__ import annotations

import pathlib
import geopandas

from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute


class OSMDataParserInterface(ABC):
    """
    The OSMDataParser job is to parse the OSMData into a human-readable format.
    This human-readable format is a GeoDataFrame from GeoPandas.
    """
    
    @abstractmethod
    def parse_osm_data_file(self, path, category_manager_o: CategoryManager, activated_attributes: List[Attribute]):
        """
        It gets a path pointing towards an OSM data in protocol buffer Binary Format(pbf) and transforms it into an
        GeoDataFrame.
        Each row in the GeoDataFrame is a single data entry, which is an osm element from the read osm data.
        Each column in the GeoDataFrame is a feature of the osm element from the osm_data, such as the location of the
        osm element, whereby a feature is a tag or something otherwise that describes the osm-element e.g. location.

        Args:
            path (pathlib.Path):  The path pointing towards the OSM data we want to parse in the ".pbf" format.
            activated_attributes (List[Attribute]): A list of attributes tha are activated and will be used in the calculation.
            category_manager_o (CategoryManager): The CategoryManager, used to figure out which categories apply to an osm element.
        
        Returns:
            geopandas.GeoDataFrame: The parsed OSM data as a GeoDataFrame.
        """
        pass

