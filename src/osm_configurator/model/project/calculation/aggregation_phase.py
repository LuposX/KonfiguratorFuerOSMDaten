from __future__ import annotations

import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum_i
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum_i
import src.osm_configurator.model.parser.osm_data_parser as osm_data_parser_i
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion_i
import src.osm_configurator.model.parser.cut_out_parser as cut_out_parser_i
import src.osm_configurator.model.project.calculation.osm_file_format_enum as osm_file_format_enum_i

import src.osm_configurator.model.project.calculation.folder_path_calculator as folder_path_calculator_i



from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
from src.osm_configurator.model.parser.custom_exceptions.tags_wrongly_formatted_exception import TagsWronglyFormatted
from src.osm_configurator.model.parser.custom_exceptions.osm_data_wrongly_formatted_Exception import \
    OSMDataWronglyFormatted
from src.osm_configurator.model.parser.custom_exceptions.illegal_cut_out_exception import IllegalCutOutException
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum

import src.osm_configurator.model.model_constants as model_constants_i

import pandas as pd
import geopandas as gpd
from fiona.errors import DriverError

from pathlib import Path

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
    from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationConfiguration
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.parser.osm_data_parser import OSMDataParser
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.parser.cut_out_parser import CutOutParserInterface
    from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from pathlib import Path
    from typing import Tuple, Dict, List
    from geopandas import GeoDataFrame
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion
    from pandas import DataFrame


class AggregationPhase(ICalculationPhase):
    """
    This calculation phase is responsible for aggregating the attractivity attributes in the given traffic cells.
    For details see the method calculate().
    """
    def get_calculation_phase_enum(self) -> CalculationPhase:
        return calculation_phase_enum.CalculationPhase.AGGREGATION_PHASE

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
        folder_path_calculator_o = folder_path_calculator_i.FolderPathCalculator()

        # Get path to the results of the last Phase
        checkpoint_folder_path_last_phase: Path = folder_path_calculator_o.get_checkpoints_folder_path_from_phase(
            configuration_manager_o,
            calculation_phase_enum_i.CalculationPhase.ATTRACTIVITY_PHASE)

        # Get path to the results of the current Phase
        checkpoint_folder_path_current_phase: Path = folder_path_calculator_o.get_checkpoints_folder_path_from_phase(
            configuration_manager_o,
            calculation_phase_enum_i.CalculationPhase.AGGREGATION_PHASE)

        # Prepare result folder
        deleter: FileDeletion = file_deletion_i.FileDeletion()
        deleter.reset_folder(checkpoint_folder_path_current_phase)

        # check if the folder exist
        if Path(checkpoint_folder_path_last_phase).exists() and Path(checkpoint_folder_path_current_phase).exists():
            list_of_traffic_cell_checkpoints: List = list(checkpoint_folder_path_last_phase.iterdir())

        else:
            return calculation_state_enum_i.CalculationState.ERROR_INVALID_PREVIOUS_CALCULATIONS, \
                "Data folder from the previous phase doesn't exists."

        # Get the CategoryManager
        aggregation_configuration: AggregationConfiguration = configuration_manager_o.get_aggregation_configuration()

        # get all activated aggregation methods
        active_aggregation_methods: List[AggregationMethod] = aggregation_configuration.get_all_active_aggregation_methods()

        # For each active aggregation method create one dataframe with all traffic cells in it
        aggregation_method: AggregationMethod
        for aggregation_method in active_aggregation_methods:

            # Create a dict where we save the dataframe
            # it has as key the name of a attractivity attribute and as value the list of calculated data entries
            # for each traffic cell.
            # Another key, value pair is the traffic cell name, per entry in a list.
            aggregation_phase_data: Dict[str, List] = {}
            aggregation_phase_data.update({model_constants_i.CL_TRAFFIC_CELL_NAME: []})

            attractivity_attribute: AttractivityAttribute
            for attractivity_attribute in configuration_manager_o.get_category_manager()\
                    .get_all_defined_attractivity_attributes():
                aggregation_phase_data.update({attractivity_attribute.get_attractivity_attribute_name(): []})

            # For each traffic cell.
            file_path: Path
            for file_path in list_of_traffic_cell_checkpoints:
                try:
                    traffic_cell_data_frame: DataFrame = pd.read_csv(file_path, index_col=0)

                except TagsWronglyFormatted as err:
                    return calculation_state_enum_i.CalculationState.ERROR_TAGS_WRONGLY_FORMATTED, ''.join(str(err))

                except (OSMDataWronglyFormatted, DriverError, UnicodeDecodeError) as err:
                    return calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA, ''.join(str(err))

                # add the name of the cell
                aggregation_phase_data[model_constants_i.CL_TRAFFIC_CELL_NAME].append(file_path.stem)

                # iterate over the column of the dataframe, each column corresponds to one attractivity attribute
                # This ignores the index column
                column_name: str
                for column_name in traffic_cell_data_frame.columns.values:
                    # Calculate the given method
                    column_result: float = aggregation_method.calculate_aggregation(traffic_cell_data_frame[column_name])

                    aggregation_phase_data[column_name].append(column_result)

            aggregation_method_df: DataFrame = pd.DataFrame.from_dict(aggregation_phase_data)

            # Save the dataframe to the disk
            # This is the dataframe where all traffic cells and attractivity attributes are in it for a single
            # aggregation method.
            try:
                aggregation_method_df. \
                    to_csv(checkpoint_folder_path_current_phase.
                           joinpath(aggregation_method.get_name()
                                    + osm_file_format_enum_i.OSMFileFormat.CSV.get_file_extension()))

            # If there's an error while encoding the file.
            except ValueError as err:
                return calculation_state_enum_i.CalculationState.ERROR_ENCODING_THE_FILE, ''.join(str(err))

            # If the file cannot be opened.
            except OSError as err:
                return calculation_state_enum_i.CalculationState.ERROR_COULDNT_OPEN_FILE, ''.join(str(err))

        return calculation_state_enum_i.CalculationState.RUNNING, ""
