import src.osm_configurator.model.project.calculation.configuration_manager
import src.osm_configurator.model.project.calculation.calculation_phase_enum


class CalculationManager:
    """
    The CalculationManager manages the calculation of the Project. The Calculation are distributed on the calculation phases, which are also managed by the Calculation Controller.
    """

    def __init__(self, configuration_manager):
        """Gets called when we first create an object of this class, it saves all information it needs for
        managing the calculations.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): Saves all information required to configure the calculation.
        """
        pass

    def cancel_calculation(self):
        """This method will cancel an ongoing calculation.
        A calculation consists of an :class:`<model.CalculationPhase>`, that will be interrupted.

        Returns:
            bool: true if it succeeded, false if something goes wrong, or no calculation is going on.
        """
        pass

    def _validate_starting_point(self, starting_point):
        """Validates the correctness of the Staring Point.

        Args:
            starting_point (calculation_phase_enum.CalculationPhase): The starting point that is observed

        Returns:
            calculation_phase_enum.CalculationState: The state of the calculation, after the starting point was verified.
        """
        pass

    def start_calculation(self, starting_point):
        """Starts the calculation.
        Distributes the calculations to the calculation phases.

        Args:
            starting_point (calculation_phase_enum.CalculationPhase): The starting phase of the calculation. The calculations wll start beginning in this phase

        Returns:
            calculation_phase_enum.CalculationState: The state of the calculation, after trying to start the calculations.
        """
        pass
