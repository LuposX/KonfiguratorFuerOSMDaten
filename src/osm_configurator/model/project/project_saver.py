from __future__ import annotations

import src.osm_configurator.model.project.active_project
import pathlib
import csv

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.active_project import ActiveProject
    from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
    from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationConfiguration
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
    from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
    from pathlib import Path


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
        self.active_project = active_project

    def save_project(self, destination: Path):
        """
        Stores all the configurations of the project.
        The information about the configuration of the project are stored to the disk.

        Args:
            destination (pathlib.Path): The path pointing towards the project folder. The data will be stored here.

        Returns:
            bool: True, if the project was stored successfully, False, if an error occurred.
        """

        # Saves ProjectSettings
        filename = str(destination) + "/" + self.active_project.get_project_settings().get_name() + "project_settings.csv"
        settings_data = [["name", self.active_project.get_project_settings().get_name()],
                         ["description", self.active_project.get_project_settings().get_description()],
                         ["location", self.active_project.get_project_settings().get_location()],
                         ["calculation_phase_checkpoints_folder", str(self.active_project.get_project_settings()
                                                                      .get_calculation_phase_checkpoints_folder())]]
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(settings_data)

        # Save ConfigPhase
        filename = str(destination) + "/" + self.active_project.get_project_settings().get_name() + "last_step.text"
        config_phase_data = str(self.active_project.get_last_step())
        with open(filename, 'w') as f:
            f.write(config_phase_data)

        # Save OSMDataConfiguration
        filename = str(destination) + "/" + self.active_project.get_project_settings().get_name() + "osm_path.text"
        osm_path_data = str(self.active_project.get_config_manager().get_osm_data_configuration().get_osm_data())
        with open(filename, 'w') as f:
            f.write(osm_path_data)

        # Save AggregationConfiguration
        filename = str(destination) + "/" + self.active_project.get_project_settings().get_name() + "/Configuration/active_methods.csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for method in AggregationMethod:
                if self.active_project.get_config_manager().get_aggregation_configuration() \
                        .is_aggregation_method_active(method):
                    writer.writerow(str(method))

        # Save CutOutConfiguration
        filename = str(destination) + "/" + self.active_project.get_project_settings().get_name() \
                   + "/Configuration/cut_out_configuration.csv"
        cut_out_data = [["cut_out_path",
                         self.active_project.get_config_manager().get_cut_out_configuration().get_cut_out_path()],
                        ["cut_out_mode",
                         self.active_project.get_config_manager().get_cut_out_configuration().get_cut_out_mode().get_name()]]

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(cut_out_data)

        # Save Categories (one file for every category)
        categories_labels = [["name", "status", "white_list", "black_list", "calculation_method_of_area",
                              "active_attributes", "strictly_use_default_values", "attractivity_attributes",
                              "default_value_list"]]
        category_manager = self.active_project.get_config_manager().get_category_manager()

        for category in category_manager.get_categories():
            filename = str(destination) + "/" + self.active_project.get_project_settings().get_name() + "/Configuration/Categories" \
                       + category.get_category_name + "csv"
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(categories_labels)
                category_name = category.get_category_name()
                category_is_active = category.is_active()
                category_whitelist = category.get_whitelist()
                category_blacklist = category.get_blacklist()
                category_calculation_method_of_area = category.get_calculation_method_of_area()
                # Todo: Method missing
                category_strictly_use_default_values = category.get_strictly_use_default_values()
                category_active_attributes = ""
                for attribute in Attribute:
                    if attribute:
                        category_active_attributes = category_active_attributes + "," + attribute.get_name()
                category_data = [[category_name, category_is_active, category_whitelist, category_blacklist,
                                  category_calculation_method_of_area, category_strictly_use_default_values,
                                  category_active_attributes]]
                writer.writerow(category_data)
