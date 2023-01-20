import src.osm_configurator.view.toplevelframes.reduction_frame
import src.osm_configurator.control.category_controller

from src.osm_configurator.view.activatable import Activatable


class ReductionCalculationFrame(Activatable):
    """
    This frame provides the ability to the user to set how the calculation of the reduction of a category
    will be done.
    This is a subframe from the ReductionFrame.
    """

    def __init__(self, parent, category_controller):
        """
        This method creates a ReductionCalculationFrame that lets the user edit the calculation of the reduction of
        Categories.
        Args:
            parent (reduction_frame.ReductionFrame): This is the parent frame of this frame. The frame will be located here.
            category_controller (category_controller.CategoryController): Respective controller.
        """
        pass

    def activate(self):
        """
        Tells the current frame to activate and collect all the data it needs.

        Returns:
            bool: True, if activation was successful, otherwise false.
        """
        pass
