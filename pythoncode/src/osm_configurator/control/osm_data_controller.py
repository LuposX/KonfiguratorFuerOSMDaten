from src.osm_configurator.control.osm_data_controller_interface import IOSMDataController

import pathlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication


class OSMDataController(IOSMDataController):
    __doc__ = IOSMDataController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the OSMDataController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def set_osm_data_reference(self, path: pathlib.Path) -> bool:
        pass

    def get_osm_data_reference(self) -> pathlib.Path:
        pass

    def download_osm_data(self, path: pathlib.Path) -> bool:
        pass
