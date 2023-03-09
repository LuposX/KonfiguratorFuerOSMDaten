from __future__ import annotations

from src.osm_configurator.control.project_controller_interface import IProjectController

import pathlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.passive_project import PassiveProject
    from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
    from src.osm_configurator.model.application.application import Application
    from pathlib import Path


class ProjectController(IProjectController):
    __doc__ = IProjectController.__doc__

    def __init__(self, model: Application):
        """
        Creates a new instance of the ProjectController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        self._model: Application = model

    def get_project_path(self) -> Path:
        return self._model.get_active_project().get_project_path()

    def get_list_of_passive_projects(self) -> list[PassiveProject]:
        return self._model.get_passive_project_list()

    def load_project(self, path: pathlib.Path) -> bool:
        return self._model.load_project(path)

    def create_project(self, name: str, description: str, destination: pathlib.Path) -> bool:
        return self._model.create_project(name, description, destination)

    def delete_passive_project(self, passive_project: PassiveProject) -> bool:
        return self._model.delete_passive_project(passive_project)

    def save_project(self) -> bool:
        return self._model.get_active_project().get_project_saver().save_project()

    def set_current_config_phase(self, config_phase: ConfigPhase) -> bool:
        return self._model.get_active_project().set_last_step(config_phase)

    def get_current_config_phase(self) -> ConfigPhase:
        return self._model.get_active_project().get_last_step()

    def unload_project(self):
        return self._model.unload_project()

    def is_project_loaded(self) -> bool:
        return self._model.get_active_project() is not None
