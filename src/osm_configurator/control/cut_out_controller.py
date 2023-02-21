from __future__ import annotations

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
        self._model: IApplication = model

    def get_cut_out_mode(self) -> CutOutMode:
        _cut_out_manager: CutOutConfiguration = self._model.get_active_project().get_config_manager().get_cut_out_configuration()
        return _cut_out_manager.get_cut_out_mode()

    def set_cut_out_mode(self, mode: CutOutMode) -> bool:
        _cut_out_manager: CutOutConfiguration = self._model.get_active_project().get_config_manager().get_cut_out_configuration()
        return _cut_out_manager.set_cut_out_mode(mode)

    def get_cut_out_reference(self) -> pathlib.Path:
        _cut_out_manager: CutOutConfiguration = self._model.get_active_project().get_config_manager().get_cut_out_configuration()
        return _cut_out_manager.get_cut_out_path()

    def set_cut_out_reference(self, path: pathlib.Path) -> bool:
        _cut_out_manager: CutOutConfiguration = self._model.get_active_project().get_config_manager().get_cut_out_configuration()
        return _cut_out_manager.set_cut_out_path(path)
