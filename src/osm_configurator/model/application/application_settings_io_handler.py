from __future__ import annotations

from typing import TYPE_CHECKING, Final


if TYPE_CHECKING:
    from pathlib import Path

READ: str = "r"


class ApplicationSettingsIOHandler:
    """
    This class job is to build the settings in the application.
    """

    def __init__(self, application_settings_file: Path):
        """
        Creates a new instance of the ApplicationSettingsIOHandler.

        Args:
            application_settings_file (Path): name of the file
        """
        self.filename: Path = application_settings_file

    def load_settings_file(self) -> Path:
        """
        This method loads the settings file.

        Returns:
            bool: True when building the path works, otherwise false.
        """
        with open(self.filename, READ) as f:
            location = f.read()
            return location


