from __future__ import annotations

import os
import csv
from pathlib import Path

import src.osm_configurator.model.project.calculation.aggregation_method_enum as aggregation_method_enum_i
import src.osm_configurator.model.project.active_project as active_project_i

from src.osm_configurator.model.project import saver_io_handler_constants
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.active_project import ActiveProject

# The data loaded by this class is stored in csv or txt files
# The data in those files are stored as described below
SETTINGS_TABLE_FIRST_COLUMN: int = 0  # Describes the type of data stored in the following columns.
SETTINGS_TABLE_SECOND_COLUMN: int = 1  # In this column specific data is stored
SETTING_TABLE_FIRST_ROW: int = 0  # This row stores the name of the project
SETTING_TABLE_SECOND_ROW: int = 1  # This row stores the description of the project
SETTING_TABLE_THIRD_ROW: int = 2  # This row stores the last_edit_date of the project

NAME_OF_AGGREGATION: int = 0  # The name of the aggregation is stored in the first column of a csv
VALUE_OF_AGGREGATION: int = 1  # The value of the aggregation is stored in the first column of a csv

CUT_OUT_TABLE_FIRST_COLUMN: int = 0  # Describes the type of data stored in the second column.
CUT_OUT_TABLE_SECOND_COLUMN: int = 1  # In this column specific data is stored
CUT_OUT_TABLE_FIRST_ROW: int = 0  # In this row the cut-out-path is stored
CUT_OUT_TABLE_SECOND_ROW: int = 1  # In this row the cut-out-mode is stored


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
            active_project (active_project_i.ActiveProject): The project the ProjectLoader shall load.
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
            self.config_directory = os.path.join(project_path, saver_io_handler_constants.CONFIGURATION)
            os.makedirs(self.config_directory)
            self.category_directory = os.path.join(self.config_directory, saver_io_handler_constants.CATEGORIES)
            os.makedirs(self.category_directory)
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
        self.config_directory = os.path.join(self.destination, saver_io_handler_constants.CONFIGURATION)
        self.category_directory = os.path.join(self.config_directory, saver_io_handler_constants.CATEGORIES)

        # Check if the folder is a valid project folder
        if not os.path.exists(self.destination):
            return False
        if not os.path.exists(self.config_directory):
            return False
        if not os.path.exists(self.category_directory):
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
            return False
        return True

    def _load_project_settings(self) -> bool:
        filepath: Path = Path(os.path.join(
            self.destination,
            saver_io_handler_constants.PROJECT_SETTINGS + saver_io_handler_constants.CSV)
        )
        if os.path.exists(filepath):
            project_settings_data: list[str] = ProjectIOHandler._read_csv_file(filepath)
            self._active_project.get_project_settings().set_name(
                project_settings_data[SETTING_TABLE_FIRST_ROW][SETTINGS_TABLE_SECOND_COLUMN])
            self._active_project.get_project_settings().set_description(
                project_settings_data[SETTING_TABLE_SECOND_ROW][SETTINGS_TABLE_SECOND_COLUMN])
            self._active_project.get_project_settings().set_last_edit_date(
                project_settings_data[SETTING_TABLE_THIRD_ROW][SETTINGS_TABLE_SECOND_COLUMN])
            return True
        return False

    def _load_config_phase(self) -> bool:
        filepath: Path = Path(os.path.join(
            self.destination,
            saver_io_handler_constants.LAST_STEP + saver_io_handler_constants.TXT)
        )
        if os.path.exists(filepath):
            last_step: str = ProjectIOHandler._read_txt_file(filepath)
            last_step_config_phase: ConfigPhase = ConfigPhase.convert_str_to_config_phase(last_step)
            if last_step_config_phase is not None:
                self._active_project.set_last_step(last_step_config_phase)
                return True
        return False

    def _load_osm_configurator(self) -> bool:
        filepath: Path = Path(os.path.join(
            self.config_directory,
            saver_io_handler_constants.OSM_PATH + saver_io_handler_constants.TXT)
        )
        if os.path.exists(filepath):
            osm_path: str = ProjectIOHandler._read_txt_file(filepath)
            self._active_project.get_config_manager().get_osm_data_configuration().set_osm_data(Path(osm_path))
            return True
        return False

    def _load_aggregation_configuration(self) -> bool:
        filepath: Path = Path(os.path.join(
            self.config_directory,
            saver_io_handler_constants.AGGREGATION_METHOD + saver_io_handler_constants.CSV)
        )
        if os.path.exists(filepath):
            aggregation: list[str] = ProjectIOHandler._read_csv_file(filepath)
            for row in aggregation:
                value: bool = ProjectIOHandler._convert_bool(row[VALUE_OF_AGGREGATION])
                if value is not None:
                    self._active_project.get_config_manager().get_aggregation_configuration()\
                        .set_aggregation_method_active(
                        aggregation_method_enum_i.convert_str_to_aggregation_method(row[NAME_OF_AGGREGATION]), value)
                else:
                    return False
            return True
        return False

    def _load_cut_out_configurator(self) -> bool:
        filepath: Path = Path(os.path.join(
            self.config_directory,
            saver_io_handler_constants.CUT_OUT_CONFIGURATION + saver_io_handler_constants.CSV)
        )
        if os.path.exists(filepath):
            cut_out: list[str] = ProjectIOHandler._read_csv_file(filepath)
            cut_out_path: Path = Path(cut_out[CUT_OUT_TABLE_FIRST_ROW][CUT_OUT_TABLE_SECOND_COLUMN])
            cut_out_mode: CutOutMode = CutOutMode.convert_str_to_cut_out_mode(
                cut_out[CUT_OUT_TABLE_SECOND_ROW][CUT_OUT_TABLE_SECOND_COLUMN])
            self._active_project.get_config_manager().get_cut_out_configuration().set_cut_out_path(cut_out_path)
            if cut_out_mode is not None:
                self._active_project.get_config_manager().get_cut_out_configuration().set_cut_out_mode(cut_out_mode)
            else:
                return False
            return True
        return False

    def _load_category_configuration(self) -> bool:
        return self._active_project.get_config_manager().get_category_manager()\
            .override_categories(self.category_directory)

    @staticmethod
    def _convert_bool(string: str) -> bool | None:
        """
        Converts a string to the associated boolean.

        Args:
            string(str): The string.

        Returns:
            bool: The value of the string.
        """
        if string == saver_io_handler_constants.TRUE:
            return True
        if string == saver_io_handler_constants.FALSE:
            return False

        return None

    @staticmethod
    def _read_csv_file(path: Path) -> list[str]:
        """
        Reads out the given csv file and returns the content.

        Args:
            path (pathlib.Path): The path pointing towards the csv file.

        Returns:
            list[str]: The content of the csv file.
        """
        with open(path, saver_io_handler_constants.READ, encoding="utf-8") as csv_file:
            return list(csv.reader(csv_file))

    @staticmethod
    def _read_txt_file(path: Path) -> str:
        """
        Reads out the given txt file and returns the content.

        Args:
            path (pathlib.Path): The path pointing towards the txt file.

        Returns:
            str: The content of the txt file.
        """
        with open(path, saver_io_handler_constants.READ, encoding="utf-8") as txt_file:
            return txt_file.read()
