from src.osm_configurator.control.settings_controller_interface import ISettingsController
import src.osm_configurator.model.application.application_settings_default_enum as application_settings_default_enum_i

import pathlib

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication


class SettingsController(ISettingsController):
    __doc__ = ISettingsController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the SettingsController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        self._model = model

    def get_project_name(self) -> str:
        return self._model.get_active_project().get_project_settings().get_name()

    def set_project_name(self, name: str) -> bool:
        return self._model.get_active_project().get_project_settings().set_name(name)

    def get_project_description(self) -> str:
        return self._model.get_active_project().get_project_settings().get_description()

    def set_project_description(self, description: str) -> bool:
        return self._model.get_active_project().get_project_settings().set_description(description)

    def get_project_default_folder(self) -> pathlib.Path:
        return self._model.get_application_settings()\
            .get_setting(application_settings_default_enum_i
                         .ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER)

    def set_project_default_folder(self, default_folder: pathlib.Path) -> bool:
        return self._model.get_application_settings()\
            .set_setting(application_settings_default_enum_i
                         .ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER, default_folder)

    def get_number_of_processes(self) -> int:
        return self._model.get_application_settings() \
            .get_setting(application_settings_default_enum_i
                         .ApplicationSettingsDefault.NUMBER_OF_PROCESSES)

    def set_number_of_processes(self, number_of_processes: int) -> bool:
        return self._model.get_application_settings() \
            .set_setting(application_settings_default_enum_i
                         .ApplicationSettingsDefault.NUMBER_OF_PROCESSES, number_of_processes)
