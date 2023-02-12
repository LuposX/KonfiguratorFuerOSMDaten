import pathlib
from abc import ABC

from src.osm_configurator.control.osm_data_controller_interface import IOSMDataController

class OSMDataControllerStub(IOSMDataController, ABC):
    def set_osm_data_reference(self, path: pathlib.Path) -> bool:
        pass

    def get_osm_data_reference(self) -> pathlib.Path:
        pass

    def download_osm_data(self, path: pathlib.Path) -> bool:
        pass

