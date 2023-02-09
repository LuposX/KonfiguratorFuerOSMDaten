from __future__ import annotations


from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Tuple
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager


class ICalculationPhase(ABC):
    """This class represents a calculation phase. A calculation phase is a single step in the big process of computing
    the final results. Calculation phases are executed after each other. A calculation phase consists of the
    following 3 steps:\n
    1. Load needed results of previously computed calculation phases.\n
    2. Execute the computations of this calculation phase.\n
    3. Store the results of this computation phase so the following execution phases can read it.
    """

    @abstractmethod
    def calculate(self, configuration_manager_o: ConfigurationManager) -> Tuple[CalculationState, str]:
        """
        Performs the calculations of the calculation phase.
        This consists of the following steps:\n
        1. Load needed results of previously computed calculation phases.\n
        2. Execute the computations of this calculation phase.\n
        3. Store the results of this computation phase so the following execution phases can read it.\n

        Args:
            configuration_manager_o (ConfigurationManager): The ConfigurationManager where the information about the configuration of the configuration is stored.

        Returns:
            Tuple[CalculationState, str]: The state of the calculation after this phase finished its execution or failed trying so and a string which describes what happend e.g. a error.
        """
        pass

    @abstractmethod
    def get_calculation_phase_enum(self) -> CalculationPhase:
        """
        Returns the CalculationPhase that corresponds to this ICalculationPhase.
        Returns:
            CalculationPhase: the CalculationPhase that corresponds to this ICalculationPhase.
        """
        pass
