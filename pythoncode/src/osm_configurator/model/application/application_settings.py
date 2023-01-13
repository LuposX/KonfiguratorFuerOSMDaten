from pathlib import Path


class ApplicationSettings:
    """
    This class job is to manage the settings apart from the project settings. In those settings the default-location
    to save projects can be changed.
    """

    def __init__(self):
        """
        Creates a new instance of the ApplicationSettings.
        """
        pass

    def get_default_location(self):
        """
        Gives back the path pointing towards the project.

        Returns:
            pathlib.Path: Returns the path of the default location.
        """
        pass

    def set_default_location(self, new_location):
        """
        Sets the default path pointing towards the project to a new Location.

        Args:
            new_location (pathlib.Path): The new Location, where the user wants to save new projects.
        """
        pass
