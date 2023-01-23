import pathlib
from src.osm_configurator.control.cut_out_controller_interface import ICutOutController

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
        pass

    def get_cut_out_mode(self):
        pass

    def set_cut_out_mode(self, mode: CutOutMode):
        pass

    def set_cut_out_reference(self, path: pathlib.Path):
        pass

    def get_cut_out_reference(self):
        pass
