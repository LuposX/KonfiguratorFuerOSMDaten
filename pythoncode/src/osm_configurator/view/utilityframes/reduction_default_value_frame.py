from __future__ import annotations

import src.osm_configurator.view.toplevelframes.reduction_frame
import src.osm_configurator.control.category_controller

from src.osm_configurator.view.activatable import Activatable


class ReductionDefaultValueFrame(Activatable):
    """
    This frame shows a list of tags in a priority order, that can be expanded by adding or removing tags.
    These tags can hold default values on attributes that can be used in the calculation.
    """

    def __init__(self, parent, control):
        """
        This method creates a ReductionDefaultValueFrame where the User can edit default-values on tags for
        categories.

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
