from __future__ import annotations

from enum import Enum


class CalculationStates(Enum):
    """
    This Enum holds all calculation phases
    """
    DATA_INPUT_AND_GEO_FILTER = 0
    TAG_FILTER = 1
    REDUCTION = 2
    ATTRACTIVITY = 3
    AGGREGATION = 4
