from src.osm_configurator.control.calculation_controller_interface import ICalculationController
from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState


class CalculationControllerStub(ICalculationController):
    def start_calculations(self, starting_phase: CalculationPhase) -> CalculationState:
        pass

    def get_calculation_state(self) -> CalculationState:
        pass

    def get_current_calculation_phase(self) -> CalculationPhase:
        pass

    def get_current_calculation_process(self) -> float:
        pass

    def cancel_calculations(self) -> bool:
        pass