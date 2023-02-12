from __future__ import annotations

from enum import Enum


class ButtonConstants(Enum):
    """
    This Enum holds the constant values to create a standard button
    """
    BUTTON_CORNER_RADIUS = 8
    BUTTON_BORDER_WIDTH = 0
    BUTTON_FG_COLOR_ACTIVE = "#D9D9D9"
    BUTTON_FG_COLOR_DISABLED = "#7E8394"
    BUTTON_FG_COLOR_RED = "EA5353"  # FG-Color if button is a cancel / delete button
    BUTTON_FG_COLOR_YELLOW = "FFB800"
    BUTTON_FG_COLOR_GREEN = "40B135"
    BUTTON_HOVER_COLOR = "#7E8394"
    BUTTON_BORDER_COLOR = "#000000"
    BUTTON_TEXT_COLOR = "#000000"
    BUTTON_TEXT_COLOR_DISABLED = "#000000"
