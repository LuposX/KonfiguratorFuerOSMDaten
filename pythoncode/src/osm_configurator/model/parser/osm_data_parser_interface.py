from abc import ABC, abstractmethod
import pathlib
import geopandas


class OSMDataParserInterface(ABC):
    """
    The OSMDataParser job is to parse the OSMData into a human-readable format.
    This human-readable format is a GeoDataFrame from GeoPandas.
    """
    
    @abstractmethod
    def parse_osm_data_file(self, path):
        """
        It gets a path pointing towards an OSM data in protocol buffer Binary Format(pbf) and transforms it into an
        GeoDataFrame.
        Each row in the GeoDataFrame is a single data entry, which is an osm element from the read osm data.
        Each column in the GeoDataFrame is a feature of the osm element from the osm_data, such as the location of the
        osm element, whereby a feature is a tag or something otherwise that describes the osm-element e.g. location.

        Args:
            path (pathlib.Path):  The path pointing towards the OSM data we want to parse in the ".pbf" format.
        
        Returns:
            geopandas.GeoDataFrame: The parsed OSM data as a GeoDataFrame.
        """
        pass

