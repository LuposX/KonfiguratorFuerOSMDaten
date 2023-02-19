from __future__ import annotations

from enum import Enum

from src.osm_configurator.view.constants.button_constants import ButtonConstants


class SegmentedButtonConstants(Enum):
    SEGMENTED_BUTTON_CORNER_RADIUS = 8
    SEGMENTED_BUTTON_FG_COLOR = "#CED2FC"  # Pimmelfarbe
    SEGMENTED_BUTTON_SELECTED_COLOR = ButtonConstants.BUTTON_FG_COLOR_DISABLED.value
    SEGMENTED_BUTTON_SELECTED_HOVER_COLOR = ButtonConstants.BUTTON_HOVER_COLOR.value
    SEGMENTED_BUTTON_UNSELECTED_COLOR = ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value
    SEGMENTED_BUTTON_UNSELECTED_HOVER_COLOR = ButtonConstants.BUTTON_HOVER_COLOR.value
    SEGMENTED_BUTTON_TEXT_COLOR = ButtonConstants.BUTTON_TEXT_COLOR.value
    SEGMENTED_BUTTON_TEXT_COLOR_DISABLED = ButtonConstants.BUTTON_TEXT_COLOR_DISABLED.value
