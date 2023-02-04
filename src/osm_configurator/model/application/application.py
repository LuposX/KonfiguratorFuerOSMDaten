from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING

from src.osm_configurator.model.application.application_interface import IApplication

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
        self.active_project = ActiveProject
        self.passive_project_list = list[PassiveProject]
        self.application_settings = ApplicationSettings
        self.recommender_system = RecommenderSystem
        self.application_settings_saver = ApplicationSettingsSaver

    def create_project(self, name, description, destination) -> bool:
        pass

    def load_project(self, path) -> bool:
        pass

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
