import src.osm_configurator.view.states.positioned_frame

from enum import Enum


class StateName(Enum):
    """
    This enum saves the different state possibilities that exist, to define a state by this enum and not, by a number.
    This enum gives a state a name.
    """

    MAIN_MENU = 1
    CREATE_PROJECT = 2
    DATA = 3
    CATEGORY = 4
    REDUCTION = 5
    ATTRACTIVITY_EDIT = 6
    ATTRACTIVITY_VIEW = 7
    AGGREGATION = 8
    CALCULATION = 9
    SETTINGS = 10
