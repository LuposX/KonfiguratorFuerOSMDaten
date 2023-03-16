from __future__ import annotations

from enum import Enum

import src.osm_configurator.view.constants.frame_constants as frame_constants_i


class LabelConstants(Enum):
    """
    Holds all values needed to implement a standard Label-Constant
    """
    LABEL_CONSTANTS_CORNER_RADIUS = 0
    LABEL_CONSTANTS_FG_COLOR = "transparent"
    LABEL_CONSTANTS_TEXT_COLOR = "#000000"
    LABEL_CONSTANTS_TEXT_COLOR_POP_UP = "#000000"
    LABEL_CONSTANTS_ANCHOR_CENTER = "center"  # places text in the center
    LABEL_CONSTANTS_ANCHOR_LEFT = "w"  # places text on the left
    LABEL_TITLE_FG_COLOR = frame_constants_i.FrameConstants.HEAD_FRAME_FG_COLOR.value
    LABEL_CONSTANTS_PAD_Y = 4
    LABEL_CONSTANTS_PAD_X = 4
    