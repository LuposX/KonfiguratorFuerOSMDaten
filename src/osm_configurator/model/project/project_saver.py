from __future__ import annotations

import os
import csv
import shutil

from pathlib import Path
import src.osm_configurator.model.project.active_project
from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
from src.osm_configurator.model.project.configuration.category import Category
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.osm_configurator.model.project.active_project import ActiveProject
    from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
    from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationConfiguration
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from pathlib import Path


def _write_csv_file(data: list, filename: Path) -> bool:
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
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
            active_project (active_project.ActiveProject): The project the ProjectSaver shall load.
        """
        self.active_project: ActiveProject = active_project
        self.destination: Path = self.active_project.get_project_settings().get_location()

    def save_to_export(self, export_destination: Path) -> bool:
        """
        Stores all the configurations of the project at the given path.

        Args:
            export_destination (pathlib.Path): The path, where the config should be stored.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        if os.path.exists(export_destination):
            self.save_project()
            shutil.copytree(self.active_project.get_project_settings().get_location(), export_destination.joinpath(self.active_project.get_project_settings().get_name()))
            return True
        return False

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
        filename: Path = self._create_filename("project_settings")
        settings_data = [["name", self.active_project.get_project_settings().get_name()],
                         ["description", self.active_project.get_project_settings().get_description()],
                         ["location", self.active_project.get_project_settings().get_location()],
                         ["calculation_phase_checkpoints_folder", self.active_project.get_project_settings()
                         .get_calculation_phase_checkpoints_folder()]]
        _write_csv_file(settings_data, filename)
        return True

    def _save_config_phase(self) -> bool:
        """
        Stores the last config step of the project.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        filename: Path = self.destination.joinpath(Path("last_step.txt"))
        config_phase_data = self.active_project.get_last_step().get_name()
        with open(filename, "w") as f:
            f.write(config_phase_data)
        return True

    def _save_osm_configurator(self) -> bool:
        """
        Stores the osm-configuration of the project.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        config_directory: Path = self.destination.joinpath("configuration")
        filename: Path = config_directory.joinpath("osm_path.txt")
        osm_path_data = str(self.active_project.get_config_manager().get_osm_data_configuration().get_osm_data())
        with open(filename, "w") as f:
            f.write(osm_path_data)
        return True

    def _save_aggregation_configurator(self) -> bool:
        """
        Stores all active aggregation methods.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        filename = self._create_config_filename("active_methods")
        aggregation_methods: list = []
        aggregation_configurator: AggregationConfiguration = self.active_project.get_config_manager().get_aggregation_configuration()
        for method in AggregationMethod:
            aggregation_methods.append([method.get_name(), str(aggregation_configurator.is_aggregation_method_active(method))])
        _write_csv_file(aggregation_methods, filename)
        return True

    def _save_cut_out_configurator(self):
        """
        Stores the cut-out-configuration.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        filename = self._create_config_filename("cut_out_configuration")
        cut_out_data = [["cut_out_path",
                         self.active_project.get_config_manager().get_cut_out_configuration().get_cut_out_path()],
                        ["cut_out_mode",
                         self.active_project.get_config_manager().get_cut_out_configuration().get_cut_out_mode().get_name()]]
        _write_csv_file(cut_out_data, filename)
        return True

    def _save_categories(self):
        """
        Stores the categories of the project.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """
        category_manager = self.active_project.get_config_manager().get_category_manager()

        # Iterates throw every category and makes a csv-file for it
        for category in category_manager.get_categories():
            filename = self._create_category_filename(category.get_category_name())

            # Converts active attributes
            active_attributes: List[str] = []
            for attribute in category.get_activated_attribute():
                active_attributes.append(attribute.get_name())

            # Saves all attractivity attributes
            all_attractivity_attributes_list: list[str] = []
            for attractivity_attribute in category.get_activated_attribute():
                attractivity_attribute_values: list[str] = [attractivity_attribute.get_attractivity_attribute_name + "_"]
                for attribute in Attribute:
                    attractivity_attribute_values.append(attribute.get_name() + ":" + \
                                                    attractivity_attribute.get_attribute_factor(attribute))
                attractivity_attribute_values.append("base:" + attractivity_attribute.get_base_factor())
                all_attractivity_attributes_list.append(";".join(attractivity_attribute_values))

            # Saves all default value entry
            all_default_value_entries_list: list[str] = []
            for default_value_entry in category.get_default_value_list():
                default_value_entry_values: list[str] = [default_value_entry.get_default_value_entry_tag + "_"]
                for attribute in Attribute:
                    default_value_entry_values.append(attribute.get_name() + ":" \
                                                      + default_value_entry.get_attribute_default_value(attribute))
                all_default_value_entries_list.append(";".join(default_value_entry_values))
            category_data = [["name", category.get_category_name()],
                             ["status", category.is_active()],
                             ["white_list", category.get_whitelist()],
                             ["black_list", category.get_blacklist()],
                             ["calculation_method_of_area", category.get_calculation_method_of_area()],
                             ["active_attributes", active_attributes],
                             ["strictly_use_default_values", category.get_strictly_use_default_values()],
                             ["attractivity_attributes", all_attractivity_attributes_list],
                             ["default_value_list", all_default_value_entries_list]]
            _write_csv_file(category_data, filename)
        return True

    def _create_filename(self, name: str) -> Path:
        """
        Creates a filename to store data from the given str and destination.

        Args:
            name (str): The name of the new file.

        Returns:
            pathlib.Path: The created path.
        """
        file: str = name + ".csv"
        return self.destination.joinpath(file)

    def _create_config_filename(self, name: str) -> Path:
        """
        Creates a filename to store data from the given str and destination.

        Args:
            name (str): The name of the new file.

        Returns:
            pathlib.Path: The created path.
        """
        config_directory: Path = self.destination.joinpath("configuration")
        return config_directory.joinpath(name + ".csv")

    def _create_category_filename(self, name: str) -> Path:
        """
        Creates a filename to store category-data from the given str and destination.

        Args:
            name (str): The name of the new file.

        Returns:
            pathlib.Path: The created path.
        """
        config_directory: Path = self.destination.joinpath("configuration")
        category_directory: Path = config_directory.joinpath("categories")
        return category_directory.joinpath(self._create_filename(name))
