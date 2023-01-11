import src.osm_configurator.view.toplevelframes.reduction_frame
import src.osm_configurator.control.control_interface


class ReductionDefaultValueFrame:
    """
    This Frame shows a List of Tags in a priority order, that can be expanded by adding or removing tags.
    These Tags can hold default Values on attributes, that can be used in the Calculation.
    """

    def __init__(self, parent, control):
        """
        This Method Creates a ReductionDefaultValueFrame where the User can edit Default-Values on Tags for
        Categories.

        Args:
            parent (reduction_frame.ReductionFrame): This is the Parent Frame of this Frame. The Frame will be located here.
            control (control_interface.IControl): The Control the Frame calls, to gain access to the Model.
        """
        pass
