from __future__ import annotations

import os

import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum_i
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion_i
import src.osm_configurator.model.parser.cut_out_parser as cut_out_parser_i
import src.osm_configurator.model.project.calculation.folder_path_calculator as folder_path_calculator_i
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum_i
from src.osm_configurator.model.parser.custom_exceptions.illegal_cut_out_exception import IllegalCutOutException

from typing import TYPE_CHECKING, List, Tuple

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.parser.cut_out_parser import CutOutParserInterface
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from pathlib import Path
    from typing import List
    from typing import Tuple
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
            -> Tuple[GeoDataFrame, Path, Path, List[Path] | Path] | Tuple[CalculationState, str, None, None]:
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
            Tuple[CalculationState, str]: Gets returned if an error occurred.
            Tuple[GeoDataFrame, Path, Path, List[Path]]: Returns in a tuple with the following items in
                                                        the following order:
                                                        Dataframe of the cut out file,
                                                        the path towards the folder of the last phase,
                                                        the path towards the folder of the current phase,
                                                         a list of paths for all items in the last directory.
        """
        # Get data frame of geojson
        parser: CutOutParserInterface = cut_out_parser_i.CutOutParser()
        geojson_path: Path = configuration_manager_o.get_cut_out_configuration().get_cut_out_path()

        if geojson_path is None:
            return calculation_state_enum_i.CalculationState.ERROR_INVALID_CUT_OUT_DATA, \
                "geojson was not configured", None, None

        if not os.path.exists(geojson_path):
            return calculation_state_enum_i.CalculationState.ERROR_INVALID_CUT_OUT_DATA, \
                "referenced geojson file does not exist", None, None

        try:
            cut_out_dataframe: GeoDataFrame = parser.parse_cutout_file(geojson_path)
        except IllegalCutOutException:
            return calculation_state_enum_i.CalculationState.ERROR_INVALID_CUT_OUT_DATA, \
                "The geojson is corrupted", None, None


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
            return calculation_state_enum_i.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY, \
                "The result folder for the current phase doesn't exist.", None, None

        if checkpoint_folder_path_last_phase is None:
            return calculation_state_enum_i.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY, \
                "The checkpoint folder of the last phase is not valid.", None, None

        if current_calculation_phase == calculation_phase_enum_i.CalculationPhase.GEO_DATA_PHASE:
            if checkpoint_folder_path_last_phase.exists():
                list_of_traffic_cell_checkpoints: Path = checkpoint_folder_path_last_phase

            else:
                return calculation_state_enum_i.CalculationState.ERROR_INVALID_OSM_DATA, \
                    "The osm data are not valid.", None, None

        else:
            if checkpoint_folder_path_last_phase.exists():
                list_of_traffic_cell_checkpoints: List[Path] = list(checkpoint_folder_path_last_phase.iterdir())

            else:
                return calculation_state_enum_i.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY, \
                    "The result folder for the last phase doesn't exist.", None, None

        return cut_out_dataframe, \
            checkpoint_folder_path_last_phase, \
            checkpoint_folder_path_current_phase, \
            list_of_traffic_cell_checkpoints
