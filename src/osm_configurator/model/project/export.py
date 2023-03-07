from __future__ import annotations

import os.path
import pathlib
from pathlib import Path
import shutil
import src.osm_configurator.model.project.active_project
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.active_project import ActiveProject
    from pathlib import Path

ZIP: str = "zip"
CONFIGURATION: str = "configuration"
RESULTS: str = "results"


def _path_with_zip_to_str(path: Path) -> str:
    """
    This method converts a path to a str and removes the ".zip" ending.

    Args:
        path: (Path): The path which should be edited.

    Returns:
        str: The name of the zip.
    """
    string_version_of_path: str = str(path)
    if string_version_of_path[-4:] == ".zip":
        return string_version_of_path[:-4]

    return string_version_of_path


class Export:
    """
    This class provides different export features based on the current project.
    Whereby exporting means, saving data from the currently active project somewhere else on the system on the disk.
    """

    def __init__(self, active_project: ActiveProject):
        """
        Creates a new instance of the "Export" class.

        Args:
            active_project (active_project.ActiveProject): The project to make exports from
        """
        self._active_project = active_project

    def export_project(self, path: Path):
        """
        Exports the whole project to the given path.

        Args:
            path (pathlib.Path): The path where the project shall be exported to with the name of the zip included.

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        zip_file_name: str = _path_with_zip_to_str(path)
        self._active_project.get_project_saver().save_project()
        try:
            shutil.make_archive(zip_file_name, ZIP, self._active_project.get_project_settings().get_location())
            return True
        except OSError:
            return False

    def export_configuration(self, path: Path) -> bool:
        """
        Exports the configuration to the given path. More specific, exports all the categories and their configurations,
        to the given path.

        Args:
            path (pathlib.Path): The path where the configurations shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        try:
            zip_file_name: str = _path_with_zip_to_str(path)
            shutil.make_archive(zip_file_name, ZIP,
                                os.path.join(self._active_project.get_project_settings().get_location(), CONFIGURATION))
            return True
        except OSError:
            return False

    def export_calculation(self, path: Path) -> bool:
        """
        Exports the results of the calculation to the given path.
        Whereby the calculation are a folder with all the different results from each
        calculation step in it.

        Args:
            path (Path): The path where the results of the calculation shall be exported to with the name
                of the zip included.

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        try:
            zip_file_name: str = _path_with_zip_to_str(path)
            shutil.make_archive(
                zip_file_name,
                ZIP,
                os.path.join(self._active_project.get_project_settings().get_location(), RESULTS)
            )
            return True
        except OSError:
            return False

    def export_map(self, path: Path) -> bool:
        """
        Exports an HTML-Data with the map in it, to the given path.

        Args:
            path (Path): The path, where the map shall be exported to

        Returns:
            bool: true, if export was successful, otherwise false.
        """
        zip_file_name: str = _path_with_zip_to_str(path)
        directory, filename = os.path.split(zip_file_name)
        return self._active_project.get_data_visualizer().create_map(self._active_project.get_config_manager()
                                                                     .get_cut_out_configuration().get_cut_out_path(), Path(directory), filename + ".html")

 
