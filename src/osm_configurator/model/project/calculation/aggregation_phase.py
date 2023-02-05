from __future__ import annotations

import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum_i
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum_i
import src.osm_configurator.model.parser.osm_data_parser as osm_data_parser_i
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion_i
import src.osm_configurator.model.parser.cut_out_parser as cut_out_parser_i
import src.osm_configurator.model.project.calculation.osm_file_format_enum as osm_file_format_enum_i

import src.osm_configurator.model.project.calculation.calculation_phase_utility as calculation_phase_utility

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
from src.osm_configurator.model.parser.custom_exceptions.tags_wrongly_formatted_exception import TagsWronglyFormatted
from src.osm_configurator.model.parser.custom_exceptions.osm_data_wrongly_formatted_Exception import \
    OSMDataWronglyFormatted
from src.osm_configurator.model.parser.custom_exceptions.illegal_cut_out_exception import IllegalCutOutException

import src.osm_configurator.model.model_constants as model_constants_i

import pandas as pd
import geopandas as gpd

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
    from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationConfiguration
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.parser.osm_data_parser import OSMDataParser
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.parser.cut_out_parser import CutOutParserInterface
    from pathlib import Path
    from typing import Tuple, Dict, List
    from geopandas import GeoDataFrame
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion


class AggregationPhase(ICalculationPhase):
    """
    This calculation phase is responsible for aggregating the attractivity attributes in the given traffic cells.
    For details see the method calculate().
    """

    def calculate(self, configuration_manager_o: ConfigurationManager) -> Tuple[CalculationState, str]:
        """
        Aggregates the attractivity attributes in the given traffic cells.
        The calculation phase reads the data of the previous calculation phase. Now for every traffic cell all selected
        aggregation methods are performed for all attractivity attributes. For details on the different aggregation
        methods, see AggregationMethod.
        After the calculations are done, the results are stored on the hard-drive.

        Args:
            configuration_manager_o (configuration_manager.ConfigurationManager): The object containing all the configuration needed for execution.

        Returns:
            calculation_state_enum.CalculationState: The state of the calculation, after this phase finished its execution or failed trying so.
        """
        # Get path to the results of the last Phase
        checkpoint_folder_path_last_phase: Path = calculation_phase_utility.get_checkpoints_folder_path_from_phase(
            configuration_manager_o,
            calculation_phase_enum_i.CalculationPhase.GEO_DATA_PHASE)

        # Get path to the results of the current Phase
        checkpoint_folder_path_current_phase: Path = calculation_phase_utility.get_checkpoints_folder_path_from_phase(
            configuration_manager_o,
            calculation_phase_enum_i.CalculationPhase.TAG_FILTER_PHASE)

        # Prepare result folder
        deleter: FileDeletion = file_deletion_i.FileDeletion()
        deleter.reset_folder(checkpoint_folder_path_current_phase)

        # check if the folder exist
        if checkpoint_folder_path_last_phase.exists() and checkpoint_folder_path_current_phase.exists():
            list_of_traffic_cell_checkpoints: List = list(checkpoint_folder_path_last_phase.iterdir())
        else:
            return calculation_state_enum_i.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY, ""

        # Get the CategoryManager
        aggregation_configuration: AggregationConfiguration = configuration_manager_o.get_aggregation_configuration()

        # get all activated aggregation methods
        active_aggregation_methods: List[AggregationMethod] = self._get_activated_aggregation_methods(aggregation_configuration)

        # Create a dict where we save the dataframe
        aggregation_phase_data: Dict[AggregationMethod, List] = {}
        aggregation_phase_data.update({model_constants_i.CL_OSM_ELEMENT_NAME: []})
        for agg_method in active_aggregation_methods:
            aggregation_phase_data.update({agg_method: []})

        # For each traffic cell.
        file_path: Path
        for file_path in list_of_traffic_cell_checkpoints:
            try:
                traffic_cell_data_frame: GeoDataFrame = gpd.read_file(file_path)

            except TagsWronglyFormatted as err:
                return calculation_state_enum_i.CalculationState.ERROR_TAGS_WRONGLY_FORMATTED, ''.join(str(err))

            except OSMDataWronglyFormatted as err:
                return calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA, ''.join(str(err))

            # add the name of the cell
            aggregation_phase_data[model_constants_i.CL_OSM_ELEMENT_NAME].append(file_path.stem)

            # Calculate the given method
            aggregation_method: AggregationMethod
            for aggregation_method in aggregation_configuration.get_all_aggregation_methods():
                result: float = aggregation_method.calculate_aggregation(traffic_cell_data_frame)

                aggregation_phase_data[aggregation_method].append(result)

        return pd.DataFrame.from_dict(aggregation_phase_data)

    def _get_activated_aggregation_methods(self, aggregation_configuration: AggregationConfiguration):
        """
        Returns all activated aggregation method, where activated means the suer want to calculate with them.
        """
        active_aggregation_methods: List[AggregationMethod] = []

        for aggregation_method in aggregation_configuration.get_all_aggregation_methods():
            if aggregation_configuration.is_aggregation_method_active(aggregation_method):
                active_aggregation_methods.append(aggregation_method)

        return active_aggregation_methods