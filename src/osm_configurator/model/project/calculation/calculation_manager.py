from __future__ import annotations

import src.osm_configurator.model.project.calculation.geo_data_phase as geo_data_phase
import src.osm_configurator.model.project.calculation.tag_filter_phase as tag_filter_phase
import src.osm_configurator.model.project.calculation.reduction_phase as reduction_phase
import src.osm_configurator.model.project.calculation.attractivity_phase as attractivity_phase
import src.osm_configurator.model.project.calculation.aggregation_phase as aggregation_phase

import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import multiprocessing

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Tuple
    from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.application.application_settings import ApplicationSettings
    from multiprocessing import Process
    from multiprocessing import SimpleQueue


class CalculationManager:
    """
    The CalculationManager manages the calculation of the Project. The Calculation are distributed on the calculation
    phases which are also managed by the CalculationController.
    """

    def __init__(self, configuration_manager: ConfigurationManager, application_manager: ApplicationSettings):
        """
        Gets called when we first create an object of this class. It saves all information it needs for
        managing the calculations.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): Saves all information required to configure the calculation.
            application_manager (ApplicationSettings): Needed for some settings on how we calculate.
        """
        self._config_manager = configuration_manager
        self._phases: List[ICalculationPhase] = [
            geo_data_phase.GeoDataPhase(),
            tag_filter_phase.TagFilterPhase(),
            reduction_phase.ReductionPhase(),
            attractivity_phase.AttractivityPhase(),
            aggregation_phase.AggregationPhase()
        ]
        self._calculation_state: Tuple[CalculationState, str] = (calculation_state_enum.CalculationState.NOT_STARTED_YET,
                                   "The calculation is starting...")
        self._process: Process = multiprocessing.Process()
        self._state_queue: SimpleQueue = multiprocessing.SimpleQueue()
        self._phase_queue: SimpleQueue = multiprocessing.SimpleQueue()
        self._current_phase: CalculationPhase = calculation_phase_enum.CalculationPhase.NONE
        self._progress = 0

        self._application_manager = application_manager

    def cancel_calculation(self) -> bool:
        """
        This method will cancel an ongoing calculation.
        A calculation consists of an CalculationPhase, that will be interrupted.

        Returns:
            bool: True if it is successful and false if something goes wrong, or no calculation is going on.
        """
        self._current_phase: CalculationPhase = calculation_phase_enum.CalculationPhase.NONE
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
        while not self._state_queue.empty():
            self._calculation_state = self._state_queue.get()

    def start_calculation(self, starting_point: CalculationPhase) -> Tuple[CalculationState, str]:
        """
        Starts the calculation.
        Distributes the calculations to the calculation phases.

        Args:
            starting_point (calculation_phase_enum.CalculationPhase): The starting phase of the calculation. The calculations start from this phase.

        Returns:
            calculation_phase_enum.CalculationState, str: The state of the calculation, after trying to start the calculations.
        """
        # Check if there is exactly one phase with the given starting point
        if len([x for x in self._phases if x.get_calculation_phase_enum() == starting_point]) != 1:
            raise ValueError("There is not a unique ICalculationPhase with the given staring point")

        # Terminate all calculations that are running till now
        if self._process.is_alive():
            self._process.terminate()

        # Start process that executes _do_calculations
        self._process = multiprocessing.Process(target=self._do_calculations,
                                                args=(starting_point, self._state_queue, self._phase_queue))
        self._process.start()

        return calculation_state_enum.CalculationState.RUNNING, "The calculations are currently running"

    def get_current_calculation_phase(self) -> CalculationPhase:
        """
        Returns the calculation phase the calculations are in

        Returns:
            CalculationPhase: the calculation phase the calculations are in
        """
        self._update_calculation_phase()
        return self._current_phase

    def _update_calculation_phase(self):
        while not self._phase_queue.empty():
            self._current_phase = self._phase_queue.get()

    def get_calculation_progress(self) -> float:
        """
        Returns an approximation of the progress of the calculations in the currently selected project.
        The progress is given as a number between 0 and 1, where 0 indicates that the calculation has not started yet
        and 1 indicates, that the calculations are done. The approximation is done by dividing the number of done
        phases by the number of total phases

        Returns:
            float: The value of the approximation.
        """
        self._update_calculation_phase()
        return (self._current_phase.get_order() - 1) / len(self._phases)

    def _do_calculations(self, starting_point: CalculationPhase, state_queue: SimpleQueue, phase_queue: SimpleQueue):
        # Get index of the phase where the calculation should start
        starting_index: int = 0
        while self._phases[starting_index].get_calculation_phase_enum() != starting_point:
            starting_index += 1

        # Beginning  at the starting point, calculate all following phases
        current_index: int = starting_index
        result: Tuple[CalculationState, str] = calculation_state_enum.CalculationState.RUNNING, "The calculation is running"
        while current_index < len(self._phases) and result[0] == calculation_state_enum.CalculationState.RUNNING:
            phase_queue.put(self._phases[current_index].get_calculation_phase_enum())
            result = self._phases[current_index].calculate(self._config_manager, self._application_manager)
            state_queue.put(result)  # Put the return value of the phases in the queue to the main process
            current_index += 1

        phase_queue.put(calculation_phase_enum.CalculationPhase.NONE)

        # If all calculation is done and the calculations aer still running: switch state to ENDED_SUCCESSFULLY
        if result[0] == calculation_state_enum.CalculationState.RUNNING:
            state_queue.put((calculation_state_enum.CalculationState.ENDED_SUCCESSFULLY,
                               "The calculation have finished successfully"))
