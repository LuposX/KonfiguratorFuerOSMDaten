from __future__ import annotations

import src.osm_configurator.model.project.configuration.configuration_manager
import src.osm_configurator.model.project.calculation.calculation_phase_enum


class CalculationManager:
    """
    The CalculationManager manages the calculation of the Project. The Calculation are distributed on the calculation
    phases which are also managed by the CalculationController.
    """

    def __init__(self, configuration_manager):
        """
        Gets called when we first create an object of this class. It saves all information it needs for
        managing the calculations.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): Saves all information required to configure the calculation.
        """
        pass

    def cancel_calculation(self):
        """
        This method will cancel an ongoing calculation.
        A calculation consists of an CalculationPhase, that will be interrupted.

        Returns:
            bool: True if it is successful and false if something goes wrong, or no calculation is going on.
        """
        pass

    def _validate_starting_point(self, starting_point):
        """
        Validates the correctness of the starting point.

        Args:
            starting_point (calculation_phase_enum.CalculationPhase): The starting point that is observed.

        Returns:
            calculation_phase_enum.CalculationState: The state of the calculation after the starting point was verified.
        """
        pass

    def start_calculation(self, starting_point):
        """
        Starts the calculation.
        Distributes the calculations to the calculation phases.

        Args:
            starting_point (calculation_phase_enum.CalculationPhase): The starting phase of the calculation. The calculations start from this phase.

        Returns:
            calculation_phase_enum.CalculationState: The state of the calculation, after trying to start the calculations.
        """
        pass
