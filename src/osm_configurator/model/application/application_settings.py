from __future__ import annotations

import os.path
from pathlib import Path

from typing import TYPE_CHECKING

import  src.osm_configurator.model.application.application_settings_io_handler as application_settings_io_handler_i

if TYPE_CHECKING:
    from pathlib import Path
    from src.osm_configurator.model.application.application_settings_io_handler import ApplicationSettingsIOHandler


class ApplicationSettings:
    """
    This class job is to manage the settings apart from the project settings. In those settings the default-location
    to save projects can be changed.
    """

    def __init__(self, application_settings_file: Path):
        """
        Creates a new instance of the application_settings_file.

        Args:
            application_settings_file (Path): name of the file
        """
        application_settings_io_handler: ApplicationSettingsIOHandler = application_settings_io_handler_i\
            .ApplicationSettingsIOHandler(application_settings_file)

        self.path: Path = application_settings_io_handler.load_settings_file()

    def get_default_project_folder(self) -> Path:
        """
        Gives back the path pointing towards the project.

        Returns:
            pathlib.Path: Returns the path of the default location.
        """
        return self.path

    def set_default_location(self, new_location: Path):
        """
        Sets the default path pointing towards the project to a new Location.

        Args:
            new_location (pathlib.Path): The new Location, where the user wants to save new projects.
        """
        if os.path.exists(new_location):
            self.path = new_location
