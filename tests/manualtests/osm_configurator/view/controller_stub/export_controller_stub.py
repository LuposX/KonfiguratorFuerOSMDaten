import pathlib

from src.osm_configurator.control.export_controller_interface import IExportController


class ExportControllerStub(IExportController):
    def export_project(self, path: pathlib.Path) -> bool:
        return True

    def export_calculations(self, path: pathlib.Path) -> bool:
        return True

    def export_configurations(self, path: pathlib.Path) -> bool:
        return True

    def export_cut_out_map(self, path: pathlib.Path) -> bool:
        return True
