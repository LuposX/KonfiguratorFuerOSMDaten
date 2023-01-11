import src.osm_configurator.view.toplevelframes.reduction_frame
import src.osm_configurator.control.control_interface


class ReductionCalculationFrame:
    """
    This Frame provides the ability to the User to set how the calculation of the reduction of a category
    will be done.
    This is a subframe from the ReductionFrame.
    """

    def __init__(self, parent, control):
        """
        This Method Creates a ReductionCalculationFrame, that lets the User edit the calculation of the reduction of
        Categories.
        Args:
            parent (reduction_frame.ReductionFrame): This is the Parent Frame of this Frame. The Frame will be located here.
            control (control_interface.IControl): The Frame calls the Control, to gain access to the Model.
        """
        pass
