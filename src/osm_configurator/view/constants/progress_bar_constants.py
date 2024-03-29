from __future__ import annotations

from enum import Enum

from src.osm_configurator.view.constants.button_constants import ButtonConstants


class ProgressBarConstants(Enum):
    """
    Holds all constant-value to implement a Progress-Bar according to the application's standards
    """

    PROGRESS_BAR_CONSTANTS_BORDER_WITH = 0
    PROGRESS_BAR_CONSTANTS_CORNER_RADIUS = 8
    PROGRESS_BAR_CONSTANTS_FG_COLOR = ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value
    PROGRESS_BAR_CONSTANTS_PROGRESS_COLOR = "#60DB5E"
    PROGRESS_BAR_CONSTANTS_ORIENTATION = "horizontal"
    PROGRESS_BAR_CONSTANTS_MODE = "determinate"
    PROGRESS_BAR_CONSTANTS_DETERMINATE_SPEED = 1
    PROGRESS_BAR_CONSTANTS_INDETERMINATE_SPEED = 1
    PROGRESS_BAR_CONSTANTS_WIDTH = 420
