from __future__ import annotations

import os
import csv

from pathlib import Path
import src.osm_configurator.model.project.active_project
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from src.osm_configurator.model.project.active_project import ActiveProject
    from pathlib import Path

READ: str = "r"
TRUE: str = "True"
FALSE: str = "False"
CONFIGURATION: str = "configuration"
CATEGORIES: str = "categories"
CSV: str = ".csv"
TXT: str = ".txt"
PROJECT_SETTINGS: str = "project_settings"
LAST_STEP: str = "last_step"
OSM_PATH: str = "osm_path"
AGGREGATION_METHOD: str = "aggregation_methods"
CUT_OUT_CONFIGURATION: str = "cut_out_configuration"

# The data loaded by this class is stored in csv or txt files
# The data in those files are stored as described below
SETTINGS_TABLE_FIRST_COLUMN: int = 0  # Describes the type of data stored in the following columns.
SETTINGS_TABLE_SECOND_COLUMN: int = 1  # In this column specific data is stored
SETTING_TABLE_FIRST_ROW: int = 0  # This row stores the name of the project
SETTING_TABLE_SECOND_ROW: int = 1  # This row stores the description of the project
SETTING_TABLE_THIRD_ROW: int = 2  # This row stores the location of the project
SETTING_TABLE_FOURTH_ROW: int = 3  # This row stores the calculation_check_points of the project
SETTING_TABLE_FIFTH_ROW: int = 4  # This row stores the last_edit_date of the project

NAME_OF_AGGREGATION: int = 0  # The name of the aggregation is stored in the first column of a csv
VALUE_OF_AGGREGATION: int = 1  # The value of the aggregation is stored in the first column of a csv

CUT_OUT_TABLE_FIRST_COLUMN: int = 0  # Describes the type of data stored in the second column.
CUT_OUT_TABLE_SECOND_COLUMN: int = 1  # In this column specific data is stored
CUT_OUT_TABLE_FIRST_ROW: int = 0  # In this row the cut-out-path is stored
CUT_OUT_TABLE_SECOND_ROW: int = 1  # In this row the cut-out-mode is stored


def convert_bool(string: str) -> bool | None:
    """
    Converts a string to the associated boolean.

    Args:
        string(str): The string.

    Returns:
        bool: The value of the string.
    """
    if string == TRUE:
        return True
    if string == FALSE:
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
            self.config_directory = os.path.join(project_path, CONFIGURATION)
            os.makedirs(self.config_directory)
            self.category_directory = os.path.join(self.config_directory, CATEGORIES)
            os.makedirs(self.category_directory)
            os.makedirs(os.path.join(
                project_path, self._active_project.get_project_settings().get_calculation_phase_checkpoints_folder()))
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
        self.config_directory = os.path.join(self.destination, CONFIGURATION)
        self.category_directory = os.path.join(self.config_directory, CATEGORIES)

        # Check if the folder is a valid project folder
        if not os.path.exists(self.destination):
            return False
        if not os.path.exists(self.config_directory):
            return False
        if not os.path.exists(self.category_directory):
            return False
        if not os.path.exists(os.path.join(self.destination, PROJECT_SETTINGS + CSV)):
            return False
        if not os.path.exists(os.path.join(self.destination, LAST_STEP + TXT)):
            return False

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
            print("6")
            return False
        return True

    def _load_project_settings(self) -> bool:
        filepath: Path = Path(os.path.join(self.destination, PROJECT_SETTINGS + CSV))
        if os.path.exists(filepath):
            with open(filepath, READ) as f:
                reader = csv.reader(f)
                project_settings_data = list(reader)
            self._active_project.get_project_settings().set_name(
                project_settings_data[SETTING_TABLE_FIRST_ROW][SETTINGS_TABLE_SECOND_COLUMN])
            self._active_project.get_project_settings().set_description(
                project_settings_data[SETTING_TABLE_SECOND_ROW][SETTINGS_TABLE_SECOND_COLUMN])
            self._active_project.get_project_settings().set_location(Path(
                project_settings_data[SETTING_TABLE_THIRD_ROW][SETTINGS_TABLE_SECOND_COLUMN]))
            self._active_project.get_project_settings().set_calculation_phase_checkpoints_folder(
                project_settings_data[SETTING_TABLE_FOURTH_ROW][SETTINGS_TABLE_SECOND_COLUMN])
            self._active_project.get_project_settings().set_last_edit_date(
                project_settings_data[SETTING_TABLE_FIFTH_ROW][SETTINGS_TABLE_SECOND_COLUMN])
            return True
        return False

    def _load_config_phase(self) -> bool:
        filepath: Path = Path(os.path.join(self.destination, LAST_STEP + TXT))
        if os.path.exists(filepath):
            with open(filepath, READ) as f:
                last_step: str = f.read()
            last_step_config_phase: ConfigPhase = ConfigPhase.convert_str_to_config_phase(last_step)
            if last_step_config_phase is not None:
                self._active_project.set_last_step(last_step_config_phase)
                return True
        return False

    def _load_osm_configurator(self) -> bool:
        filepath: Path = Path(os.path.join(self.config_directory, OSM_PATH + TXT))
        if os.path.exists(filepath):
            with open(filepath, READ) as f:
                osm_path: str = f.read()
            self._active_project.get_config_manager().get_osm_data_configuration().set_osm_data(Path(osm_path))
            return True
        return False

    def _load_aggregation_configuration(self) -> bool:
        filepath: Path = Path(os.path.join(self.config_directory, AGGREGATION_METHOD + CSV))
        if os.path.exists(filepath):
            with open(filepath, READ) as f:
                reader = csv.reader(f)
                aggregation: list[str] = list(reader)
            for row in aggregation:
                value: bool = convert_bool(row[VALUE_OF_AGGREGATION])
                if value is not None:
                    self._active_project.get_config_manager().get_aggregation_configuration().set_aggregation_method_active(
                        AggregationMethod.convert_str_to_aggregation_method(row[NAME_OF_AGGREGATION]), value)
                else:
                    return False
            return True
        return False

    def _load_cut_out_configurator(self) -> bool:
        filepath: Path = Path(os.path.join(self.config_directory, CUT_OUT_CONFIGURATION + CSV))
        if os.path.exists(filepath):
            with open(filepath, READ) as f:
                reader = csv.reader(f)
                cut_out: list[str] = list(reader)
            cut_out_path: Path = Path(cut_out[CUT_OUT_TABLE_FIRST_ROW][CUT_OUT_TABLE_SECOND_COLUMN])
            cut_out_mode: CutOutMode = CutOutMode.convert_str_to_cut_out_mode(
                cut_out[CUT_OUT_TABLE_SECOND_ROW][CUT_OUT_TABLE_SECOND_COLUMN])
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
        return self._active_project.get_config_manager().get_category_manager().override_categories(self.category_directory)
