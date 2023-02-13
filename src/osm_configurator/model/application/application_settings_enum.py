from __future__ import annotations

from enum import Enum, unique

from typing import TYPE_CHECKING
import multiprocessing

if TYPE_CHECKING:
    from typing import Any


@unique
class ApplicationSettingsEnum(Enum):
    # The first value of the tuple is teh name of teh setting.
    # The second value is the default value the setting will have if it didn't get changed.
    SETTING_KEY_DEFAULT_PROJECT_FOLDER = ("default_project_folder", None)
    SETTING_KEY_NUMBER_OF_PROCESSES = ("number_of_processes_for_calculation", multiprocessing.cpu_count())

    def get_name(self) -> str:
        """
        Getter for the name of the setting.

        Returns:
            str: Name of the setting.
        """
        return self.value[0]

    def get_default_setting_value(self) -> Any:
        """
        Getter for the default value of the setting.

        Returns:
            Any: Default value of the setting.
        """
        return self.value[1]
