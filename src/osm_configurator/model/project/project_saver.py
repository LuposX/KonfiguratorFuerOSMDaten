from __future__ import annotations

import os
import csv

from datetime import date
import src.osm_configurator.model.project.active_project as active_project_i
from typing import TYPE_CHECKING

from src.osm_configurator.model.project import saver_io_handler_constants

if TYPE_CHECKING:
    from src.osm_configurator.model.project.active_project import ActiveProject
    from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
    from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationConfiguration
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from pathlib import Path

NAME: str = "name"
DESCRIPTION: str = "description"
LOCATION: str = "location"
DEFAULT_CHECKPOINTS_FOLDER_NAME: str = "calculation_check_points"
LAST_EDIT_DATE: str = "last_edit_date"
CUT_OUT_PATH: str = "cut_out_path"
CUT_OUT_MODE: str = "cut_out_mode"
STATUS: str = "status"
WHITE_LIST: str = "white_list"
BLACK_LIST: str = "black_list"
CALCULATION_METHOD_OF_AREA: str = "calculation_method_of_area"
ACTIVE_ATTRIBUTES: str = "active_attributes"
STRICTLY_USE_DEFAULT_VALUES: str = "strictly_use_default_values"
ATTRACTIVITY_ATTRIBUTES: str = "attractivity_attributes"
BASE: str = "base"
DEFAULT_VALUE_LIST: str = "default_value_list"


def _create_filename(name: str) -> Path:
    """
    Creates a name for the file to store data.

    Args:
        name (str): The name of the new file.

    Returns:
        pathlib.Path: The created File.
    """
    filename: str = name + saver_io_handler_constants.CSV
    return Path(filename)


def _write_csv_file(data: list, filename: Path) -> bool:
    """
    This method is to write the given data in a csv-file.

    Args:
        data (list): The data which should be stored.
        filename (pathlib.Path): The path where the csv-file with the data should be stored

    Returns:
        bool: True if saving works, otherwise false.
    """
    with open(filename, saver_io_handler_constants.WRITE, newline=saver_io_handler_constants.EMPTY_STRING) as f:
        writer = csv.writer(f)
        writer.writerows(data)
    return True

def _write_txt_file(data: str, filename: Path) -> bool:
    """
    This method is to write the given data in a txt-file.

    Args:
        data (str): The data which should be stored.
        filename (pathlib.Path): The path where the txt-file with the data should be stored

    Returns:
        bool: True if saving works, otherwise false.
    """
    with open(filename, saver_io_handler_constants.WRITE) as f:
        f.write(data)
    return True


