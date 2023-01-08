class OSMDataController:
    """The OSMDataController is responsible for consistently forwarding requests regarding the OSM-data of the currently selected project.
    """

    def __init__(self, model):
        """Creates a new instance of the OSMDataController, with a association to the model.

        Args:
            model (IApplication): The interface which is used to communicate with the model.
        """
        pass

    def set_osm_data_reference(self, path):
        """Sets the reference to the osm-data for the selected project.
        The reference contains the osm-data used in the calculations of the project. This method does not check if the given data is valid.

        Args:
            path (Path): The reference to the osm-data

        Returns:
            bool: True, if the new reference was set successfully; False, if an error accured whie setting the reference.
        """
        pass

    def get_osm_data_reference(self):
        """Returns the path to the osm-data, that is used in the currently selected project.

        Returns:
            Path: The path to the osm-data of the currently selected project.
        """
        pass