from __future__ import annotations

import pandas as pd
import os
from pathlib import Path
from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
from src.osm_configurator.model.parser.custom_exceptions.illegal_cut_out_exception import IllegalCutOutException

import src.osm_configurator.model.parser.cut_out_parser as cut_out_parser
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.model_constants as model_constants
import src.osm_configurator.model.project.calculation.calculation_phase_utility as calculation_phase_utility

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from geopandas import GeoDataFrame
    from src.osm_configurator.model.parser.cut_out_parser import CutOutParser
    from typing import Tuple
    from pandas.core.series import Series
    from pandas import DataFrame


class AttractivityPhase(ICalculationPhase):
    """
    This calculation phase is responsible for calculating the attractivity attributes of the OSM-elements.
    For details see the method calculate().
    """
    def calculate(self, configuration_manager: ConfigurationManager) -> Tuple[CalculationState, str]:
        """Calculates the attractivity attributes of the osm-elements
        The calculation phase reads the data of the previous calculation phase. Now it calculates the attractivity
        attributes of every OSM-element. The attractivity attributes that are calculated for an osm-element are dependent
        on the category, the element belongs to. The value of an attractivity attribute is computed as a linear function
        with the previously computed attributes. The factors of this linear function are given in the configuration of
        the category. After the calculations are done, the results are stored on the hard-drive.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): The object containing all the configuration needed for execution.

        Returns:
            calculation_state_enum.CalculationState: The state of the calculation, after this phase finished its execution or failed trying so.
        """
        # Get the traffic cells
        geojson_path: Path = configuration_manager.get_cut_out_configuration().get_cut_out_path()
        co_parser: CutOutParser = cut_out_parser.CutOutParser()
        try:
            cells: GeoDataFrame = co_parser.parse_cutout_file(geojson_path)
        except IllegalCutOutException as err:
            return calculation_state_enum.CalculationState.ERROR_INVALID_CUT_OUT_DATA, str(err.args[0])

        # Iterate over all traffic cells and generate the attractivities
        index: int
        row: Series
        for index, row in cells:
            cell_name: str = row[model_constants.CL_TRAFFIC_CELL_NAME]
            self._calculate_attractivity_in_traffic_cell(cell_name, configuration_manager)

    def _calculate_attractivity_in_traffic_cell(self, cell_name: str, config_manager: ConfigurationManager) \
            -> Tuple[CalculationState, str]:
        # get the necessary path's
        reduction_folder: Path = calculation_phase_utility\
            .get_checkpoints_folder_path_from_phase(config_manager,
                                                    calculation_phase_enum.CalculationPhase.REDUCTION_PHASE)
        attractivity_folder: Path = calculation_phase_utility \
            .get_checkpoints_folder_path_from_phase(config_manager,
                                                    calculation_phase_enum.CalculationPhase.REDUCTION_PHASE)
        input_path: Path = Path(os.path.join(reduction_folder, cell_name, ".csv"))
        output_path: Path = Path(os.path.join(attractivity_folder, cell_name, ".csv"))
        # TODO: magic strings

        # Read and create data frames
        input_df: DataFrame = pd.read_csv(input_path)
        output_df: DataFrame = pd.DataFrame()

        return calculation_state_enum.CalculationState.RUNNING, "running"

    def _calculate_attractivity_for_element(self, element: Series, output_df: DataFrame,
                                            config_manager: ConfigurationManager) -> Tuple[CalculationState, str]:
        pass
