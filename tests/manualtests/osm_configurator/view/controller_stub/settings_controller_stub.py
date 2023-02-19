import pathlib

from src.osm_configurator.control.settings_controller_interface import ISettingsController


class SettingsControllerStub(ISettingsController):
    def get_project_name(self) -> str:
        return "EXAMPLE PROJECT NAME"

    def set_project_name(self, name: str) -> bool:
        return True

    def get_project_description(self) -> str:
        return "EXAMPLE PROJECT DESCRIPTION"

    def set_project_description(self, description: str) -> bool:
        return True

    def get_project_default_folder(self) -> pathlib.Path:
        return pathlib.Path("")

    def set_project_default_folder(self, default_folder: pathlib.Path) -> bool:
        return True
