from enum import Enum
import src.osm_configurator.control.control_interface
import src.osm_configurator.view.states.positioned_frame


class State(Enum):
    """
    This Class models a State, that holds different Frames that shall be shown on a Window, if it gets activated.
    As well as defining what State (more specific, what Frames) is the default on its left and right.
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

    # def __init__(self, active_frames, control):
    #     """
    #     This Method Creates a new State, with a List of Frames it shall hold and a Control the Frames shall call
    #     to access the Model.
    #
    #     Args:
    #         active_frames list[positioned_frame.PositionedFrame]: A List of Frames that shall be shown if this
    #         State is activated.
    #         control (control_interface.IControl): The Control the Frames of this State shall call if they need to
    #         access the Model.
    #     """
    #     pass

    def get_active_frames(self):
        """
        This Method Returns the List of the Frames this State holds.

        Returns:
            list[positioned_frame.PositionedFrame]: a List of Frames, this State holds.
        """
        pass

    def get_default_left(self):
        """
        This Method Returns what the State on its left is.

        Returns:
            State: the State on this States left
        """
        pass

    def get_default_right(self):
        """
        This Method Returns what the State on its right is.

        Returns:
            State: the State on this States right
        """
        pass
