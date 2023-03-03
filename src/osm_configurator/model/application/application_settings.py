from __future__ import annotations

from typing import TYPE_CHECKING

import os.path
import json
import sys
from pathlib import Path

import src.osm_configurator.model.application.application_settings_default_enum as application_settings_enum_i

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_settings_default_enum import ApplicationSettingsDefault
    from typing import Dict, Any, Final

READ_MODE: str = "r"
WRITE_MODE: str = "w"
APPLICATION_SETTINGS_FILE: Final = "application_setting.json"


class ApplicationSettings:
    """
    This class job is to manage the settings apart from the project settings. In those settings the default-location
    to save projects can be changed.
    """

    def __init__(self, path_to_starting_file: Path = None):
        """
        Creates a new instance of the application_settings_file.

        Args:
            path_to_starting_file (Path): If set that directory will be used to create the application settings file.
        """
        # Get the path of the application
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # If the application is run as a bundle, the PyInstaller bootloader
            # extends the sys module by a flag frozen=True and sets the app
            # path into variable _MEIPASS'.
            # noinspection PyProtectedMember
            # pylint: disable=protected-access
            application_path = sys._MEIPASS
        else:
            if path_to_starting_file is None:
                application_path = os.path.dirname(os.path.abspath(__file__))

            else:
                application_path = path_to_starting_file

        # check for the application settings file.
        self._application_settings_file: Path | None = None
        file: str
        for file in Path(application_path).iterdir():
            if os.path.basename(file) == APPLICATION_SETTINGS_FILE:
                self._application_settings_file = Path(file)
                break

        # This mean the application_Settings file doesn't exist yet, and we need to create it
        if self._application_settings_file is None:
            self._application_settings_file = \
                ApplicationSettings.create_application_settings_file(application_path,
                                                                     APPLICATION_SETTINGS_FILE)

    def get_setting(self, settings_enum: ApplicationSettingsDefault) -> Any:
        """
        This method gets a specific setting from the setting file.

        Args:
            settings_enum (ApplicationSettingsDefault): The setting we want to get. "None" if it failed to read it,
                this could be because user used an invalid value.

        Returns:
            Any: The value of the setting.
        """
        try:
            settings: Dict[Any] = self._load_settings_file()

            if settings_enum == application_settings_enum_i.ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER:
                if settings[settings_enum.get_name()] is None:
                    return None

                return Path(settings[settings_enum.get_name()])

            return settings[settings_enum.get_name()]

        except Exception:
            return None

    def set_setting(self, settings_enum: ApplicationSettingsDefault, setting_value: Any) -> bool:
        """
        This method sets a setting in the setting file.

        Args:
            settings_enum (ApplicationSettingsDefault): The setting we want to set.
            setting_value (Any): The value we want the setting to have.

        Returns:
            bool: true if value got set successfully.
        """
        try:
            settings: Dict[Any] = self._load_settings_file()

            if settings_enum == application_settings_enum_i.ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER:
                settings[settings_enum.get_name()] = str(setting_value)

            else:
                settings[settings_enum.get_name()] = setting_value

            with open(self._application_settings_file, WRITE_MODE, encoding="utf-8") as settings_file:
                json.dump(settings, settings_file)

            return True

        except Exception:
            return False

    def _load_settings_file(self) -> Dict[Any]:
        """
        This method loads the settings file.

        Returns:
            Dict[Any]: Returns a dictionary of settings.
        """
        with open(self._application_settings_file, READ_MODE, encoding="utf-8") as settings_file:
            return json.load(settings_file)

    @classmethod
    def create_application_settings_file(cls, saving_path: Path, application_settings_file_name: str) -> Path | None:
        """
        Creates the Application Settings file in the project.

        Args:
            saving_path (Path): where we want to save the settings file.
            application_settings_file_name (str) The name of the settings file, should have the extension '.json'.

        Returns:
            Path | None: The path towards the created file, none if didn't work.
        """
        settings_dict: Dict[str, Any] = {}

        # create the dict which we wil save later to disk
        setting: ApplicationSettingsDefault
        for setting in application_settings_enum_i.ApplicationSettingsDefault:
            settings_dict.update({setting.get_name(): setting.get_default_setting_value()})

        # save the dict to disk
        try:
            full_path: Path = Path(os.path.join(saving_path, application_settings_file_name))
            with open(full_path, WRITE_MODE, encoding="utf-8") as settings_file:
                json.dump(settings_dict, settings_file)

            return full_path

        except OSError:
            return None
