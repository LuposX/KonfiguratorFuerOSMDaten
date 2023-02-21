from __future__ import annotations

from enum import Enum, unique

from typing import TYPE_CHECKING
import multiprocessing

if TYPE_CHECKING:
    from typing import Any


@unique
class ApplicationSettingsDefault(Enum):
    # The first value of the tuple is the name of the setting.
    # The second value is the default value the setting will have if it didn't get changed.
    DEFAULT_PROJECT_FOLDER = ("default_project_folder", None)
    NUMBER_OF_PROCESSES = ("number_of_processes_for_calculation", multiprocessing.cpu_count())
    NUMBER_OF_RECOMMENDATIONS = ("number_of_recommendation", 6)

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
