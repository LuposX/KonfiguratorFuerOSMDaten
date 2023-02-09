from __future__ import annotations

from enum import Enum


class LabelConstants(Enum):
    """
    Holds all values needed to implement a standard Label-Constant
    """
    LABEL_CONSTANTS_CORNER_RADIUS = 0
    LABEL_CONSTANTS_FG_COLOR = "FFFFFF"
    LABEL_CONSTANTS_TEXT_COLOR = "000000"
    LABEL_CONSTANTS_ANCHOR = "center"  # defines where the text is placed
