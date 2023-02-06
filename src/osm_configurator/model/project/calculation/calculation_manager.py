from __future__ import annotations

import src.osm_configurator.model.project.calculation.geo_data_phase as geo_data_phase
import src.osm_configurator.model.project.calculation.tag_filter_phase as tag_filter_phase
import src.osm_configurator.model.project.calculation.reduction_phase as reduction_phase
import src.osm_configurator.model.project.calculation.attractivity_phase as attractivity_phase
import src.osm_configurator.model.project.calculation.aggregation_phase as aggregation_phase

import src.osm_configurator.model.project.calculation.calculation_state_enum  as calculation_state_enum
import threading

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Tuple
    from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from threading import Thread


class CalculationManager:
    """
    The CalculationManager manages the calculation of the Project. The Calculation are distributed on the calculation
    phases which are also managed by the CalculationController.
    """

    def __init__(self, configuration_manager: ConfigurationManager):
        """
        Gets called when we first create an object of this class. It saves all information it needs for
        managing the calculations.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): Saves all information required to configure the calculation.
        """
        self._config_manager = configuration_manager
        self._phases: List[ICalculationPhase] = [
            geo_data_phase.GeoDataPhase(),
            tag_filter_phase.TagFilterPhase(),
            reduction_phase.ReductionPhase(),
            attractivity_phase.AttractivityPhase(),
            aggregation_phase.AggregationPhase()
        ]
        self._calculation_state = calculation_state_enum.CalculationState.NOT_STARTED_YET
        self._calculation_message = "The calculation has not started yet"

    def cancel_calculation(self) -> bool:
        """
        This method will cancel an ongoing calculation.
        A calculation consists of an CalculationPhase, that will be interrupted.

        Returns:
            bool: True if it is successful and false if something goes wrong, or no calculation is going on.
        """
        pass

    def _validate_starting_point(self, starting_point: CalculationPhase) -> Tuple[CalculationState, str]:
        """
        Validates the correctness of the starting point.

        Args:
            starting_point (calculation_phase_enum.CalculationPhase): The starting point that is observed.

        Returns:
            calculation_phase_enum.CalculationState, str: The state of the calculation after the starting point was verified.
        """
        pass

    def start_calculation(self, starting_point: CalculationPhase) -> Tuple[CalculationState, str]:
        """
        Starts the calculation.
        Distributes the calculations to the calculation phases.

        Args:
            starting_point (calculation_phase_enum.CalculationPhase): The starting phase of the calculation. The calculations start from this phase.

        Returns:
            calculation_phase_enum.CalculationState, str: The state of the calculation, after trying to start the calculations.
        """
        if len([x for x in self._phases if x.get_calculation_phase_enum() == starting_point]) != 1:
            raise ValueError("There is not a unique ICalculationPhase with the given staring point")

        thread: Thread = threading.Thread(target=self._do_calculations, args=[starting_point])
        thread.start()

    def _do_calculations(self, starting_point: CalculationPhase):
        starting_index: int = 0
        while self._phases[starting_index].get_calculation_phase_enum() != starting_point:
            starting_index += 1

        current_index: int = starting_index
        result: Tuple[CalculationState, str] = calculation_state_enum.CalculationState.RUNNING
        while current_index < len(self._phases) and result[0] == calculation_state_enum.CalculationState.RUNNING:
            result = self._phases[current_index].calculate(self._config_manager)
            self._calculation_state = result[0]
            self._calculation_message = result[1]

        if result[0] == calculation_state_enum.CalculationState.RUNNING:
            self._calculation_state = calculation_state_enum.CalculationState.ENDED_SUCCESSFULLY
            self._calculation_message = "The calculation have finished successfully"
