from __future__ import annotations

import tkinter
from enum import Enum

from src.osm_configurator.view.constants.button_constants import ButtonConstants


class ComboBoxConstants(Enum):
    """
    Holds all constant-values needed to implement a standard combo-box
    """

    COMBO_BOX_CONSTANTS_CORNER_RADIUS = 8
    COMBO_BOX_CONSTANTS_FG_COLOR = ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value
    COMBO_BOX_CONSTANTS_BUTTON_COLOR = ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value
    COMBO_BOX_CONSTANTS_BORDER_COLOR = ButtonConstants.BUTTON_BORDER_COLOR.value
    COMBO_BOX_CONSTANTS_BUTTON_HOVER_COLOR = ButtonConstants.BUTTON_HOVER_COLOR.value
    COMBO_BOX_CONSTANTS_DROPDOWN_FG_COLOR = ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value
    COMBO_BOX_CONSTANTS_DROPDOWN_TEXT_COLOR = ButtonConstants.BUTTON_TEXT_COLOR.value
    COMBO_BOX_CONSTANTS_TEXT_COLOR = ButtonConstants.BUTTON_TEXT_COLOR.value
    COMBO_BOX_CONSTANTS_HOVER = True
    COMBO_BOX_CONSTANTS_STATE = tkinter.NORMAL

