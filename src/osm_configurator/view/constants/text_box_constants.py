from __future__ import annotations

from enum import Enum

from src.osm_configurator.view.constants.button_constants import ButtonConstants


class TextBoxConstants(Enum):
    """
    Holds all constant-values to implement a Text-Box according to this application's standards
    """
    TEXT_BOX_CORNER_RADIUS = 8
    TEXT_BOX_BORDER_WITH = 1
    TEXT_BOX_FG_COLOR = ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value
    TEXT_BOX_BORDER_COLOR = "#000000"
    TEXT_BOX_TEXT_COLOR = ButtonConstants.BUTTON_TEXT_COLOR.value
