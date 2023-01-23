from src.osm_configurator.control.settings_controller_interface import ISettingsController

import pathlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication


class SettingsController(ISettingsController):
    __doc__ = ISettingsController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the SettingsController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def get_project_name(self):
        pass

    def set_project_name(self, name: str):
        pass

    def get_project_description(self):
        pass

    def set_project_description(self, description: str):
        pass

    def get_project_default_folder(self):
        pass

    def set_project_default_folder(self, default_folder: pathlib.Path):
        pass
