from __future__ import annotations

from enum import Enum

from src.osm_configurator.view.constants.button_constants import ButtonConstants


class SwitchConstants(Enum):
    """
    Holds all values to implement a Switch according to the application's standards
    """

    SWITCH_CONSTANTS_CORNER_RADIUS = 8
    SWITCH_CONSTANTS_BORDER_WIDTH = 0
    SWITCH_CONSTANTS_FG_COLOR = "#FFFFFF"
    SWITCH_CONSTANTS_BORDER_COLOR = "#FFFFFF"
    SWITCH_CONSTANTS_PROGRESS_COLOR = "green"
    SWITCH_CONSTANTS_BUTTON_COLOR = ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value
    SWITCH_CONSTANTS_BUTTON_HOVER_COLOR = ButtonConstants.BUTTON_HOVER_COLOR.value
    SWITCH_CONSTANTS_HOVER_COLOR = ButtonConstants.BUTTON_HOVER_COLOR.value
    SWITCH_CONSTANTS_TEXT_COLOR = "#FFFFFF"
