from abc import ABC, abstractmethod
import src.osm_configurator.model.project.calculation.calculation_state_enum
import src.osm_configurator.model.project.configuration.configuration_manager


class ICalculationPhase(ABC):
    """This class represents a calculation phase. A calculation phase is a single step in the big process of computing the final results. Calculation phases are executed after each other. A calculation phase consists out of the following 3 steps:\n
    1. Load needed results of previously computed calculation phases.\n
    2. Execute the computations of this calculation phase.\n
    3. Store the results of this computation phase, so the following execution phases can read it.
    """

    @abstractmethod
    def calculate(self, configuration_manager):
        """Performs the calculations of the calculation phase.
        This consists out of the following steps:\n
        1. Load needed results of previously computed calculation phases.\n
        2. Execute the computations of this calculation phase.\n
        3. Store the results of this computation phase, so the following execution phases can read it.\n

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): The ConfigurationManager, where the information about the configuration of the configuration is stored.

        Returns:
            calculation_state_enum.CalculationState: The state of the calculation, after this phase finished it's execution or failed trying so.
        """
        pass