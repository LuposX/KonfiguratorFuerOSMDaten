from __future__ import annotations

from enum import Enum

from src.osm_configurator.view.constants.button_constants import ButtonConstants


class CheckBoxConstants(Enum):
    CHECK_BOX_CORNER_RADIUS = 8
    CHECK_BOX_BORDER_WIDTH = 1
    CHECK_BOX_FG_COLOR = "#000000"
    CHECK_BOX_HOVER_COLOR = ButtonConstants.BUTTON_HOVER_COLOR.value
    CHECK_BOX_TEXT_COLOR = ButtonConstants.BUTTON_TEXT_COLOR.value
    CHECK_BOX_TEXT_COLOR_DISABLED = ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value
