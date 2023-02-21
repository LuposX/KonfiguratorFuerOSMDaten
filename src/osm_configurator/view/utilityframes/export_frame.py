from __future__ import annotations

import src.osm_configurator.view.toplevelframes.project_head_frame
import src.osm_configurator.control.export_controller_interface

from src.osm_configurator.view.freezable import Freezable


class ExportFrame(Freezable):
    """
    The ExportFrame provides a dropdown menu that providing the following Options:
    - project export
    - calculation export
    - Configurations Export
    """

    def __init__(self, parent_frame, export_controller):
        """
        This method creates an ExportFrame that provides the user with different export options.

        Args:
            parent_frame (project_head_frame.ProjectHeadFrame): The parent of the ExportFrame is the HeadFrame where the export feature is located.
            export_controller (export_controller.ExportController): Respective controller.
        """
        pass

    def freeze(self):
        """
        If this method is called, the frame will freeze by disabling all possible interactions with it.
        """
        pass

    def unfreeze(self):
        """
        If this method is called, the frame returns into its previous interactable state.
        """
        pass
