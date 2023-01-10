class OSMDataConfiguration:

    """
    The job of the OSMDataConfiguration is to store the path pointing towards the OSM data.
    """

    def __init__(self):
        """
        Creates a new instance of the OSMDataConfiguration.
        """
        pass

    def get_osm_data(self):
        """
        Gives back the path pointing towards the OSM data as a GeoDataFrame.

        Returns:
            pathlib.Path: The path pointing towards the OSM data.
        """
        pass

    def set_osm_data(self, osm_data):
        """
        Edits the path pointing towards the OSM data as a GeoDataFrame.

        Args:
            osm_data (pathlib.Path): The new path:

        Returns:
            bool: True if changing the path works, otherwise false.
        """
        pass