from enum import Enum
import src.osm_configurator.control.control_interface
import src.osm_configurator.view.states.positioned_frame


class StateName(Enum):
    """
    This Enum saves the different State possibilities that exist, to define a state by this enum and not, by a number.
    This Enum gives a State a name.
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
