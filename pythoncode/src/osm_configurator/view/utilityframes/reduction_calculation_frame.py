import src.osm_configurator.view.toplevelframes.reduction_frame


class ReductionCalculationFrame:
    """
    This frame provides the ability to the user to set how the calculation of the reduction of a category
    will be done.
    This is a subframe from the ReductionFrame.
    """

    def __init__(self, parent, control):
        """
        This method creates a ReductionCalculationFrame that lets the user edit the calculation of the reduction of
        Categories.
        Args:
            parent (reduction_frame.ReductionFrame): This is the parent frame of this frame. The frame will be located here.
            control (control_interface.IControl): The control the frame will call to get access to the model.
        """
        pass

    def activate(self):
        """
        Tells the current frame to activate and collect all the data it needs.

        Returns:
            bool: True, if activation was successful, otherwise false.
        """
        pass
