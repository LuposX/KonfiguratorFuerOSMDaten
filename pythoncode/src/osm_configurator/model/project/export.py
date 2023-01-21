from __future__ import annotations

import pathlib
import src.osm_configurator.model.project


class Export:
    """
    This class provides different export features based on the current project.
    Whereby exporting means, saving data from the currently active project somewhere else on the system on the disk.
    """

    def __init__(self, project):
        """
        Creates a new instance of the "Export" class.

        Args:
            project (project.ActiveProject): The project to make exports from
        """
        pass

    def export_project(self, path):
        """
        Exports the whole project to the given path.

        Args:
            path (pathlib.Path): The path where the project shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        pass

    def export_configuration(self, path):
        """
        Exports the configuration to the given path. More specific, exports all the categories and their configurations,
        to the given path.

        Args:
            path (pathlib.Path): The path where the configurations shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        pass

    def export_calculation(self, path):
        """
        Exports the results of the calculation to the given path.
        Whereby the calculation are a folder with all the different results from each
        calculation step in it.

        Args:
            path (Path): The path where the results of the calculation shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        pass

    def export_map(self, path):
        """
        Exports an HTML-Data with the map in it, to the given path.

        Args:
            path (Path): The path, where the map shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        pass
