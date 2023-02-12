from __future__ import annotations

from enum import Enum

from src.osm_configurator.view.constants.button_constants import ButtonConstants


class OptionsMenuConstants(Enum):
    """
    Holds all constant-values to implement an Options-Menu according to the application's standards
    """

    OPTIONS_MENU_CONSTANTS_CORNER_RADIUS = 8
    OPTIONS_MENU_CONSTANTS_FG_COLOR = "#FFFFFF"
    OPTIONS_MENU_CONSTANTS_BUTTON_COLOR = ButtonConstants.BUTTON_FG_COLOR_ACTIVE.value
    OPTIONS_MENU_CONSTANTS_BUTTON_HOVER_COLOR = ButtonConstants.BUTTON_HOVER_COLOR.value
    OPTIONS_MENU_CONSTANTS_DROPDOWN_FG_COLOR = "#FFFFFF"
    OPTIONS_MENU_CONSTANTS_DROPDOWN_HOVER_COLOR = ButtonConstants.BUTTON_HOVER_COLOR.value
    OPTIONS_MENU_CONSTANTS_DROPDOWN_TEXT_COLOR = "#000000"
    OPTIONS_MENU_CONSTANTS_TEXT_COLOR = "#000000"
    OPTIONS_MENU_CONSTANTS_HOVER = True
    OPTIONS_MENU_CONSTANTS_STATE = "normal"
    OPTIONS_MENU_CONSTANTS_ANCHOR = "center"
