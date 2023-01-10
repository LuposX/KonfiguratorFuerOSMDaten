from enum import Enum, unique


@unique
class CalculationMethodOfArea(Enum):
    """
    Enum Provides Calculation Method of the Area
    """
    CALCULATE_SITE_AREA = "Calculate Site Area"
    CALCULATE_BUILDING_AREA = "Calculate Building Area"
