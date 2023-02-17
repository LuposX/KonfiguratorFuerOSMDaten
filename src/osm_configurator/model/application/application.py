from __future__ import annotations

from pathlib import Path
import os, sys
from typing import TYPE_CHECKING, List, Final

from src.osm_configurator.model.application.application_interface import IApplication
import src.osm_configurator.model.application.recommender_system as recommender_system_i
import src.osm_configurator.model.application.application_settings as application_settings_i
import src.osm_configurator.model.application.application_settings_default_enum as application_settings_enum_i

if TYPE_CHECKING:
    from src.osm_configurator.model.application.passive_project import PassiveProject
    from src.osm_configurator.model.application.recommender_system import RecommenderSystem
    from src.osm_configurator.model.project.active_project import ActiveProject
    from src.osm_configurator.model.application.application_settings import ApplicationSettings
    from pathlib import Path

PROJECT_SETTING: str = "project_settings.csv"
APPLICATION_SETTINGS_FILE: Final = "application_setting.json"


class Application(IApplication):
    __doc__ = IApplication.__doc__

    def __init__(self):
        """
        Creates a new instance of the application_interface.Application.

        """
        # Get the path of the application
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # If the application is run as a bundle, the PyInstaller bootloader
            # extends the sys module by a flag frozen=True and sets the app
            # path into variable _MEIPASS'.
            application_path = sys._MEIPASS
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))

        # check for the application settings file.
        application_settings_file: Path = None
        file: str
        for file in os.listdir(application_path):
            if os.path.isfile(file):
                if os.path.basename(file) == APPLICATION_SETTINGS_FILE:
                    application_settings_file = Path(file)

        # This mean the application_Settings file doesn't exist yet and we need to create it
        if application_settings_file is None:
            application_settings_i.ApplicationSettings.create_application_settings_file(application_path,
                                                                                        APPLICATION_SETTINGS_FILE)

        self.active_project: ActiveProject = None

        self.application_settings: ApplicationSettings = application_settings_i.ApplicationSettings(
            application_settings_file)

        self.passive_project_list: List[PassiveProject] = self._create_passive_project_list(
            self.application_settings.get_setting(
                application_settings_enum_i.ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER))

        self.recommender_system: RecommenderSystem = recommender_system_i.RecommenderSystem()

    def create_project(self, name: str, description: str, destination: Path) -> bool:
        self.active_project = ActiveProject(destination, True, self.application_settings, name, description)
        return True

    def load_project(self, destination: Path) -> bool:
        self.active_project = ActiveProject(destination, False, self.application_settings)
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
                        passive_project_list.append(PassiveProject(filepath))
            return passive_project_list
        else:
            return None
