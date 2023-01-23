from src.osm_configurator.control.project_controller_interface import IProjectController

import pathlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication
    from src.osm_configurator.model.application.passive_project import PassiveProject
    from src.osm_configurator.model.project.config_phase_enum import ConfigPhase


class ProjectController(IProjectController):
    __doc__ = IProjectController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the ProjectController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def get_list_of_passive_projects(self):
        pass

    def load_project(self, path: pathlib.Path):
        pass

    def create_project(self, name: str, description: str, destination: pathlib.Path):
        pass

    def delete_passive_project(self, project: PassiveProject):
        pass

    def save_project(self):
        pass

    def set_current_config_phase(self, config_phase: ConfigPhase):
        pass

    def get_current_config_phase(self):
        pass

    def is_project_loaded(self):
        pass
