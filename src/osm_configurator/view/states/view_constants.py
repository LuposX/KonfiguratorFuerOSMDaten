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
