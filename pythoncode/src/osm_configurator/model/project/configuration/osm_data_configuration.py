import pathlib


class OSMDataConfiguration:
    """
    The job of the OSMDataConfiguration is to store the path pointing towards the OSM data file.
    """

    def __init__(self):
        """
        Creates a new instance of the "OSMDataConfiguration" class.
        """
        pass

    def get_osm_data(self):
        """
        Gives back the path pointing towards the OSM data file.

        Returns:
            pathlib.Path: The path pointing towards the OSM data.
        """
        pass

    def set_osm_data(self, osm_data):
        """
        Edits the path pointing towards the OSM data file.

        Args:
            osm_data (pathlib.Path): The new path towards the osm data file.

        Returns:
            bool: True if changing the path works, otherwise false.
        """
        pass

    def download_data(self, coordinates):
        """
        Downloads the OSM data which the coordinates dictate.

        Args:
            coordinates (shapely.Polygon): The new area, which should be downloaded

        Returns:
            bool: True when the download works, otherwise false.
        """
        pass
