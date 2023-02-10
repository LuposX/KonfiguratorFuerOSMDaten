from __future__ import annotations

from pathlib import Path
from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
from src.osm_configurator.model.project.data_visualizer import DataVisualizer
from src.osm_configurator.model.project.project_settings import ProjectSettings
from src.osm_configurator.model.project.calculation.calculation_manager import CalculationManager
from src.osm_configurator.model.project.export import Export
from src.osm_configurator.model.project.project_saver import ProjectSaver
from src.osm_configurator.model.project.project_io_handler import ProjectIOHandler
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_manager import CalculationManager
    from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
    from src.osm_configurator.model.project.project_saver import ProjectSaver
    from src.osm_configurator.model.project.project_io_handler import ProjectIOHandler
    from src.osm_configurator.model.project.data_visualizer import DataVisualizer
    from src.osm_configurator.model.project.project_settings import ProjectSettings
    from src.osm_configurator.model.project.export import Export
    from pathlib import Path


class ActiveProject:
    """
    This class job is to manage the active project the user is working on.
    Whereby an active project, a project is that got selected by the user in the project selected screen or
    created.
    """

    def __init__(self, project_folder: Path, is_newly_created: bool, project_name=None, project_description=None):
        """
        Creates a new instance of the ActiveProject. In this process it creates the ConfigurationManager and also
        differentiate between the case that the project is new or loaded. In the case of an existing project it
        calls the ProjectLoader, otherwise it creates a new project.

        Args:
            project_folder (pathlib.Path): This is path pointing towards the folder, where the project is saved.
            is_newly_created (bool): This argument is true if the project is newly created, otherwise false.
            project_name (str): How we want to name the project.
            project_description (str): The description of our project.
        """

        self.project_directory: Path = project_folder.joinpath(project_name)

        self._project_io_handler: ProjectIOHandler = ProjectIOHandler(self)
        self._configurator_manager: ConfigurationManager = ConfigurationManager(project_folder)
        self._calculation_manager: CalculationManager = CalculationManager(self._configurator_manager)
        self._project_settings: ProjectSettings = ProjectSettings(self.project_directory, project_name,
                                                                  project_description, "calculation_check_points")
        self._last_step: ConfigPhase = ConfigPhase.DATA_CONFIG_PHASE

        if is_newly_created:
            self._project_io_handler.build_project(self.project_directory)
        else:
            self._project_io_handler.load_project(self.project_directory)

        self._project_saver: ProjectSaver = ProjectSaver(self)
        self._data_visualizer: DataVisualizer = DataVisualizer()
        self._export: Export = Export(self)

    def get_last_step(self) -> ConfigPhase:
        """
        This method is there so that the user can continue working in the same phase in an existing project
        where he previously stopped.

        Returns:
            config_phase_enum.ConfigPhase: The last phase the user was working on.
        """
        return self._last_step

    def set_last_step(self, current_step: ConfigPhase) -> bool:
        """
        This method is there so that the user can continue working in the same phase in an existing project
        where he previously stopped.

        Args:
            config_phase_enum.ConfigPhase: The current phase the user is working on.

        Return:
            bool: True if changing the state works, otherwise false.
        """
        if current_step in ConfigPhase:
            self._last_step = current_step
            return True
        return False

    def get_project_path(self) -> Path:
        """
        This method is to give back the path pointing towards the project folder.

        Returns:
            pathlib.Path: The path pointing towards the project folder.
        """
        return self._project_settings.get_location()

    def get_config_manager(self) -> ConfigurationManager:
        """
        Getter for the configuration Manager.

        Returns:
            configuration_manager.ConfigurationManager: The configuration manager.
        """
        return self._configurator_manager

    def get_data_visualizer(self) -> DataVisualizer:
        """
        Getter for the data visualizer.

        Returns:
            data_visualizer.DataVisualizer: The data visualizer.
        """
        return self._data_visualizer

    def get_calculation_manager(self) -> CalculationManager:
        """
        Getter for the calculation Manager.

        Returns:
            calculation_manager.CalculationManager: The calculation Manager.
        """
        return self._calculation_manager

    def get_project_settings(self) -> ProjectSettings:
        """
        Getter for the project settings.

        Returns:
            project_settings.ProjectSettings: The project settings.
        """
        return self._project_settings

    def get_export_manager(self) -> Export:
        """
        Getter for the export Manager.

        Returns:
            export.Export: The  export Manager.
        """
        return self._export

    def get_project_saver(self) -> ProjectSaver:
        """
        Getter for the project saver.

        Returns:
            project_saver.ProjectSaver: The project saver.
        """
        return self._project_saver

