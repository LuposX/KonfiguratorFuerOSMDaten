from __future__ import annotations

import pathlib
import os
from typing import TYPE_CHECKING

from src.osm_configurator.model.application.application_interface import IApplication
from src.osm_configurator.model.application.application_settings import ApplicationSettings
from src.osm_configurator.model.application.application_settings_saver import ApplicationSettingsSaver
from src.osm_configurator.model.application.recommender_system import RecommenderSystem
from src.osm_configurator.model.application.passive_project import PassiveProject

if TYPE_CHECKING:
    from src.osm_configurator.model.application.passive_project import PassiveProject
    from src.osm_configurator.model.application.recommender_system import RecommenderSystem
    from src.osm_configurator.model.project.active_project import ActiveProject
    from src.osm_configurator.model.application.application_settings import ApplicationSettings
    from src.osm_configurator.model.application.application_settings_saver import ApplicationSettingsSaver
    from pathlib import Path


class Application(IApplication):
    __doc__ = IApplication.__doc__

    def __init__(self):
        """
        Creates a new instance of the application_interface.Application.
        """
        self.active_project: ActiveProject = None
        self.application_settings: ApplicationSettings = ApplicationSettings()
        self.passive_project_list: list[PassiveProject] = self._create_passive_project_list(
            self.application_settings.get_default_location())
        self.recommender_system: RecommenderSystem = RecommenderSystem()
        self.application_settings_saver: ApplicationSettingsSaver = ApplicationSettingsSaver()

    def create_project(self, name: str, description: str, destination: pathlib.Path) -> bool:
        self.active_project = ActiveProject(destination, True, name, description)
        return True

    def load_project(self, destination: pathlib.Path) -> bool:
        self.active_project = ActiveProject(destination, False)
        return True

    def get_passive_project_list(self) -> list[PassiveProject]:
        return self.passive_project_list

    def get_key_recommendation_system(self) -> RecommenderSystem:
        return self.recommender_system

    def get_active_project(self) -> ActiveProject:
        return self.active_project

    def get_application_settings(self) -> ApplicationSettings:
        return self.application_settings

    def save(self, destination: Path) -> bool:
        self.application_settings_saver.save_settings(destination)
        self.active_project.get_project_saver(destination)
        return True

    def _create_passive_project_list(self, destination: pathlib.Path) -> list[PassiveProject]:
        passive_project_list: list[PassiveProject] = []

        for files in os.walk(destination):
            for filename in files:
                if filename.endswith("settings.csv"):
                    filepath = os.path.join(destination, filename)
                    passive_project_list.append(PassiveProject(Path(filepath)))
        return passive_project_list
