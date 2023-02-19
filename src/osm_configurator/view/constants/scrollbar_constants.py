from __future__ import annotations

from enum import Enum

import src.osm_configurator.view.constants.button_constants as button_constants_i


class ScrollbarConstants(Enum):
    SCROLLBAR_CORNER_RADIUS = 8
    SCROLLBAR_BORDER_SPACING = 0
    SCROLLBAR_FG_COLOR = button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value
    SCROLLBAR_BUTTON_COLOR = button_constants_i.ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value
    SCROLLBAR_BUTTON_HOVER_COLOR = button_constants_i.ButtonConstants.BUTTON_HOVER_COLOR.value
