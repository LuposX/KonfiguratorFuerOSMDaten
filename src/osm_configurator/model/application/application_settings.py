from __future__ import annotations

import os.path
import json

from typing import TYPE_CHECKING
from pathlib import Path
import src.osm_configurator.model.application.application_settings_default_enum as application_settings_enum_i

if TYPE_CHECKING:
    from pathlib import Path
    from src.osm_configurator.model.application.application_settings_default_enum import ApplicationSettingsDefault
    from typing import Dict, Any

READ_MODE: str = "r"
WRITE_MODE: str = "w"


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
        self._application_settings_file: Path = application_settings_file

    def get_setting(self, settings_enum: ApplicationSettingsDefault) -> str | None:
        """
        This method gets a specific setting from the setting file.

        Args:
            settings_enum (ApplicationSettingsDefault): The setting we want to get.
            None: if it failed to read it, this could be because user used an invalid value.

        Returns:
            str: The value of the setting.
        """
        try:
            settings: Dict[Any] = self._load_settings_file()
            return settings[settings_enum.get_name()]

        except:
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

            settings[settings_enum.get_name()] = setting_value

            with open(self._application_settings_file, WRITE_MODE) as settings_file:
                json.dump(settings, settings_file)

            return True

        except:
            return False

    def _load_settings_file(self) -> Dict[Any]:
        """
        This method loads the settings file.

        Returns:
            Dict[Any]: Returns a dictionary of settings.
        """
        with open(self._application_settings_file, READ_MODE) as settings_file:
            return json.load(settings_file)

    @classmethod
    def create_application_settings_file(cls, saving_path: Path, application_settings_file_name: str) -> bool:
        """
        Creates the Application Settings file in the project.

        Args:
            saving_path (Path): where we want to save the settings file.
            application_settings_file_name (str) The name of the settings file, should have the extension '.json'.

        Returns:
            bool: True if successful, otherwise false.
        """
        settings_dict: Dict[str, Any] = {}

        # create the dict which we wil save later to disk
        setting: ApplicationSettingsDefault
        for setting in application_settings_enum_i.ApplicationSettingsDefault:
            settings_dict.update({setting.get_name(): setting.get_default_setting_value()})

        # save the dict to disk
        full_path: Path = Path(os.path.join(saving_path, application_settings_file_name))
        with open(full_path, WRITE_MODE) as settings_file:
            json.dump(settings_dict, settings_file)