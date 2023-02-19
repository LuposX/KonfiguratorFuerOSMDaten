from src.osm_configurator.control.export_controller_interface import IExportController

import pathlib
from src.osm_configurator.model.project.export import Export

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
        self._model = model

    def export_project(self, path: pathlib.Path) -> bool:
        export_manager: Export = self._model.get_active_project().get_export_manager()
        return export_manager.export_project(path)

    def export_calculations(self, path: pathlib.Path) -> bool:
        export_manager: Export = self._model.get_active_project().get_export_manager()
        return export_manager.export_calculation(path)

    def export_configurations(self, path: pathlib.Path) -> bool:
        export_manager: Export = self._model.get_active_project().get_export_manager()
        return export_manager.export_configuration(path)

    def export_cut_out_map(self, path: pathlib.Path) -> bool:
        export_manager: Export = self._model.get_active_project().get_export_manager()
        return export_manager.export_map(path)
