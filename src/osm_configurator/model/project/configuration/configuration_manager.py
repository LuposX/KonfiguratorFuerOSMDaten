from __future__ import annotations

import pathlib

import src.osm_configurator.model.project.configuration.osm_data_configuration as osm_data_configuration
import src.osm_configurator.model.project.configuration.aggregation_configuration as aggregation_configuration
import src.osm_configurator.model.project.configuration.cut_out_configuration as cut_out_configuration
import src.osm_configurator.model.project.configuration.category_manager as category_manager

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.osm_data_configuration import OSMDataConfiguration
    from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationConfiguration
    from src.osm_configurator.model.project.configuration.cut_out_configuration import CutOutConfiguration
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager


class ConfigurationManager:
    """
    This class job is to manage the configurations of the OSM data, aggregation, cut-out and categories.
    It also makes this information available to the calculation
    """

    def __init__(self, active_project_path):
        """
        Creates a new instance of the ConfigurationManager.

        Args:
            active_project_path (pathLib.Path): The path pointing towards the project folder.
        """
        self._active_project_path = active_project_path
        self._calculation_phase_checkpoints_folder_name = "Results"  # TODO: remove Magic String
        self._osm_data_configurator = osm_data_configuration.OSMDataConfiguration()
        self._aggregation_configurator = aggregation_configuration.AggregationConfiguration()
        self._cut_out_configurator = cut_out_configuration.CutOutConfiguration()
        self._category_manager = category_manager.CategoryManager()

    def get_osm_data_configuration(self):
        """
        Getter for the osm data configuration.

        Returns:
            osm_data_configuration.OSMDataConfiguration: The osm data configuration.
        """
        return self._osm_data_configurator

    def get_aggregation_configuration(self):
        """
        Getter for the aggregation configuration.

        Returns:
            aggregation_configuration.AggregationConfiguration: The aggregation configuration.
        """
        return self._aggregation_configurator

    def get_cut_out_configuration(self) -> CutOutConfiguration:
        """
        Getter for the cut-out configuration.

        Returns:
            cut_out_configuration.CutOutConfiguration: The cut-out configuration.
        """
        return self._cut_out_configurator

    def get_category_manager(self):
        """
        Getter for the category manager.

        Returns:
            category_manager.CategoryManager: The category manager.
        """
        return CategoryManager

    def get_active_project_path(self) -> pathlib.Path:
        """
        Getter for the active project path

        Returns:
            pathlib.Path: the project path.
        """
        return self._active_project_path

    def get_calculation_phase_checkpoints_folder_name(self) -> str:
        """
        This method is used to get the name of the folder in which the results will be saved.

        Returns:
            str: The name of the folder
        """
        return self._calculation_phase_checkpoints_folder_name
