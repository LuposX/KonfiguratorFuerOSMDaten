from __future__ import annotations

import os.path
from pathlib import Path

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
from src.osm_configurator.model.parser.custom_exceptions.illegal_cut_out_exception import IllegalCutOutException
import src.osm_configurator.model.parser.cut_out_parser as cut_out_parser
import src.osm_configurator.model.project.calculation.calculation_phase_utility as calc_util
import src.osm_configurator.model.project.calculation.calculation_phase_enum as phase_enum

import src.osm_configurator.model.project.calculation.split_up_files as split_up_files
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.parser.cut_out_parser import CutOutParserInterface
    from pathlib import Path
    from geopandas.geodataframe import GeoDataFrame
    from src.osm_configurator.model.project.calculation.split_up_files import SplitUpFile
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion


class GeoDataPhase(ICalculationPhase):
    """
    This Phase is responsible for splitting the file in smaller pieces, based on the traffic cells.
    """

    def calculate(self, configuration_manager: ConfigurationManager) -> CalculationState:
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
        Returns:
            calculation_state_enum.CalculationState: The state of the calculation after this phase finished its execution or failed trying so.
        """
        # Get data frame of geojson
        parser: CutOutParserInterface = cut_out_parser.CutOutParser()
        geojson_path: Path = configuration_manager.get_cut_out_configuration().get_cut_out_path()

        if not os.path.exists(geojson_path):
            return calculation_state_enum.CalculationState.ERROR_INVALID_CUT_OUT_DATA

        try:
            dataframe: GeoDataFrame = parser.parse_cutout_file(geojson_path)
        except IllegalCutOutException as err:
            return calculation_state_enum.CalculationState.ERROR_INVALID_CUT_OUT_DATA

        # Get folder, where to store the files
        cp_folder: Path = calc_util.get_checkpoints_folder_path_from_phase(configuration_manager,
                                                                           phase_enum.CalculationPhase.GEO_DATA_PHASE)

        # Get folder, where to read the OSM-data from
        osm_path: Path = configuration_manager.get_osm_data_configuration().get_osm_data()
        if not os.path.exists(osm_path):
            return calculation_state_enum.CalculationState.ERROR_INVALID_OSM_DATA

        # Prepare result folder
        deleter: FileDeletion = file_deletion.FileDeletion()
        deleter.reset_folder(cp_folder)

        # Split up files
        splitter: SplitUpFile = split_up_files.SplitUpFile(osm_path, cp_folder)
        result: bool = splitter.split_up_files(dataframe)

        if result:
            return calculation_state_enum.CalculationState.RUNNING
        else:
            return calculation_state_enum.CalculationState.ERROR_INVALID_OSM_DATA

