from __future__ import annotations

from enum import Enum

from src.osm_configurator.view.constants.button_constants import ButtonConstants


class EntryConstants(Enum):
    """
    Holds all constants to define an Entry after the applications standards
    """
    ENTRY_CORNER_RADIUS = 8
    ENTRY_FG_COLOR = ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value
    ENTRY_TEXT_COLOR = ButtonConstants.BUTTON_TEXT_COLOR.value
    ENTRY_TEXT_COLOR_INVALID = "#EA5353"

    ENTRY_BASE_HEIGHT_BIG = 60
    ENTRY_BASE_HEIGHT_SMALL = 22

