import src.osm_configurator.view.toplevelframes.reduction_frame
import src.osm_configurator.control.control_interface


class ReductionDefaultValueFrame:
    """
    This frame shows a list of tags in a priority order, that can be expanded by adding or removing tags.
    These tags can hold default values on attributes, that can be used in the calculation.
    """

    def __init__(self, parent, control):
        """
        This method creates a ReductionDefaultValueFrame where the User can edit default-values on tags for
        categories.

        Args:
            parent (reduction_frame.ReductionFrame): This is the parent frame of this frame. The frame will be located here.
            control (control_interface.IControl): The control the frame calls, to gain access to the model.
        """
        pass
