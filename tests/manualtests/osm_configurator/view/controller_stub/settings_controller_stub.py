import pathlib

from src.osm_configurator.control.settings_controller_interface import ISettingsController


class SettingsControllerStub(ISettingsController):
    def get_project_name(self) -> str:
        pass

    def set_project_name(self, name: str) -> bool:
        pass

    def get_project_description(self) -> str:
        pass

    def set_project_description(self, description: str) -> bool:
        pass

    def get_project_default_folder(self) -> pathlib.Path:
        pass

    def set_project_default_folder(self, default_folder: pathlib.Path) -> bool:
        pass