from __future__ import annotations

from enum import Enum


class ViewConstants(Enum):
    """
    This Enums holds the necessary constants to remove code duplicates and
    keep the view running
    """

    # PopUp Constants

    POPUPSIZE = "400x200"

    # MainWindow Constants
    WINDOW_TITLE = "OSM-Configurator"
    MAIN_WINDOW_HEIGHT_MINIMUM = 800
    MAIN_WINDOW_WIDTH_MINIMUM = 1200
    MAIN_WINDOW_HEIGHT = 800
    MAIN_WINDOW_WIDTH = 1200

    # Frame Constants
    HEAD_FRAME_HEIGHT = 100
    HEAD_FRAME_WIDTH = 1200
    FOOT_FRAME_HEIGHT = 50
    FOOT_FRAME_WIDTH = 1200
    MIDDLE_FRAME_HEIGHT = 600
    MIDDLE_FRAME_WIDTH = 1200
    FULL_FRAME_HEIGHT = 800
    FULL_FRAME_WIDTH = 1200

    FRAME_CORNER_RADIUS = 1
    HEAD_FRAME_FG_COLOR = "#FFFFFF"
    FOOT_FRAME_FG_COLOR = "#FFFFFF"
    MIDDLE_FRAME_FG_COLOR = "#FFFFFF"
    FULL_FRAME_FG_COLOR = "#FFFFFF"

    # Button Constants
    BUTTON_CORNER_RADIUS = 1
    BUTTON_BORDER_WIDTH = 1
    BUTTON_FG_COLOR_ACTIVE = "#FFFFFF"
    BUTTON_FG_COLOR_DISABLED = "#FFFFFF"
    BUTTON_HOVER_COLOR = "#FFFFFF"
    BUTTON_BORDER_COLOR = "#FFFFFF"
    BUTTON_TEXT_COLOR = "#FFFFFF"
    BUTTON_TEXT_COLOR_DISABLED = "#FFFFFF"

