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
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from pathlib import Path
    from typing import List
    from geopandas import GeoDataFrame
    from geopandas import geoseries


def _get_checkpoints_folder_path_from_phase(configuration_manager_o: ConfigurationManager, phase: CalculationPhase):
    # Get the path to the project path and the name of the folder where we save the results and add them together
    project_path: Path = configuration_manager_o.get_active_project_path()

    result_folder_name: str = configuration_manager_o.get_calculation_phase_checkpoints_folder_name()

    phase_folder_name: str = phase.get_folder_name_for_results()
    checkpoint_folder_path: Path = project_path.joinpath(result_folder_name).joinpath(phase_folder_name)

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
        # Get path to the results of the last Phase
        checkpoint_folder_path_last_phase: Path = _get_checkpoints_folder_path_from_phase(configuration_manager_o,
                                                                                        calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE)

        # Get path to the results of the current Phase
        checkpoint_folder_path_current_phase: Path = _get_checkpoints_folder_path_from_phase(configuration_manager_o,
                                                                                             calculation_phase_enum.CalculationPhase.TAG_FILTER_PHASE)

        # check if the folder exist
        if checkpoint_folder_path_last_phase.exists() and checkpoint_folder_path_current_phase.exists():
            list_of_traffic_cell_checkpoints: List = list(checkpoint_folder_path_last_phase.iterdir())
        else:
            return calculation_state_enum.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY

        # Get the CategoryManager
        category_manager_o: CategoryManager = configuration_manager_o.get_category_manager()

        # create a new osm data parser, which is used to parse the osm data
        osm_data_parser_o: OSMDataParser = osm_data_parser.OSMDataParser()

        # parse the osm data  with the parser
        file_path: Path
        for file_path in list_of_traffic_cell_checkpoints:
            traffic_cell_data_frame: GeoDataFrame = osm_data_parser_o.parse_osm_data_file(file_path)

            # name of the file
            file_name = file_path.name

            # save the parsed osm data
            try:
                traffic_cell_data_frame.to_csv(checkpoint_folder_path_current_phase.joinpath(file_name))
            except Exception:  # TODO: This is probably bad style
                return calculation_state_enum.CalculationState.ERROR_INVALID_OSM_DATA
