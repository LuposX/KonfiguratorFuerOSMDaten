from __future__ import annotations

from enum import Enum

from src.osm_configurator.view.constants.button_constants import ButtonConstants


class SwitchConstants(Enum):
    """
    Holds all values to implement a Switch according to the application's standards
    """

    SWITCH_CONSTANTS_CORNER_RADIUS = 8
    SWITCH_CONSTANTS_BORDER_WIDTH = 0

    SWITCH_CONSTANTS_FG_COLOR_ACTIVE = "#81889D"
    SWITCH_CONSTANTS_FG_COLOR_DISABLED = "#D9D9D9"
    SWITCH_CONSTANTS_BORDER_COLOR = "#000000"
    SWITCH_CONSTANTS_PROGRESS_COLOR_ACTIVE = "#81889D"
    SWITCH_CONSTANTS_PROGRESS_COLOR_DISABLED = "#D9D9D9"
    SWITCH_CONSTANTS_BUTTON_COLOR = "#33363F"

    SWITCH_CONSTANTS_BUTTON_COLOR_DISABLED = "#656B7E"
    SWITCH_CONSTANTS_BUTTON_HOVER_COLOR = "#8F96AA"
    SWITCH_CONSTANTS_HOVER_COLOR = ButtonConstants.BUTTON_HOVER_COLOR.value
    SWITCH_CONSTANTS_TEXT_COLOR = ButtonConstants.BUTTON_TEXT_COLOR.value

    SWITCH_CONSTANTS_BASE_HEIGHT = 42
    SWITCH_CONSTANTS_BASE_WIDTH = 240
