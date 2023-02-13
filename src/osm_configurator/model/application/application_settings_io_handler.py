from __future__ import annotations

from typing import TYPE_CHECKING, Final
import pathlib

import json

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Dict, Any

READ_MODE: str = "r"
WRITE_MODE: str = "w"


class ApplicationSettingsIOHandler:
    """
    This class job is to build the settings in the application.
    """

    def __init__(self, application_settings_file: Path):
        """
        Creates a new instance of the ApplicationSettingsIOHandler.

        Args:
            application_settings_file (pathlib.Path): name of the file
        """
        self._application_settings_file: Path = application_settings_file

    def get_setting(self, settings_key: str) -> str:
        """
        This method gets a specific setting from the setting file.

        Args:
            settings_key (str): The name of the setting we want to set.

        Returns:
            str: The value of the setting.
        """
        settings: Dict[Any] = self._load_settings_file()

        return settings[settings_key]

    def set_setting(self, settings_key: str, setting_value: str):
        """
        This method sets a setting in the setting file.

        Args:
            settings_key (str): The name of the setting we want to set.
            setting_value (str): The value we want the setting to have.
        """
        settings: Dict[Any] = self._load_settings_file()

        settings[settings_key] = setting_value

        with open(self._application_settings_file, WRITE_MODE) as settings_file:
            json.dump(settings, settings_file)

    def _load_settings_file(self) -> Dict[Any]:
        """
        This method loads the settings file.

        Returns:
            Dict[Any]: Returns a dictionary of settings.
        """
        with open(self._application_settings_file, READ_MODE) as settings_file:
            return json.load(settings_file)
