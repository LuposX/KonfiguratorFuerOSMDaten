from __future__ import annotations

from abc import abstractmethod
from enum import Enum, unique


@unique
class CalculationMethodOfArea(Enum):
    """
    Enum Provides Calculation Method of the Area.
    """
    CALCULATE_SITE_AREA = "Calculate Site Area"
    CALCULATE_BUILDING_AREA = "Calculate Building Area"

    @abstractmethod
    def get_calculation_method(self):
        """
        Getter for the name of the Calculation Method.

        Returns:
            str: The name of the Calculation Method.
        """
        return self.value

    def equals(name: str) -> CalculationMethodOfArea | None:
        for method in CalculationMethodOfArea:
            if method.get_calculation_method() == name:
                return method
        return None

