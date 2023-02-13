from src.osm_configurator.control.export_controller_interface import IExportController

import pathlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication


class ExportController(IExportController):
    __doc__ = IExportController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the ExportController with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def export_project(self, path: pathlib.Path) -> bool:
        pass

    def export_calculations(self, path: pathlib.Path) -> bool:
        pass

    def export_configurations(self, path: pathlib.Path) -> bool:
        pass

    def export_cut_out_map(self, path: pathlib.Path) -> bool:
        pass
