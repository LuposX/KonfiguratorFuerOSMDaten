from __future__ import annotations

import pandas

import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.parser.osm_data_parser as osm_data_parser

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.parser.osm_data_parser import OSMDataParser
    from pathlib import Path
    from typing import List
    from geopandas import GeoDataFrame
    from geopandas import geoseries


def _get_checkpoints_folder_path(configuration_manager_o):
    # Get the path to the project path and the name of the folder where we save the results and add them together
    project_path: Path = configuration_manager_o.get_active_project_path()
    folder_name: str = calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE.get_folder_name_for_results()
    checkpoint_folder_path: Path = project_path.joinpath(folder_name)
    return checkpoint_folder_path


class TagFilterPhase(ICalculationPhase):
    """
    This calculation phase is responsible for sorting OSM-elements into their corresponding categories.
    For details see the method calculate().
    """
    def calculate(self, configuration_manager_o: ConfigurationManager):
        """
        Sorts OSM-elements into their corresponding categories.
        Firstly this method reads in the OSM-files of the previously executed calculation phase. Every category has
        defined a tag filter in the configuration phase. The OSM-Elements are now sorted into the categories, depending
        on whether they do pass or do not pass the corresponding tag filters. A tag filter is defined by a
        black- and a whitelist. Each list is a collection of constraints of the tags of the osm-elements. An
        osm-element passes a tag filter, if all constraints of the whitelist are satisfied and no entry of the
        blacklist is satisfied.
        After execution the results shall be stored again on the hard-drive.

        Args:
            configuration_manager_o (configuration_manager.ConfigurationManager): The object containing all the configuration needed for an execution.

        Returns:
            calculation_state_enum.CalculationState: The state of the calculation after this phase finished its execution or failed trying so.
        """
        checkpoint_folder_path: Path = _get_checkpoints_folder_path(configuration_manager_o)

        # check if the folder exist
        if checkpoint_folder_path.exists():
            list_of_traffic_cell_checkpoints: List = list(checkpoint_folder_path.iterdir())
        else:
            return calculation_state_enum.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY

        # Get the CategoryManager
        category_manager_o: CategoryManager = configuration_manager_o.get_category_manager()

        # create a new osm data parser, which is used to parse the osm data
        osm_data_parser_o: OSMDataParser = osm_data_parser.OSMDataParser()

        # parse the osm data  with the parser
        for file_path in list_of_traffic_cell_checkpoints:
            traffic_cell_data_frame: GeoDataFrame = osm_data_parser_o.parse_osm_data_file(file_path)

            # TODO: magic string set corrects column name
            # This should be a pandas series
            traffic_cell_data_frame["tags"]: geoseries

            # Add a new column to the dataframe which says the category per element
            # TODO: another magic string
            # traffic_cell_data_frame["Categories"]: geoseries = category_data

            # Check each category how they apply to the GeoDataframe
            for category in category_manager_o.get_categories():
                category_name: str = category.get_category_name()
                category_blacklist: List[str] = category.get_blacklist()
                category_whitelist: List[str] = category.get_whitelist()

                traffic_cell_data_frame["tags"].get
