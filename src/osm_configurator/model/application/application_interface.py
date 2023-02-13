from __future__ import annotations

import src.osm_configurator.model.application.recommender_system
import src.osm_configurator.model.project.active_project
import src.osm_configurator.model.application.application_settings
import src.osm_configurator.model.application.passive_project

from abc import ABC, abstractmethod
from pathlib import Path

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.osm_configurator.model.application.passive_project import PassiveProject
    from src.osm_configurator.model.application.recommender_system import RecommenderSystem
    from src.osm_configurator.model.project.active_project import ActiveProject
    from src.osm_configurator.model.application.application_settings import ApplicationSettings


class IApplication(ABC):
    """
    The IApplication job, is to provide the functionality the application needs.
    """

    @abstractmethod
    def create_project(self, name, description, destination) -> bool:
        """
        This method creates a new project with a name, a description and saves it at a given destination.

        Args:
            name (str): The name of the new project.
            description (str): The description of the new project.
            destination (pathlib.Path): The path, where the new project should be saved.

        Returns:
            bool: True if create_project completed successfully, otherwise false.
        """
        pass

    @abstractmethod
    def load_project(self, destination: Path) -> bool:
        """
        This method loads an existing project. This project can be internal or external ones. The path is pointing
        towards the folder, where the project is saved.

        Args:
            destination (pathlib.Path): The path of the project, to be loaded.
        Returns:
            bool: True if loading the project is working, otherwise false.
        """
        pass

    @abstractmethod
    def get_passive_project_list(self) -> List[PassiveProject]:
        """
        Returns the list of all passive project in the current project default folder.

        Returns:
            List[passive_project.PassiveProject]: The list of the passive projects.
        """
        pass

    @abstractmethod
    def get_key_recommendation_system(self) -> RecommenderSystem:
        """
        Returns the Key Recommendation system.

        Returns:
            recommender_system.RecommenderSystem: The key recommender system.
        """
        pass

    @abstractmethod
    def get_active_project(self) -> ActiveProject:
        """
        Returns the currently active project.

        Returns:
            active_project.ActiveProject: The active project.
        """
        pass

    @abstractmethod
    def get_application_settings(self) -> ApplicationSettings:
        """
        Returns the settings of the application.

        Returns:
            application_settings.ApplicationSettings: The settings of the application.
        """
        pass

    @abstractmethod
    def save(self):
        """
        Saves the active Project and the application settings to the drive.
        """
        pass

    @abstractmethod
    def _create_passive_project_list(self, destination: Path) -> List[PassiveProject]:
        """
        Creates the list of passive projects.

        Args:
            destination (pathlib.Path): The path where the projects are stored.

        Returns:
            list[passive_project.PassiveProject]: The list of passive projects.
        """
        pass
