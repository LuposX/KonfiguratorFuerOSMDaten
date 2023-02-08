from __future__ import annotations

import src.osm_configurator.model.project.calculation.geo_data_phase as geo_data_phase
import src.osm_configurator.model.project.calculation.tag_filter_phase as tag_filter_phase
import src.osm_configurator.model.project.calculation.reduction_phase as reduction_phase
import src.osm_configurator.model.project.calculation.attractivity_phase as attractivity_phase
import src.osm_configurator.model.project.calculation.aggregation_phase as aggregation_phase

import src.osm_configurator.model.project.calculation.calculation_state_enum  as calculation_state_enum
import multiprocessing

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Tuple
    from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from multiprocessing import Process
    from multiprocessing import SimpleQueue


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
        self._calculation_state = (calculation_state_enum.CalculationState.NOT_STARTED_YET,
                                   "The calculation has not started yet")
        self._process: Process = multiprocessing.Process()
        self._message_queue: SimpleQueue = multiprocessing.SimpleQueue()

    def cancel_calculation(self) -> bool:
        """
        This method will cancel an ongoing calculation.
        A calculation consists of an CalculationPhase, that will be interrupted.

        Returns:
            bool: True if it is successful and false if something goes wrong, or no calculation is going on.
        """
        if self._process.is_alive():
            self._process.terminate()
            self._calculation_state = (calculation_state_enum.CalculationState.CANCELED, "The calculation was canceled")
            return True
        return False

    def get_calculation_state(self) -> Tuple[CalculationState, str]:
        """
        Returns the state of the current calculations.
        Returns:
            Tuple[CalculationState, str]: The state of teh current calculation together with a descriptive string
        """
        self._update_calculation_state()
        return self._calculation_state

    def _update_calculation_state(self):
        while not self._message_queue.empty():
            self._new_state = self._message_queue.get()

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

        if self._process.is_alive():
            self._process.terminate()

        self._process = multiprocessing.Process(target=self._do_calculations, args=(starting_point, self._message_queue))
        self._process.start()

        return calculation_state_enum.CalculationState.RUNNING, "The calculations are currently running"

    def _do_calculations(self, starting_point: CalculationPhase, message_queue: SimpleQueue):
        starting_index: int = 0
        while self._phases[starting_index].get_calculation_phase_enum() != starting_point:
            starting_index += 1

        current_index: int = starting_index
        result: Tuple[CalculationState, str] = calculation_state_enum.CalculationState.RUNNING
        while current_index < len(self._phases) and result[0] == calculation_state_enum.CalculationState.RUNNING:
            result = self._phases[current_index].calculate(self._config_manager)
            message_queue.put(result)

        if result[0] == calculation_state_enum.CalculationState.RUNNING:
            message_queue.put((calculation_state_enum.CalculationState.ENDED_SUCCESSFULLY,
                               "The calculation have finished successfully"))
