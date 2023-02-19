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
        self._model = model

    def set_osm_data_reference(self, path_to_osm_data: pathlib.Path) -> bool:
        return self._model.get_active_project().get_config_manager()\
            .get_osm_data_configuration().set_osm_data(path_to_osm_data)

    def get_osm_data_reference(self) -> pathlib.Path:
        return self._model.get_active_project().get_config_manager()\
            .get_osm_data_configuration().get_osm_data()
