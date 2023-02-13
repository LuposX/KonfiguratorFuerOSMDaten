from __future__ import annotations

import os.path
from pathlib import Path

from typing import TYPE_CHECKING

import src.osm_configurator.model.application.application_settings_io_handler as application_settings_io_handler_i
import multiprocessing

if TYPE_CHECKING:
    from pathlib import Path
    from src.osm_configurator.model.application.application_settings_io_handler import ApplicationSettingsIOHandler
    from typing import Final

SETTING_KEY_DEFAULT_PROJECT_FOLDER: Final = "default_project_folder"
SETTING_KEY_NUMBER_OF_PROCESSES: Final = multiprocessing.cpu_count()


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
        self._application_settings_io_handler: ApplicationSettingsIOHandler = application_settings_io_handler_i \
            .ApplicationSettingsIOHandler(application_settings_file)

        self._path_settings_file: Path = self._application_settings_io_handler.load_settings_file()

    def get_default_project_folder(self) -> Path | None:
        """
        Gives back the path pointing towards the project.

        Returns:
            Path: Returns the path of the default location.
              None: if it failed to read the setting.
        """
        try:
            return Path(self._application_settings_io_handler.get_setting(SETTING_KEY_DEFAULT_PROJECT_FOLDER))

        except:
            return None

    def set_default_location(self, new_location: Path) -> bool:
        """
        Sets the default path pointing towards the project to a new Location.

        Args:
            new_location (Path): The new Location, where the user wants to save new projects.

        Return:
            bool: true if sucessfull
        """
        try:
            self._application_settings_io_handler.set_setting(SETTING_KEY_DEFAULT_PROJECT_FOLDER, str(new_location))
            return True

        except:
            return False

    def get_number_of_processes(self) -> int | None:
        """
        Getter for the number of processes the calculation will be run with.

        Returns:
            int: Number of processes to use.
            None: if it failed to read it, this could be because user used an invalid value.
        """
        try:
            return int(self._application_settings_io_handler.get_setting(str(SETTING_KEY_NUMBER_OF_PROCESSES)))

        except:
            return None
