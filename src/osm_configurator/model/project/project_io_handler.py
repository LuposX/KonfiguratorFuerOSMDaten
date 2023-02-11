from __future__ import annotations

import os
import csv

from pathlib import Path
import src.osm_configurator.model.project.active_project
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode
from src.osm_configurator.model.project.configuration.category import Category
from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.active_project import ActiveProject
    from pathlib import Path


def convert_bool(string: str) -> bool | None:
    if string is "True":
        return True
    if string is not "False":
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

    def build_project(self, path: Path) -> bool:
        """
        This method is to build the given project. To do this it reads out the configurations and builds a folder
        structure on the disk.

        Args:
            path (pathlib.Path): The path pointing towards the project folder.

        Returns:
            bool: True if creating the project works, otherwise false.
        """

        if not os.path.exists(path):
            os.makedirs(path)
            self.config_directory = path.joinpath("configuration")
            os.makedirs(self.config_directory)
            self.category_directory = self.config_directory.joinpath("categories")
            os.makedirs(self.category_directory)
            os.makedirs(path.joinpath(self._active_project.get_project_settings().get_calculation_phase_checkpoints_folder()))
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
        self.config_directory = self.destination.joinpath("configuration")
        self.category_directory = self.config_directory.joinpath("categories")

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
        filepath = self.destination.joinpath("project_settings.csv")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
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
        filepath: Path = self.destination.joinpath("last_step.txt")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                last_step: str = f.read()
            last_step_config_phase: ConfigPhase = ConfigPhase.equals(last_step)
            if last_step_config_phase is not None:
                self._active_project.set_last_step(last_step_config_phase)
                return True
        return False

    def _load_osm_configurator(self) -> bool:
        filepath: Path = self.config_directory.joinpath("osm_path.txt")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                osm_path: str = f.read()
            self._active_project.get_config_manager().get_osm_data_configuration().set_osm_data(Path(osm_path))
            return True
        return False

    def _load_aggregation_configuration(self) -> bool:
        filepath: Path = self.config_directory.joinpath("aggregation_methods.csv")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                reader = csv.reader(f)
                aggregation = list(reader)
            for row in aggregation:
                if row[1] == "True":
                    self._active_project.get_config_manager().get_aggregation_configuration() \
                        .set_aggregation_method_active(AggregationMethod.equals(row[0]), True)
                elif row[1] == "False":
                    self._active_project.get_config_manager().get_aggregation_configuration() \
                        .set_aggregation_method_active(AggregationMethod.equals(row[0]), False)
                else:
                    return False
            return True
        return False

    def _load_cut_out_configurator(self) -> bool:
        filepath: Path = self.config_directory.joinpath("cut_out_configuration.csv")

        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                reader = csv.reader(f)
                cut_out = list(reader)
            cut_out_path: Path = Path(cut_out[0][1])
            cut_out_mode: CutOutMode = CutOutMode.equals(cut_out[1][1])
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

        category_list: list[Category] = []

        for file in os.listdir(self.destination):
            if file.endswith(".csv"):
                filepath: Path = self.category_directory.joinpath(str(file))
                with open(filepath, "r") as f:
                    reader = csv.reader(f)
                    category_data: list[str] = list(reader)
                loaded_category: Category = Category()
                loaded_category.set_category_name(category_data[0][1])
                if category_data[1][1] is "True":
                    loaded_category.activate()
                if category_data[1][1] is not "False":
                    loaded_category.deactivate()
                else:
                    return False

                # Loads whitelist
                loaded_category.set_whitelist(category_data[2][1].split(","))

                # Loads blacklist
                loaded_category.set_blacklist(category_data[3][1].split(","))

                # Loads calculation method of area
                loaded_category.set_calculation_method_of_area(CalculationMethodOfArea.equals(category_data[4][1]))

                # Loads active attributes
                number_of_active_attributes = len(category_data[5]) - 1
                for number in range(number_of_active_attributes):
                    attribute: Attribute = Attribute.equals(category_data[5][number + 1])
                    if attribute is not None:
                        loaded_category.set_attribute(attribute)
                    else:
                        return False

                # Loads strictly use default values
                strictly_use_default_value_bool: bool = convert_bool(category_data[6][1])
                if strictly_use_default_value_bool is not None:
                    loaded_category.set_strictly_use_default_values(strictly_use_default_value_bool)
                else:
                    return False

                # Loads attractivity attributes
                number_of_attractivity_attributes = len(category_data[6]) - 1
                for number in range(number_of_attractivity_attributes):
                    input_str: list[str] = category_data[6][number + 1].split("_")
                    attractivity_attribute: AttractivityAttribute = AttractivityAttribute(input_str[0])
                    attribute_list: list[str] = input_str[1].split(";")
                    for attribute_str in attribute_list:
                        attribute_str_split_up: list[str] = attribute_str.split(":")
                        if attribute_str_split_up[0] is "base":
                            attractivity_attribute.set_base_factor(float(attribute_str_split_up[1]))
                        else:
                            attractivity_attribute.set_attribute_factor(Attribute.equals(attribute_str_split_up[0]),
                                                                        float(attribute_str_split_up[1]))
                    loaded_category.add_attractivity_attribute(attractivity_attribute)

                # Loads default value entries
                number_of_default_value_entries = len(category_data[7]) - 1
                for number in range(number_of_default_value_entries):
                    input_str: list[str] = category_data[7][number + 1].split("_")
                    default_value_entry: DefaultValueEntry = DefaultValueEntry(input_str[0])
                    default_value_entries_list: list[str] = input_str[1].split(";")
                    for default_value_entry_str in default_value_entries_list:
                        attribute_str_split_up: list[str] = default_value_entry_str.split(":")
                        default_value_entry.set_attribute_default(Attribute.equals(attribute_str_split_up[0]),
                                                                  float(attribute_str_split_up[1]))
                    loaded_category.add_default_value_entry(default_value_entry)
                category_list.append(loaded_category)
                self._active_project.get_config_manager().get_category_manager().override_categories(category_list)
            else:
                return False
        return True