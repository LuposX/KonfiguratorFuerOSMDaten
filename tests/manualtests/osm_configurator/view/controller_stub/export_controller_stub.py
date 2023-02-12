import pathlib

from src.osm_configurator.control.export_controller_interface import IExportController


class ExportControllerInterface(IExportController):
    def export_project(self, path: pathlib.Path) -> bool:
        pass

    def export_calculations(self, path: pathlib.Path) -> bool:
        pass

    def export_configurations(self, path: pathlib.Path) -> bool:
        pass

    def export_cut_out_map(self, path: pathlib.Path) -> bool:
        pass