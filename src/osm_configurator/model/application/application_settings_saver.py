from __future__ import annotations

import os.path
import pathlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Final

class ApplicationSettingsSaver:
    """
    This class job is to save the settings in the application.
    """

    def __init__(self, application_settings_file: Path):
        """
        Creates a new instance of the ApplicationSettingsSaver.

        Args:
            application_settings_file (Path): name of the file
        """
        self.application_settings_file: Path = application_settings_file

    def save_settings(self, default_folder_path: Path) -> bool:
        """
        This method saves the default path where new projects should be stored.

        Returns:
            bool: True when saving the path works, otherwise false.
        """
        if os.path.exists(self.application_settings_file):
            with open(self.application_settings_file, 'w', newline="") as f:
                f.write(str(default_folder_path))

            return True
        return False
