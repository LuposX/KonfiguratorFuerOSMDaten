from __future__ import annotations

import os
from pathlib import Path

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
from src.osm_configurator.model.parser.custom_exceptions.illegal_cut_out_exception import IllegalCutOutException
import src.osm_configurator.model.parser.cut_out_parser as cut_out_parser
import src.osm_configurator.model.project.calculation.folder_path_calculator as folder_path_calculator_i
import src.osm_configurator.model.project.calculation.calculation_phase_enum as phase_enum

import src.osm_configurator.model.project.calculation.split_up_files as split_up_files
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.prepare_calculation_phase as prepare_calculation_phase_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.parser.cut_out_parser import CutOutParserInterface
    from geopandas.geodataframe import GeoDataFrame
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from src.osm_configurator.model.project.calculation.split_up_files import SplitUpFile
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion
    from typing import Tuple, Any, NamedTuple
    from src.osm_configurator.model.application.application_settings import ApplicationSettings
    from src.osm_configurator.model.project.calculation.prepare_calculation_information import \
        PrepareCalculationInformation


class GeoDataPhase(ICalculationPhase):
    """
    This Phase is responsible for splitting the file in smaller pieces, based on the traffic cells.
    """
    def get_calculation_phase_enum(self) -> CalculationPhase:
        return calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE

    def calculate(self, configuration_manager: ConfigurationManager,
                  application_manager: ApplicationSettings) -> NamedTuple[CalculationState, str]:
        """
        This method does:
        It splits the big input osm_data file into multiple smaller one. There are three main reason to do that
        - Organisational: Each file contains the osm elements of one previously defined traffic cell.
        This is more organized.
        - Parallelization: Splitting the file into multiple smaller files allows, for better
        parallelization, since every thread/process can work with one file.
        - RAM usage: RAM capacity is limited. We can't load one big file into the memory at once,
        so we need to split up the file.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): The object containing all the configuration needed for an execution.
            application_manager (ApplicationSettings): The settings of the application
        Returns:
            calculation_state_enum.CalculationState: The state of the calculation, after this phase finished its execution or failed trying so.
        """
        prepare_calc_obj: PrepareCalculationInformation = prepare_calculation_phase_i.PrepareCalculationPhase \
            .prepare_phase(configuration_manager_o=configuration_manager,
                           current_calculation_phase=calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE,
                           last_calculation_phase=calculation_phase_enum.CalculationPhase.NONE)

        # Return if we got an error
        if prepare_calc_obj.get_calculation_state() is not None:
            return super()._RETURN_VALUE(prepare_calc_obj.get_calculation_state(), prepare_calc_obj.get_error_message())

        # Split up files
        splitter: SplitUpFile = split_up_files.SplitUpFile(
            origin_path=prepare_calc_obj.get_checkpoint_folder_path_last_phase(),
            result_folder=prepare_calc_obj.get_checkpoint_folder_path_current_phase())
        result: bool = splitter.split_up_files(prepare_calc_obj.get_cut_out_dataframe())

        if result:
            return super()._RETURN_VALUE(calculation_state_enum.CalculationState.RUNNING, "The calculation is running")
        else:
            return super()._RETURN_VALUE(calculation_state_enum.CalculationState.ERROR_INVALID_OSM_DATA,
                                     "An error accured while reading the OSM data")
