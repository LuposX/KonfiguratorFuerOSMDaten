from __future__ import annotations

import pathlib

from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication
    from src.osm_configurator.model.application.passive_project import PassiveProject
    from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
    from pathlib import Path

class IProjectController(ABC):
    """
    The ProjectController is responsible for consistently forwarding requests regarding the project management
    to the model.
    It is responsible for managing, saving, loading, deleting and creating projects.
    """

    @abstractmethod
    def get_list_of_passive_projects(self) -> list[PassiveProject]:
        """
        Returns the list of (passive) projects, which are in the default project folder of the application.

        Returns:
            list[passive_project.PassiveProject]: The list of passive projects in the default project folder.
        """
        pass

    @abstractmethod
    def load_project(self, path: pathlib.Path) -> bool:
        """
        Loads a project
        All relevant data of a project are verified and loaded in memory. All coming project-referring calls will be directed to the given project.

        Args:
            path (pathlib.Path): The path to the project folder of the project, to be loaded.

        Returns:
            bool: True, if the project was loaded successfully; False if an error occurred, while trying to load the project. An error happens, if the path is not pointing to a valid project folder or if the project has corrupted files.
        """
        pass

    @abstractmethod
    def create_project(self, name: str, description: str, destination: pathlib.Path) -> bool:
        """
        Creates a new project with the given attributes and loads it.
        The model creates a new project folder at the given destination, all relevant files are generated and the project is loaded into memory.

        Args:
            name (str): The name of the to-be-created project, may not contain any line-breaks.
            description (str): The description of the to-be-created project. May contain line-breaks.
            destination (pathlib.Path): The path to the location, where the project-folder of the project should be created.

        Returns:
            bool: True, if the project was created successfully; False if an error occurred. An error occurs, if the name of the project is not valid, if the destination-path is not valid or if the destination-location is already occupied.
        """
        pass

    @abstractmethod
    def save_project(self) -> bool:
        """
        Saves the project.
        The currently selected project is stored on the disk. All progress made since the last saving are saved.

        Returns:
            bool: True, if the project was saved successfully; False if an error occurred, while attempting to save the project or when there is no project selected.
        """
        pass

    @abstractmethod
    def set_current_config_phase(self, config_phase: ConfigPhase) -> bool:
        """
        Stores the current configuration phase in the model.

        Args:
            config_phase (config_phase_enum.ConfigPhase): The new configuration phase.

        Returns:
            bool: True, if setting the configuration phase was successful; False, otherwise.
        """
        pass

    @abstractmethod
    def get_current_config_phase(self) -> ConfigPhase:
        """
        Returns the configuration phase, that is currently stored in the model.

        Returns:
            config_phase_enum.ConfigPhase: The configuration phase, that is currently stored in the model.
        """
        pass

    @abstractmethod
    def unload_project(self):
        """
        This method is to set the active_project to None, which is used when getting into the Main Menu.
        """
        pass

    @abstractmethod
    def is_project_loaded(self) -> bool:
        """
        Checks, whether any project is currently loaded/selected.

        Returns:
            bool: True, if a project is currently selected; False, otherwise.
        """
        pass

    @abstractmethod
    def get_project_path(self) -> Path:
        """
        Gets the path to the current project.

        Returns:
            Path: to the current project.
        """
        pass

    @abstractmethod
    def get_default_project_folder(self) -> Path:
        """
        Returns the default project folder defined by the application settings.

        Returns:
            The Folder.
        """
        pass