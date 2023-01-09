import src.osm_configurator.view.toplevelframes.reduction_frame
import src.osm_configurator.control.control_interface


class ReductionDefaultValueFrame:
    """
    This Frame lets the User edit Default Values on Tags for Categories, that the Calculation can later use.
    """

    def __init__(self, parent, control):
        """
        This Method Creates a ReductionDefaultValueFrame where the User can edit Default Values on Tags for
        Categories.
        Args:
            parent (reduction_frame.ReductionFrame): This is the Parent Frame of this Frame,
            here this Frame will be located.
            control (control_interface.IControl): The Control the Frame calls, to get access to the Model.
        """
        pass
