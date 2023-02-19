from src.osm_configurator.control.calculation_controller_interface import ICalculationController

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase

    from typing import Tuple


class CalculationController(ICalculationController):
    __doc__ = ICalculationController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the CalculationController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        self._model: IApplication = model

    def start_calculations(self, starting_phase: CalculationPhase) -> Tuple[CalculationState, str]:
        return self._model.get_active_project().get_calculation_manager().start_calculation(starting_phase)

    def get_calculation_state(self) -> Tuple[CalculationState, str]:
        return self._model.get_active_project().get_calculation_manager().get_calculation_state()

    def get_current_calculation_phase(self) -> CalculationPhase:
        return self._model.get_active_project().get_calculation_manager().get_current_calculation_phase()

    def get_current_calculation_process(self) -> float:
        return self._model.get_active_project().get_calculation_manager().get_calculation_progress()

    def cancel_calculations(self) -> bool:
        return self._model.get_active_project().get_calculation_manager().cancel_calculation()
