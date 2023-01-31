from __future__ import annotations

import os
import pathlib


class ProjectSettings:
    """
    This class saves all the different settings of a project and provides methods to view and change them.
    """

    def __init__(self, location, project_name, description, calculation_phase_checkpoints_folder):
        """
        This method creates a new ProjectSettings class with the given settings.

        Args:
            location (pathlib.Path): The location, the project is stored
            project_name (str): The name of the project
            description (str): A description of the project
            calculation_phase_checkpoints_folder(str): The name of the folder for calculation checkpoints
        """
        self._path: pathlib.Path = location
        self._name: str = project_name
        self._description: str = description
        self._calculation_phase_checkpoints_folder: str = calculation_phase_checkpoints_folder

    def get_location(self) -> pathlib.Path:
        """
        Getter for the location of the Project on the disk.

        Returns:
            pathlib.Path: The location of the project
        """
        return self._path

    def set_location(self, new_location: pathlib.Path) -> bool:
        """
        This method changes the location where the project will be stored.

        Args:
            new_location (pathlib.Path): The new location for the project

        Returns:
            bool: true, if location change was successful, false else
        """
        if os.path.exists(new_location):
            self._path = new_location
            return True
        return False

    def get_name(self) -> str:
        """
        This method returns the name of the project.

        Returns:
            str: name of the project
        """
        return self._name

    def set_name(self, new_name: str) -> bool:
        """
        This method changes the name of the project.

        Args:
            new_name (str): The new name of the project

        Returns:
            bool: true if change was successful, false else
        """
        if isinstance(new_name, str):
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

    def set_calculation_phase_checkpoints_folder(self, folder_name: str):
        """
        This method is used to set the name of the folder in which the results will be saved.

        Args:
            folder_name (str): the name of the folder
        """
        if isinstance(folder_name, str):
            self._calculation_phase_checkpoints_folder = folder_name
            return True
        return False
