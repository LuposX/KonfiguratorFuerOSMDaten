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
import src.osm_configurator.model.project.calculation.folder_path_calculator as folder_path_calculator
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

from src.osm_configurator.model.parser.custom_exceptions.category_exception import CategoryException

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.configuration.category import Category
    from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion
    from geopandas import GeoDataFrame
    from src.osm_configurator.model.parser.cut_out_parser import CutOutParser
    from typing import Tuple
    from typing import List
    from typing import Dict
    from pandas.core.series import Series
    from pandas import DataFrame
    from src.osm_configurator.model.application.application_settings import ApplicationSettings


class AttractivityPhase(ICalculationPhase):
    """
    This calculation phase is responsible for calculating the attractivity attributes of the OSM-elements.
    For details see the method calculate().
    """
    def get_calculation_phase_enum(self) -> CalculationPhase:
        return calculation_phase_enum.CalculationPhase.ATTRACTIVITY_PHASE

    def calculate(self, configuration_manager: ConfigurationManager,
                  application_manager: ApplicationSettings) -> Tuple[CalculationState, str]:
        """Calculates the attractivity attributes of the osm-elements
        The calculation phase reads the data of the previous calculation phase. Now it calculates the attractivity
        attributes of every OSM-element. The attractivity attributes that are calculated for an osm-element are dependent
        on the category, the element belongs to. The value of an attractivity attribute is computed as a linear function
        with the previously computed attributes. The factors of this linear function are given in the configuration of
        the category. After the calculations are done, the results are stored on the hard-drive.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): The object containing all the configuration needed for execution.
            application_manager (ApplicationSettings): The settings of the application

        Returns:
            calculation_state_enum.CalculationState: The state of the calculation, after this phase finished its execution or failed trying so.
        """
        # Get the traffic cells
        geojson_path: Path = configuration_manager.get_cut_out_configuration().get_cut_out_path()
        co_parser: CutOutParser = cut_out_parser.CutOutParser()

        if geojson_path is None:
            return calculation_state_enum.CalculationState.ERROR_INVALID_CUT_OUT_DATA, "Invalid geojson file"

        try:
            cells: GeoDataFrame = co_parser.parse_cutout_file(geojson_path)
        except IllegalCutOutException as err:
            return calculation_state_enum.CalculationState.ERROR_INVALID_CUT_OUT_DATA, str(err.args[0])

        # Delete result files
        result_folder: Path = folder_path_calculator.FolderPathCalculator().get_checkpoints_folder_path_from_phase(
            configuration_manager, calculation_phase_enum.CalculationPhase.ATTRACTIVITY_PHASE)
        deleter: FileDeletion = file_deletion.FileDeletion()
        deleter.reset_folder(result_folder)

        # Iterate over all traffic cells and generate the attractivities
        index: int
        row: Series
        for index, row in cells.iterrows():
            cell_name: str = row[model_constants.CL_TRAFFIC_CELL_NAME]
            result: calculation_state_enum
            msg: str
            result, msg = self._calculate_attractivity_in_traffic_cell(cell_name, configuration_manager)
            if result != calculation_state_enum.CalculationState.RUNNING:
                return result, msg

        return calculation_state_enum.CalculationState.RUNNING, "running"

    def _calculate_attractivity_in_traffic_cell(self, cell_name: str, config_manager: ConfigurationManager) \
            -> Tuple[CalculationState, str]:
        # get the necessary path's
        reduction_folder: Path = folder_path_calculator.FolderPathCalculator()\
            .get_checkpoints_folder_path_from_phase(config_manager,
                                                    calculation_phase_enum.CalculationPhase.REDUCTION_PHASE)
        attractivity_folder: Path = folder_path_calculator.FolderPathCalculator() \
            .get_checkpoints_folder_path_from_phase(config_manager,
                                                    calculation_phase_enum.CalculationPhase.ATTRACTIVITY_PHASE)
        input_path: Path = Path(os.path.join(reduction_folder, cell_name + ".csv"))
        output_path: Path = Path(os.path.join(attractivity_folder, cell_name + ".csv"))

        # Read and create data frames
        input_df: DataFrame = pd.read_csv(input_path)
        output_data: List[Dict[str, float]] = []

        # Iterate over all elements in this cell
        index: int
        element: Series
        for index, element in input_df.iterrows():
            try:
                self._calculate_attractivity_for_element(element, output_data,
                                                         config_manager.get_category_manager().get_categories())
            except CategoryException as err:
                return calculation_state_enum.CalculationState.ERROR_INVALID_CATEGORIES, err.args[0]

        # Save results as csv
        output_df: DataFrame = pd.DataFrame(output_data)
        output_df.to_csv(output_path)

        return calculation_state_enum.CalculationState.RUNNING, "running"

    def _calculate_attractivity_for_element(self, element: Series, output_data: List,
                                            category_list: List[Category]):
        category_name: str = element["category"]
        category: Category = self._get_category_by_name(category_name, category_list)

        new_entry: Dict[str, float] = {}

        attractivity: AttractivityAttribute
        for attractivity in category.get_attractivity_attributes():
            value: float = attractivity.get_base_factor()
            attribute: Attribute
            for attribute in attribute_enum.Attribute:
                value += attractivity.get_attribute_factor(attribute) * element[attribute.get_name()]
            new_entry[attractivity.get_attractivity_attribute_name()] = value

        output_data.append(new_entry)

    def _get_category_by_name(self, category_name: str, category_list: List[Category]) -> Category:
        list_of_categories_with_name: List[Category] = [cat for cat in category_list if cat.get_category_name() == category_name]
        assert len(list_of_categories_with_name) <= 1
        if len(list_of_categories_with_name) == 0:
            raise CategoryException("An OSM-element has a category that is not registered in the configuration")

        return list_of_categories_with_name[0]
