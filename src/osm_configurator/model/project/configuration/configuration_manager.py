from __future__ import annotations

import pathlib

import src.osm_configurator.model.project.configuration.osm_data_configuration
import src.osm_configurator.model.project.configuration.aggregation_configuration
import src.osm_configurator.model.project.configuration.cut_out_configuration
import src.osm_configurator.model.project.configuration.category_manager


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

    def get_osm_data_configuration(self):
        """
        Getter for the osm data configuration.

        Returns:
            osm_data_configuration.OSMDataConfiguration: The osm data configuration.
        """
        pass

    def get_aggregation_configuration(self):
        """
        Getter for the aggregation configuration.

        Returns:
            aggregation_configuration.AggregationConfiguration: The aggregation configuration.
        """
        pass

    def get_cut_out_configuration(self):
        """
        Getter for the cut-out configuration.

        Returns:
            cut_out_configuration.CutOutConfiguration: The cut-out configuration.
        """
        pass

    def get_category_manager(self):
        """
        Getter for the category manager.

        Returns:
            category_manager.CategoryManager: The category manager.
        """
        pass

    def get_active_project_path(self) -> pathlib.Path:
        """
        Getter for the active project path

        Returns:
            pathlib.Path: the project path.
        """
        pass

    def get_calculation_phase_checkpoints_folder(self) -> str:
        """
        This method is used to get the name of the folder in which the results will be saved.

        Returns:
            str: the name of the folder
        """
        pass

