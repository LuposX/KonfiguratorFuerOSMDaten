import pathlib
from src.osm_configurator.control.cut_out_controller_interface import ICutOutController

from src.osm_configurator.model.project.configuration.cut_out_configuration import CutOutConfiguration
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication
    from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode


class CutOutController(ICutOutController):
    __doc__ = ICutOutController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the CutOutController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        self._cut_out_manager: CutOutConfiguration = model.get_active_project().get_config_manager().get_cut_out_configuration()

    def get_cut_out_mode(self) -> CutOutMode:
        return self._cut_out_manager.get_cut_out_mode()

    def set_cut_out_mode(self, mode: CutOutMode) -> bool:
        return self._cut_out_manager.set_cut_out_mode(mode)

    def get_cut_out_reference(self) -> pathlib.Path:
        return self._cut_out_manager.get_cut_out_path()

    def set_cut_out_reference(self, path: pathlib.Path) -> bool:
        return self._cut_out_manager.set_cut_out_path(path)

