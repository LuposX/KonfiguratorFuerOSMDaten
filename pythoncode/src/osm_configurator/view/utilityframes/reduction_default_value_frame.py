from src.osm_configurator.view.toplevelframes.reduction_frame import ReductionFrame
from src.osm_configurator.control.control_interface import IControl


class ReductionDefaultValueFrame:
    """
    This Frame lets the User edit Default Values on Tags for Categories, that the Calculation can later use.
    """

    def __init__(self, parent, control):
        """
        This Method Creates a ReductionDefaultValueFrame where the User can edit Default Values on Tags for
        Categories.
        Args:
            parent (ReductionFrame): This is the Parent Frame of this Frame, here this Frame will be located.
            control (IControl): The Control the Frame calls, to get access to the Model.
        """
        pass
