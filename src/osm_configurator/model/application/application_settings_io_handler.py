from __future__ import annotations

import os

from src.osm_configurator.model.application.application import Application
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.osm_configurator.model.application.application import Application


class ApplicationSettingsIOHandler:
    """
    This class job is to build the settings in the application.
    """

    def __init__(self):
        """
        Creates a new instance of the ApplicationSettingsIOHandler.
        """
        pass

    def load_settings(self) -> bool:
        """
        This method saves the default path where new projects should be stored.
        Returns:
            bool: True when building the path works, otherwise false.
        """
        filename = "default_project_folder.txt"

        if os.path.exists(filename):
            with open(filename, 'r') as f:
                location = f.read()
                self.application.get_application_settings().set_default_location(location)
            return True
        return False
