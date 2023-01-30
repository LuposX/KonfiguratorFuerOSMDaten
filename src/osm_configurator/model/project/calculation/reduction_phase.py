from __future__ import annotations

import src.osm_configurator.model.project.configuration.configuration_manager
import src.osm_configurator.model.project.calculation.calculation_state_enum

import src.osm_configurator.model.project.calculation.calculation_phase_utility as calculation_phase_utility_i
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum_i
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion_i
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum_i

from pathlib import Path

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Tuple, List
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion


class ReductionPhase(ICalculationPhase):
    """
    This calculation phase is responsible for reducing bigger OSM-elements on single coordinates and for generating
    the values of the attributes for alle OSM-elements.
    For details see the method calculate().
    """
    def calculate(self, configuration_manager_o: ConfigurationManager) -> Tuple[CalculationState, str]:
        """
        Reduces OSM-elements on single points and calculates their attributes.
        The calculation phase reads the data of the previous calculation phase. OSM-elements that are not just a single
        node, must be reduced on one coordinate. For that the centre of the given shape is calculated and set as the
        new coordinate. This calculation phase does also calculate the attributes of every OSM-element. There is no
        generic form for calculation attributes, every attribute has an individual calculation. If a method of
        calculation is not possible or if the user turned it off, the value of the attributes is defined by the
        default value list of the category. The value is given by the highest priority entry of the default value
        list, that matches the osm-element. After the calculations are done, the results are stored on the hard-drive.

        Args:
            configuration_manager_o (configuration_manager.ConfigurationManager): The object containing all the configuration required for an execution.

        Returns:
              Tuple[CalculationState, str]: The state of the calculation after this phase finished its execution or failed trying so and a string which describes what happened e.g. an error.
        """

        # Get path to the results of the last Phase
        checkpoint_folder_path_last_phase: Path = calculation_phase_utility_i.get_checkpoints_folder_path_from_phase(
            configuration_manager_o,
            calculation_phase_enum_i.CalculationPhase.TAG_FILTER_PHASE)

        # Get path to the results of the current Phase
        checkpoint_folder_path_current_phase: Path = calculation_phase_utility_i.get_checkpoints_folder_path_from_phase(
            configuration_manager_o,
            calculation_phase_enum_i.CalculationPhase.REDUCTION_PHASE)

        # Prepare result folder
        deleter: FileDeletion = file_deletion_i.FileDeletion()
        deleter.reset_folder(checkpoint_folder_path_current_phase)

        # check if the folder exist
        if checkpoint_folder_path_last_phase.exists() and checkpoint_folder_path_current_phase.exists():
            list_of_traffic_cell_checkpoints: List = list(checkpoint_folder_path_last_phase.iterdir())
        else:
            return calculation_state_enum_i.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY, ""





