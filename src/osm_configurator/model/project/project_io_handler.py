from __future__ import annotations

import os

import src.osm_configurator.model.project.active_project
import pathlib
import csv
from typing import TYPE_CHECKING
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase

if TYPE_CHECKING:
    from src.osm_configurator.model.project.active_project import ActiveProject
    from pathlib import Path

class ProjectIOHandler:
    """
    This class handles the I/O of a project.
    This includes:
    - loading a project from disk into memory that the user selected in the main menu
    - creating a project on the disk, if the user selected that
    """

    def __init__(self, active_project: ActiveProject):
        """
        Creates a new instance of the ProjectLoader. Therefore, it gets the current active project, which should be
        loaded if not newly created.

        Args:
            active_project (active_project.ActiveProject): The project the ProjectLoader shall load.
        """
        self._active_project = active_project
        self.destination: Path = Path()

    def build_project(self, path: Path):
        """
        This method is to build the given project. To do this it reads out the configurations and builts a folder
        structure on the disk.

        Args:
            path (pathlib.Path): The path pointing towards the project folder.

        Returns:
            bool: True if creating the project works, otherwise false.
        """
        pass

    def load_project(self, path: Path) -> bool:
        """
        Loads a project in from the disk into the memory.

        Args:
            path (pathlib.Path): The path pointing towards the project folder.

        Returns:
            bool: True if creating the project works, otherwise false.
        """
        self.destination = path

        # Load project_settings
        self._load_project_settings()
        filepath = os.path.join(path, "project_settings.csv")
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)

        for filename in os.listdir(path):
            if filename.endswith("settings.csv"):
                filepath = os.path.join(path, filename)
                with open(filepath, 'r') as f:
                    reader = csv.reader(f)
                    data = list(reader)

            if filename.endswith(".csv"):
                filepath = os.path.join(path, filename)
                with open(filepath, 'r') as f:
                    reader = csv.reader(f)
                    data = list(reader)
        return True

    def _load_project_settings(self) -> bool:
        filepath = os.path.join(self.destination, "project_settings.csv")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                reader = csv.reader(f)
                project_settings_data = list(reader)
            if len(project_settings_data) is 4:
                self._active_project.get_project_settings().set_name(project_settings_data[0][1])
                self._active_project.get_project_settings().set_description(project_settings_data[1][1])
                self._active_project.get_project_settings().set_location(Path(project_settings_data[2][1]))
                self._active_project.get_project_settings().set_calculation_phase_checkpoints_folder(
                    project_settings_data[3][1])
                return True
        return False

    def _load_config_phase(self) -> bool:
        # TODO path schauen
        filepath: Path = Path(os.path.join(self.destination, "last_step.txt"))
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                last_step: str = f.read()
                last_step_config_phase: ConfigPhase = ConfigPhase.equals(last_step)
                if last_step_config_phase is not None:
                    self._active_project.set_last_step(last_step_config_phase)
                    return True
        return False

    def _load_osm_configurator(self) -> bool:
        filepath: Path = Path(os.path.join(self.destination, "osm_path.txt"))
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                osm_path: str = f.read()
                self._active_project.get_config_manager().get_osm_data_configuration().set_osm_data(Path(osm_path))
                return True
        return False

    def _load_osm_configurator(self) -> bool:
        filepath: Path = Path(os.path.join(self.destination, "osm_path.txt"))
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                osm_path: str = f.read()
                self._active_project.get_config_manager().get_osm_data_configuration().set_osm_data(Path(osm_path))
                return True
        return False