class ProjectSaver:
    """
    The ProjectSave is responsible for saving the internal representation of the
    project onto the disk.
    """

    def __init__(self, active_project: ActiveProject):
        """
        Creates a new instance of the ProjectSaver.
        Therefore, it gets the current active project, which should be
        loaded if not newly created.

        Args:
            active_project (active_project_i.ActiveProject): The project the ProjectSaver shall load.
        """
        self.active_project: ActiveProject = active_project
        self.destination: Path = self.active_project.get_project_settings().get_location()

    def save_project(self) -> bool:
        """
        Stores all the configurations of the project.
        The information about the configuration of the project are stored to the disk.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        self.destination = self.active_project.get_project_settings().get_location()

        # Saves ProjectSettings
        if not self._save_settings():
            return False

        # Save ConfigPhase
        if not self._save_config_phase():
            return False

        # Save OSMDataConfiguration
        if not self._save_osm_configurator():
            return False

        # Save AggregationConfiguration
        if not self._save_aggregation_configurator():
            return False

        # Save CutOutConfiguration
        if not self._save_cut_out_configurator():
            return False

        # Delete all existing category files.
        config_directory: Path = Path(os.path.join(self.destination, saver_io_handler_constants.CONFIGURATION))
        category_directory: Path = Path(os.path.join(config_directory, saver_io_handler_constants.CATEGORIES))
        for file in os.listdir(category_directory):
            os.remove(os.path.join(category_directory, file))

        # Save Categories (one file for every category)
        if not self._save_categories():
            return False
        return True

    def _save_settings(self) -> bool:
        """
        Stores the settings of the project.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        filename: Path = self._create_file(saver_io_handler_constants.PROJECT_SETTINGS)
        settings_data = [[NAME, self.active_project.get_project_settings().get_name()],
                         [DESCRIPTION, self.active_project.get_project_settings().get_description()],
                         [LOCATION, self.active_project.get_project_settings().get_location()],
                         [LAST_EDIT_DATE, str(date.today())]]
        _write_csv_file(settings_data, filename)
        return True

    def _save_config_phase(self) -> bool:
        """
        Stores the last config step of the project.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        filename: Path = Path(os.path.join(self.destination, Path(saver_io_handler_constants.LAST_STEP + saver_io_handler_constants.TXT)))
        config_phase_data = self.active_project.get_last_step().get_name()
        return _write_txt_file(config_phase_data, filename)

    def _save_osm_configurator(self) -> bool:
        """
        Stores the osm-configuration of the project.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        config_directory: Path = Path(os.path.join(self.destination, saver_io_handler_constants.CONFIGURATION))
        filename: Path = Path(os.path.join(config_directory, saver_io_handler_constants.OSM_PATH + saver_io_handler_constants.TXT))
        osm_path_data = str(self.active_project.get_config_manager().get_osm_data_configuration().get_osm_data())
        return _write_txt_file(osm_path_data, filename)

    def _save_aggregation_configurator(self) -> bool:
        """
        Stores all active aggregation methods.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        filename = self._create_config_file(saver_io_handler_constants.AGGREGATION_METHOD)
        aggregation_methods: list[list[str]] = []
        aggregation_configurator: AggregationConfiguration = self.active_project.get_config_manager().get_aggregation_configuration()
        for method in AggregationMethod:
            aggregation_methods.append(
                [method.get_name(), aggregation_configurator.is_aggregation_method_active(method)])
        return _write_csv_file(aggregation_methods, filename)

    def _save_cut_out_configurator(self):
        """
        Stores the cut-out-configuration.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        filename = self._create_config_file(saver_io_handler_constants.CUT_OUT_CONFIGURATION)
        cut_out_data = [[CUT_OUT_PATH,
                         self.active_project.get_config_manager().get_cut_out_configuration().get_cut_out_path()],
                        [CUT_OUT_MODE,
                         self.active_project.get_config_manager().get_cut_out_configuration().get_cut_out_mode().get_name()]]
        return _write_csv_file(cut_out_data, filename)

    def _save_categories(self):
        """
        Stores the categories of the project.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        category_manager = self.active_project.get_config_manager().get_category_manager()

        # Iterates throw every category and makes a csv-file for it
        for category in category_manager.get_categories():

            # Converts active attributes
            active_attributes: list[str] = []
            for attribute in category.get_activated_attribute():
                active_attributes.append(attribute.get_name())

            # Saves all attractivity attributes
            all_attractivity_attributes_list: list[str] = []
            for attractivity_attribute in category.get_attractivity_attributes():
                attractivity_attribute_values: list[str] = [attractivity_attribute.get_attractivity_attribute_name()]
                for attribute in Attribute:
                    attractivity_attribute_values.append(attribute.get_name() + saver_io_handler_constants.DELIMITER_COLON + str(
                        attractivity_attribute.get_attribute_factor(attribute)))
                attractivity_attribute_values.append(
                    BASE + saver_io_handler_constants.DELIMITER_COLON + str(attractivity_attribute.get_base_factor()))
                all_attractivity_attributes_list.append(saver_io_handler_constants.DELIMITER_COMMA.join(attractivity_attribute_values))

            # Saves all default value entry
            all_default_value_entries_list: list[str] = []
            for default_value_entry in category.get_default_value_list():
                default_value_entry_values: list[str] = [default_value_entry.get_default_value_entry_tag()]
                for attribute in Attribute:
                    default_value_entry_values.append(attribute.get_name() + saver_io_handler_constants.DELIMITER_COLON + str(
                        default_value_entry.get_attribute_default(attribute)))
                all_default_value_entries_list.append(saver_io_handler_constants.DELIMITER_COMMA.join(default_value_entry_values))
            category_data = [[NAME, category.get_category_name()],
                             [STATUS, category.is_active()],
                             [WHITE_LIST, saver_io_handler_constants.DELIMITER_SEMICOLON.join(category.get_whitelist())],
                             [BLACK_LIST, saver_io_handler_constants.DELIMITER_SEMICOLON.join(category.get_blacklist())],
                             [CALCULATION_METHOD_OF_AREA,
                              category.get_calculation_method_of_area().get_calculation_method()],
                             [ACTIVE_ATTRIBUTES, saver_io_handler_constants.DELIMITER_SEMICOLON.join(active_attributes)],
                             [STRICTLY_USE_DEFAULT_VALUES, category.get_strictly_use_default_values()],
                             [ATTRACTIVITY_ATTRIBUTES, saver_io_handler_constants.DELIMITER_SEMICOLON.join(all_attractivity_attributes_list)],
                             [DEFAULT_VALUE_LIST, saver_io_handler_constants.DELIMITER_SEMICOLON.join(all_default_value_entries_list)]]
            filename = self._create_category_file(category.get_category_name())
            if not _write_csv_file(category_data, filename):
                return False
        return True

    def _create_file(self, name: str) -> Path:
        """
        Creates a filename to store data from the given str and destination.

        Args:
            name (str): The name of the new file.

        Returns:
            pathlib.Path: The created path.
        """
        return Path(os.path.join(self.destination, _create_filename(name)))

    def _create_config_file(self, name: str) -> Path:
        """
        Creates a filename to store data from the given str and destination.

        Args:
            name (str): The name of the new file.

        Returns:
            pathlib.Path: The created path.
        """
        config_directory: Path = Path(os.path.join(self.destination, saver_io_handler_constants.CONFIGURATION))
        return Path(os.path.join(config_directory, _create_filename(name)))

    def _create_category_file(self, name: str) -> Path:
        """
        Creates a filename to store category-data from the given str and destination.

        Args:
            name (str): The name of the new file.

        Returns:
            pathlib.Path: The created path.
        """
        config_directory: Path = Path(os.path.join(self.destination, saver_io_handler_constants.CONFIGURATION))
        category_directory: Path = Path(os.path.join(config_directory, saver_io_handler_constants.CATEGORIES))
        return Path(os.path.join(category_directory, _create_filename(name)))
