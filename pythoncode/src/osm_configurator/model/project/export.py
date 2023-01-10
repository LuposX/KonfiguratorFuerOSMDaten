from pathlib import Path
import src.osm_configurator.model.project


class Export:
    """
    This class provides different export features based on a current project.
    """

    def __init__(self, project):
        """
        This method creates a new Export class which provides different export features based on the given project.

        Args:
            project (project.ActiveProject): The project to make exports from
        """
        pass

    def export_project(self, path):
        """
        Exports the whole project to the given path.

        Args:
            path (Path): The path where the project shall be exported to

        Returns:
            bool: true, if export was successful, false esle
        """
        pass

    def export_configuration(self, path):
        """
        Exports the configuration to the given path. More specific, exports all the categories and their configurations,
        to the given path.

        Args:
            path (Path): The path where the configurations shall be exported to

        Returns:
            bool: true, if export was successful, false else
        """
        pass

    def export_calculation(self, path):
        """
        Exports the results of the calculation to the given path.

        Args:
            path (Path): The path where the results of the calculation shall be exported to

        Returns:
            bool: true, if export was successful, false else
        """
        pass

    def export_map(self, path):
        """
        Exports an HTML-Data with the map in it, to the given path.

        Args:
            path (Path): The path, where the map shall be exported to

        Returns:
            bool: true, if export was successful, false else
        """
        pass
