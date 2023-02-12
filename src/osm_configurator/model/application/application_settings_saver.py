from __future__ import annotations

import os.path
import pathlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class ApplicationSettingsSaver:
    """
    This class job is to save the settings in the application.
    """

    def __init__(self):
        """
        Creates a new instance of the ApplicationSettingsSaver.
        """
        pass

    def save_settings(self, destination: Path) -> bool:
        """
        This method saves the default path where new projects should be stored.

        Args:
            destination (pathlib.Path): The path pointing towards the default project folder.

        Returns:
            bool: True when saving the path works, otherwise false.
        """
        if os.path.exists(destination):
            filename = "default_project_folder.txt"
            default_project_folder: Path = destination.joinpath(filename)

            with open(default_project_folder, 'w', newline="") as f:
                f.write(str(destination))
            return True
        return False
