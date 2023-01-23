from src.osm_configurator.control.calculation_controller_interface import ICalculationController

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase


class CalculationController(ICalculationController):
    __doc__ = ICalculationController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the CalculationController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def start_calculations(self, starting_phase: CalculationPhase):
        pass

    def get_calculation_state(self):
        pass

    def get_current_calculation_phase(self):
        pass

    def get_current_calculation_process(self):
        pass

    def cancel_calculations(self):
        pass
