import pathlib

from src.osm_configurator.control.project_controller_interface import IProjectController
from src.osm_configurator.model.application.passive_project import PassiveProject
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase


class ProjectControllerStub(IProjectController):
    def get_list_of_passive_projects(self) -> list[PassiveProject]:
        pass

    def load_project(self, path: pathlib.Path) -> bool:
        pass

    def create_project(self, name: str, description: str, destination: pathlib.Path) -> bool:
        pass

    def delete_passive_project(self, project: PassiveProject) -> bool:
        pass

    def save_project(self) -> bool:
        pass

    def set_current_config_phase(self, config_phase: ConfigPhase) -> bool:
        pass

    def get_current_config_phase(self) -> ConfigPhase:
        pass

    def is_project_loaded(self) -> bool:
        pass