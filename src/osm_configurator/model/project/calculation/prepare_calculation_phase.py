from __future__ import annotations

import os

import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum_i
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion_i
import src.osm_configurator.model.parser.cut_out_parser as cut_out_parser_i
import src.osm_configurator.model.project.calculation.folder_path_calculator as folder_path_calculator_i
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum_i
from src.osm_configurator.model.parser.custom_exceptions.illegal_cut_out_exception import IllegalCutOutException

from src.osm_configurator.model.project.calculation.prepare_calculation_information import PrepareCalculationInformation

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.parser.cut_out_parser import CutOutParserInterface
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from pathlib import Path
    from typing import List
    from geopandas import GeoDataFrame
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion


class PrepareCalculationPhase:
    """
    This class is responsible to prepare calculation phase, it for example checks that the data
    from the last phase exists.
    """

    @classmethod
    def prepare_phase(cls, configuration_manager_o: ConfigurationManager,
                      current_calculation_phase: CalculationPhase,
                      last_calculation_phase: CalculationPhase) \
            -> PrepareCalculationInformation:
        """
        This method does things every calculation phase needs to do, it does the following:
        1. checks that cut_out file exists.
        2. read in the cut_out file.
        3. check that the calculation from last phase exists.
        4. creates a calculation result folder for the current phase.
        5. Gets a list of all data in the last phase.

        Args:
            configuration_manager_o (ConfigurationManager): The Configuration manager,
            we need to get stuff like the path.
            current_calculation_phase (CalculationPhase): The current phase which we want to calculate.
            last_calculation_phase (CalculationPhase): The last phase which we want to calculate.

        Returns:
            PrepareCalculationInformation: All important information the phases needed encapsulated in an object.
        """
        # Get data frame of geojson
        parser: CutOutParserInterface = cut_out_parser_i.CutOutParser()
        geojson_path: Path = configuration_manager_o.get_cut_out_configuration().get_cut_out_path()

        if geojson_path is None:
            return PrepareCalculationInformation(
                calculation_state=calculation_state_enum_i.CalculationState.ERROR_INVALID_CUT_OUT_DATA,
                error_message="geojson was not configured")

        if not os.path.exists(geojson_path):
            return PrepareCalculationInformation(
                calculation_state=calculation_state_enum_i.CalculationState.ERROR_INVALID_CUT_OUT_DATA,
                error_message="referenced geojson file does not exist")

        try:
            cut_out_dataframe: GeoDataFrame = parser.parse_cutout_file(geojson_path)
        except IllegalCutOutException as err:
            return PrepareCalculationInformation(
                calculation_state=calculation_state_enum_i.CalculationState.ERROR_INVALID_CUT_OUT_DATA,
                error_message="The geojson is corrupted: " + str(err))

        # Get path to the results of the last Phase
        checkpoint_folder_path_last_phase: Path = folder_path_calculator_i.FolderPathCalculator\
            .get_checkpoints_folder_path_from_phase(configuration_manager_o, last_calculation_phase)

        # Get path to the results of the current Phase
        checkpoint_folder_path_current_phase: Path = folder_path_calculator_i.FolderPathCalculator\
            .get_checkpoints_folder_path_from_phase(configuration_manager_o, current_calculation_phase)

        # Prepare result folder
        deleter: FileDeletion = file_deletion_i.FileDeletion()
        deleter.reset_folder(checkpoint_folder_path_current_phase)

        # check if the folder exist
        if not checkpoint_folder_path_current_phase.exists():
            return PrepareCalculationInformation(
                calculation_state=calculation_state_enum_i.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY,
                error_message="The result folder for the current phase doesn't exist.")

        if checkpoint_folder_path_last_phase is None:
            return PrepareCalculationInformation(
                calculation_state=calculation_state_enum_i.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY,
                error_message="The checkpoint folder of the last phase is not valid.")

        if current_calculation_phase == calculation_phase_enum_i.CalculationPhase.GEO_DATA_PHASE:
            if checkpoint_folder_path_last_phase.exists():
                list_of_traffic_cell_checkpoints: Path = checkpoint_folder_path_last_phase

            else:
                return PrepareCalculationInformation(
                    calculation_state=calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA,
                    error_message="The osm data are not valid.")

        else:
            if checkpoint_folder_path_last_phase.exists():
                list_of_traffic_cell_checkpoints: List[Path] = list(checkpoint_folder_path_last_phase.iterdir())

            else:
                return PrepareCalculationInformation(
                    calculation_state=calculation_state_enum_i.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY,
                    error_message="The result folder for the last phase doesn't exist.")

        return PrepareCalculationInformation(
            cut_out_dataframe=cut_out_dataframe,
            checkpoint_folder_path_last_phase=checkpoint_folder_path_last_phase,
            checkpoint_folder_path_current_phase=checkpoint_folder_path_current_phase,
            list_of_traffic_cell_checkpoints=list_of_traffic_cell_checkpoints
            )
