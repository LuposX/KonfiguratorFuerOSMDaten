from __future__ import annotations

import os
import csv

from pathlib import Path
import src.osm_configurator.model.project.active_project
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.osm_configurator.model.project.active_project import ActiveProject
    from pathlib import Path


def convert_bool(string: str) -> bool | None:
    """
    Converts a string to the associated boolean.

    Args:
        string(str): The string.

    Returns:
        bool: The value of the string.
    """
    if string == "True":
        return True
    if string == "False":
        return False
    else:
        return None


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
        self._active_project: ActiveProject = active_project
        self.destination: Path = Path()
        self.config_directory: Path = Path()
        self.category_directory: Path = Path()

    def build_project(self, project_path: Path) -> bool:
        """
        This method is to build the given project. To do this it reads out the configurations and builds a folder
        structure on the disk.

        Args:
            project_path (pathlib.Path): The path pointing towards the project folder.

        Returns:
            bool: True if creating the project works, otherwise false.
        """

        if not os.path.exists(project_path):
            os.makedirs(project_path)
            self.config_directory = os.path.join(project_path, "configuration")
            os.makedirs(self.config_directory)
            self.category_directory = os.path.join(self.config_directory, "categories")
            os.makedirs(self.category_directory)
            os.makedirs(os.path.join(project_path,
                                     self._active_project.get_project_settings().get_calculation_phase_checkpoints_folder())
                                     )
            return True
        return False

    def load_project(self, path: Path) -> bool:
        """
        Loads a project in from the disk into the memory.

        Args:
            path (pathlib.Path): The path pointing towards the project folder.

        Returns:
            bool: True if creating the project works, otherwise false.
        """
        self.destination = path
        self.config_directory = os.path.join(self.destination, "configuration")
        self.category_directory = os.path.join(self.config_directory, "categories")

        # Loads the different parts of the project
        if not self._load_project_settings():
            return False

        if not self._load_config_phase():
            return False

        if not self._load_osm_configurator():
            return False

        if not self._load_aggregation_configuration():
            return False

        if not self._load_cut_out_configurator():
            return False

        if not self._load_category_configuration():
            return False
        return True

    def _load_project_settings(self) -> bool:
        filepath = os.path.join(self.destination, "project_settings.csv")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                reader = csv.reader(f)
                project_settings_data = list(reader)
            self._active_project.get_project_settings().set_name(project_settings_data[0][1])
            self._active_project.get_project_settings().set_description(project_settings_data[1][1])
            self._active_project.get_project_settings().set_location(Path(project_settings_data[2][1]))
            self._active_project.get_project_settings().set_calculation_phase_checkpoints_folder(
                project_settings_data[3][1])
            self._active_project.get_project_settings().set_last_edit_date(project_settings_data[4][1])
            return True
        return False

    def _load_config_phase(self) -> bool:
        filepath: Path = os.path.join(self.destination, "last_step.txt")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                last_step: str = f.read()
            last_step_config_phase: ConfigPhase = ConfigPhase.convert_str_to_config_phase(last_step)
            if last_step_config_phase is not None:
                self._active_project.set_last_step(last_step_config_phase)
                return True
        return False

    def _load_osm_configurator(self) -> bool:
        filepath: Path = os.path.join(self.config_directory, "osm_path.txt")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                osm_path: str = f.read()
            self._active_project.get_config_manager().get_osm_data_configuration().set_osm_data(Path(osm_path))
            return True
        return False

    def _load_aggregation_configuration(self) -> bool:
        filepath: Path = os.path.join(self.config_directory, "aggregation_methods.csv")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                reader = csv.reader(f)
                aggregation = list(reader)
            for row in aggregation:
                value: bool = convert_bool(row[1])
                if value is not None:
                    self._active_project.get_config_manager().get_aggregation_configuration() \
                        .set_aggregation_method_active(AggregationMethod.convert_str_to_aggregation_method(row[0]), value)
                else:
                    return False
            return True
        return False

    def _load_cut_out_configurator(self) -> bool:
        filepath: Path = os.path.join(self.config_directory, "cut_out_configuration.csv")

        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                reader = csv.reader(f)
                cut_out = list(reader)
            cut_out_path: Path = Path(cut_out[0][1])
            cut_out_mode: CutOutMode = CutOutMode.convert_str_to_cut_out_mode(cut_out[1][1])
            if os.path.exists(cut_out_path):
                self._active_project.get_config_manager().get_cut_out_configuration().set_cut_out_path(cut_out_path)
            else:
                return False
            if cut_out_mode is not None:
                self._active_project.get_config_manager().get_cut_out_configuration().set_cut_out_mode(cut_out_mode)
            else:
                return False
            return True
        return False

    def _load_category_configuration(self) -> bool:
        self._active_project.get_config_manager().get_category_manager().override_categories(self.category_directory)
