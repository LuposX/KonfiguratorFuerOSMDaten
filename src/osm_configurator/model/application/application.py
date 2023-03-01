from __future__ import annotations

from pathlib import Path
import os, sys
from typing import TYPE_CHECKING, List, Final

from src.osm_configurator.model.application.application_interface import IApplication
import src.osm_configurator.model.application.recommender_system as recommender_system_i
import src.osm_configurator.model.application.application_settings as application_settings_i
import src.osm_configurator.model.application.application_settings_default_enum as application_settings_enum_i
import src.osm_configurator.model.project.active_project as active_project_i
import src.osm_configurator.model.application.passive_project as passive_project_i

if TYPE_CHECKING:
    from src.osm_configurator.model.application.passive_project import PassiveProject
    from src.osm_configurator.model.application.recommender_system import RecommenderSystem
    from src.osm_configurator.model.project.active_project import ActiveProject
    from src.osm_configurator.model.application.application_settings import ApplicationSettings
    from pathlib import Path

PROJECT_SETTING: str = "project_settings.csv"


class Application(IApplication):
    __doc__ = IApplication.__doc__

    def __init__(self, path_to_starting_file: Path = None):
        """
        Creates a new instance of the application_interface.Application.

        Args:
            path_to_starting_file (Path): If set that directory will be used to create the application settings file.
        """
        self.active_project: ActiveProject = None

        # If path_to_starting_file is set we create the application settings file at that position.
        if path_to_starting_file is None:
            self.application_settings: ApplicationSettings = application_settings_i.ApplicationSettings()

        else:
            self.application_settings: ApplicationSettings = application_settings_i.ApplicationSettings(path_to_starting_file)

        self.passive_project_list: List[PassiveProject] = self._create_passive_project_list(
            self.application_settings.get_setting(
                application_settings_enum_i.ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER))

        self.recommender_system: RecommenderSystem = recommender_system_i.RecommenderSystem(self.application_settings)

    def create_project(self, name: str, description: str, destination: Path) -> bool:
        self.active_project = active_project_i.ActiveProject(destination, True, self.application_settings, name, description)
        return True

    def load_project(self, destination: Path) -> bool:
        self.active_project = active_project_i.ActiveProject(destination, False, self.application_settings)
        if self.active_project.project_directory is None:
            return False
        return True

    def get_passive_project_list(self) -> List[PassiveProject]:
        return self.passive_project_list

    def get_key_recommendation_system(self) -> RecommenderSystem:
        return self.recommender_system

    def get_active_project(self) -> ActiveProject:
        return self.active_project

    def get_application_settings(self) -> ApplicationSettings:
        return self.application_settings

    def _create_passive_project_list(self, destination: Path) -> List[PassiveProject] | None:
        passive_project_list: List[PassiveProject] = []

        if destination:
            for directory in os.listdir(destination):
                if not os.path.isfile(directory):
                    project: Path = Path(os.path.join(destination, Path(str(directory))))
                    filepath: Path = Path(os.path.join(project, PROJECT_SETTING))
                    if os.path.exists(filepath):
                        passive_project_list.append(passive_project_i.PassiveProject(filepath))
            return passive_project_list
        else:
            return []

    def delete_passive_project(self, passive_project: PassiveProject) -> bool:
        os.rmdir(passive_project.get_project_folder_path())
        self.passive_project_list.remove(passive_project)
        return True

    def unload_project(self):
        self.active_project = None
