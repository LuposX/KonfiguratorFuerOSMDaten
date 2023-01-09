from src.osm_configurator.view.toplevelframes.reduction_frame import ReductionFrame
from src.osm_configurator.control.control_interface import IControl


class ReductionCalculationFrame:
    """
    This Frame provides the User the ability to set the calculation of the reduction on Categories, that will be shown
    on the ReductionFrame.
    """

    def __init__(self, parent, control):
        """
        This Method Creates a ReductionCalculationFrame, that lets the User edit the calculation of the reduction of
        Categories.
        Args:
            parent (ReductionFrame): This is the Parent Frame of this Frame, here this Frame will be located.
            control (IControl): The Control the Frame calls, to get access to the Model.
        """
        pass
