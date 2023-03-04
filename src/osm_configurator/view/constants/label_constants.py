from __future__ import annotations

from enum import Enum


class LabelConstants(Enum):
    """
    Holds all values needed to implement a standard Label-Constant
    """
    LABEL_CONSTANTS_CORNER_RADIUS = 8
    LABEL_CONSTANTS_FG_COLOR = "transparent" #"#FFFFFF"
    LABEL_CONSTANTS_TEXT_COLOR = "#000000"
    LABEL_CONSTANTS_ANCHOR_CENTER = "center"  # places text in the center
    LABEL_CONSTANTS_ANCHOR_LEFT = "w" # places text on the left
    LABEL_TITLE_FG_COLOR = "#E8EAFD"
    LABEL_CONSTANTS_PADY = 4
    LABEL_CONSTANTS_PADX = 4
