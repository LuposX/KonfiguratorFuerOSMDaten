from __future__ import annotations

import src.osm_configurator.view.states.state_manager
import src.osm_configurator.control.category_controller

from src.osm_configurator.view.toplevelframes.top_level_frame import TopLevelFrame


class AttractivityViewFrame(TopLevelFrame):
    """
    This frame shows a list with all categories, their attractivity attributes and how they are calculated.
    This is only a visualisation and therefore a non-edit Frame.
    """

    def __init__(self, state_manager, category_controller):
        """
        This method creates an AttractivityViewFrame showing a lList of containing all categories,
        their according attractivity attributes and how they are calculated.

         Args:
            state_manager (state_manager.StateManager): The StateManager the frame will call, when it wants to change to another state.
            category_controller (category_controller.CategoryController): Respective controller
        """
        # super().__init__(state_manager, control)
        pass

    def activate(self):
        pass
