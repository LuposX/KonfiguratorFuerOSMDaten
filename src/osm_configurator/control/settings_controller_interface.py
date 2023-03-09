from __future__ import annotations

import pathlib

from abc import ABC, abstractmethod


class ISettingsController(ABC):
    """
    The SettingsController is responsible for forwarding requests to the model,
    regarding the settings of the application and the currently selected project.
    """

    @abstractmethod
    def get_project_name(self) -> str:
        """
        Gets the name of the currently selected project.

        Returns:
            str: The name of the project.
        """
        pass

    @abstractmethod
    def set_project_name(self, name: str) -> bool:
        """
        Sets the name of the currently selected project.

        Args:
            name (str): The new name of the project, may not contain line breaks.

        Returns:
            bool: True, if the name was changed successfully; False, if an error occurred:
                The name is not valid or no project was selected.
        """
        pass

    @abstractmethod
    def get_project_description(self) -> str:
        """
        Gets the description of the currently selected project.

        Returns:
            str: The description of the project.
        """
        pass

    @abstractmethod
    def set_project_description(self, description: str) -> bool:
        """
        Sets the description of the currently selected project.

        Args:
            description (str): The new description of the project, may contain line breaks.

        Returns:
            bool: True, if the description was changed successfully; False, otherwise.
        """
        pass

    @abstractmethod
    def get_project_default_folder(self) -> pathlib.Path:
        """
        Gets the project default folder.
        The project default folder is the folder where projects are stored by default.

        Returns:
            pathlib.Path: The path to the project default folder.
        """
        pass

    @abstractmethod
    def set_project_default_folder(self, default_folder: pathlib.Path) -> bool:
        """
        Sets the project default folder.
        The project default folder is the folder, where projects are stored by default.
        Projects of an old default folder will not be copied over.

        Args:
            default_folder (pathlib.Path): The path to the new project default folder.

        Returns:
            bool: True, if the default folder was set successfully; False if an error occurred:
                The path is not valid or occupied.
        """
        pass

    @abstractmethod
    def get_number_of_processes(self) -> int:
        """
        Gets the number of processes that should be used via the calculation.

        Returns:
            int: The number of processes.
        """
        pass

    @abstractmethod
    def set_number_of_processes(self, number_of_processes: int) -> bool:
        """
        Sets the number of processes we want to use for our project.

        Args:
            number_of_processes (int): The number of processes we want to use.

        Returns:
            bool: True, if s set successfully; False if an error occurred.
        """
        pass

    @abstractmethod
    def get_number_of_key_recommendations(self) -> int:
        """
        Gets the number of key recommendations that can eb shown to the user.

        Returns:
            int: The number of key recommendations.
        """
        pass

    @abstractmethod
    def set_number_of_key_recommendations(self, number_of_processes: int) -> bool:
        """
        Sets the number of key recommendations that can eb shown to the user.

        Args:
            number_of_processes (int): The number of key recommendations

        Returns:
            bool: True, if set successfully; False if an error occurred.
        """
        pass
