from __future__ import annotations

import os

from src.osm_configurator.model.project.project_io_handler import ProjectIOHandler
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class ProjectSettings:
    """
    This class saves all the different settings of a project and provides methods to view and change them.
    """

    def __init__(self, location: Path, project_name: str, description: str, calculation_phase_checkpoints_folder: str):
        """
        This method creates a new ProjectSettings class with the given settings.

        Args:
            location (pathlib.Path): The location, the project is stored
            project_name (str): The name of the project
            description (str): A description of the project
            calculation_phase_checkpoints_folder(str): The name of the folder for calculation checkpoints
        """
        self._path: Path = location
        self._name: str = project_name
        self._description: str = description
        self._calculation_phase_checkpoints_folder: str = calculation_phase_checkpoints_folder
        self._last_edit_date: str = ""

    def get_location(self) -> Path:
        """
        Getter for the location of the Project on the disk.

        Returns:
            pathlib.Path: The location of the project
        """
        return self._path

    def set_location(self, new_location: Path) -> bool:
        """
        This method loads the location where the project will be stored.

        Args:
            new_location (pathlib.Path): The location for the project.

        Returns:
            bool: true, if location change was successful, false else.
        """
        if os.path.exists(new_location):
            self._path = new_location
            return True
        return False

    def change_location(self, new_location: Path) -> bool:
        """
        This method changes the location where the project will be stored.

        Args:
            new_location (pathlib.Path): The new location for the project.

        Returns:
            bool: true, if location change was successful, false else.
        """
        if os.path.exists(new_location):
            save_path = self._path
            self._path = new_location.joinpath(self._name)
            if not os.path.exists(self._path):
                os.makedirs(self._path)
                config_directory: Path = self._path.joinpath("configuration")
                os.makedirs(config_directory)
                os.makedirs(config_directory.joinpath("categories"))
                os.makedirs(self._path.joinpath(self._calculation_phase_checkpoints_folder))
                return True
            else:
                self._path = save_path
        return False

    def get_name(self) -> str:
        """
        This method returns the name of the project.

        Returns:
            str: name of the project.
        """
        return self._name

    def set_name(self, new_name: str) -> bool:
        """
        This method loads the name of the project.

        Args:
            new_name (str): The new name of the project.

        Returns:
            bool: true if change was successful, false else.
        """
        if isinstance(new_name, str):
            self._name = new_name
            return True
        return False

    def change_name(self, new_name: str) -> bool:
        """
        This method changes the name of the project.

        Args:
            new_name (str): The new name of the project.

        Returns:
            bool: true if change was successful, false else.
        """
        if isinstance(new_name, str):
            _new_path: str = str(self._path).replace(self._name, new_name)
            if not os.path.exists(Path(_new_path)):
                os.rename(self._path, _new_path)
                self._path = Path(_new_path)
                self._name = new_name
                return True
        return False

    def get_description(self) -> str:
        """
        This method returns the description of the project.

        Returns:
            str: The description of the project
        """
        return self._description

    def set_description(self, new_description: str) -> bool:
        """
        This method changes the description of the project.

        Args:
            new_description (str): The new description of the project

        Returns:
            bool: true if change successful, false else
        """
        if isinstance(new_description, str):
            self._description = new_description
            return True
        return False

    def get_calculation_phase_checkpoints_folder(self) -> str:
        """
        This method is used to get the name of the folder in which the results will be saved.

        Returns:
            str: the name of the folder
        """
        return self._calculation_phase_checkpoints_folder

    def set_calculation_phase_checkpoints_folder(self, new_folder_name: str) -> bool:
        """
        This method is used to set the name of the folder in which the results will be saved.

        Args:
            new_folder_name (str): The name of the folder.

        Returns:
            bool: true if change successful, false else
        """
        if isinstance(new_folder_name, str):
            self._calculation_phase_checkpoints_folder = new_folder_name
            return True
        return False

    def change_calculation_phase_checkpoints_folder(self, new_folder_name: str) -> bool:
        """
        This method is used to change the name of the folder in which the results will be saved.

        Args:
            new_folder_name (str): The name of the folder.

        Returns:
            bool: true if change successful, false else.
        """
        if isinstance(new_folder_name, str):
            old_path: Path = self._path.joinpath(self._calculation_phase_checkpoints_folder)
            new_path: Path = self._path.joinpath(new_folder_name)
            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                self._calculation_phase_checkpoints_folder = new_folder_name
                return True
            return True
        return False

    def get_last_edit_date(self) -> str:
        """
        This method return the last edit of the project.

        Return:
            str: The date.
        """
        return self._last_edit_date

    def set_last_edit_date(self, date: str):
        """
        This method sets the last edit of the project.

        Args:
            The date.
        """
        self._last_edit_date = date
