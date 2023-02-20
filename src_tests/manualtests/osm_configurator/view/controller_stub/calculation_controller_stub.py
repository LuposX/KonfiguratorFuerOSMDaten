from src.osm_configurator.control.calculation_controller_interface import ICalculationController
from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState

from random import uniform


class CalculationControllerStub(ICalculationController):
    def start_calculations(self, starting_phase: CalculationPhase) -> CalculationState:
        """
        Returns:
            CalculationState: RUNNING, because the calculation started successfully
        """
        return CalculationState.RUNNING

    def get_calculation_state(self) -> CalculationState:
        return CalculationState.ENDED_SUCCESSFULLY

    def get_current_calculation_phase(self) -> CalculationPhase:
        return CalculationPhase.AGGREGATION_PHASE

    def get_current_calculation_process(self) -> float:
        """
        Returns:
            float: Random float between 0 and 1 representing the current calculation process
        """
        return uniform(0, 1)

    def cancel_calculations(self) -> bool:
        """
        Returns:
            bool: True, because it always works just as planned :)
        """
        return True
