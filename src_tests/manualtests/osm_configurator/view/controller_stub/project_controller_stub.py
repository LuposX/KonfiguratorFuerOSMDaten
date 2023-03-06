import pathlib
from typing import List

from src.osm_configurator.control.project_controller_interface import IProjectController
from src.osm_configurator.model.application.passive_project import PassiveProject
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase

from pathlib import Path


class ProjectControllerStub(IProjectController):
    def get_project_path(self) -> Path:
        return Path("")

    def unload_project(self):
        pass

    def get_list_of_passive_projects(self) -> List[PassiveProject]:
        #foo = []
        #for i in range(100):
            #foo.append(PassiveProject(Path()))

        return []

    def load_project(self, path: pathlib.Path) -> bool:
        return True

    def create_project(self, name: str, description: str, destination: pathlib.Path) -> bool:
        return True

    def delete_passive_project(self, project: PassiveProject) -> bool:
        return True

    def save_project(self) -> bool:
        return True

    def set_current_config_phase(self, config_phase: ConfigPhase) -> bool:
        return True

    def get_current_config_phase(self) -> ConfigPhase:
        return ConfigPhase.DATA_CONFIG_PHASE

    def is_project_loaded(self) -> bool:
        return True
