import pathlib

from src.osm_configurator.control.cut_out_controller_interface import ICutOutController
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode


class CutOutControllerStub(ICutOutController):
    def get_cut_out_mode(self) -> CutOutMode:
        return CutOutMode

    def set_cut_out_mode(self, mode: CutOutMode) -> bool:
        return CutOutMode

    def set_cut_out_reference(self, path: pathlib.Path) -> bool:
        return True

    def get_cut_out_reference(self) -> pathlib.Path:
        return pathlib.Path("")
