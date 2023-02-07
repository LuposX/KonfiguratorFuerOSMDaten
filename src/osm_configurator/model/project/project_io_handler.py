from __future__ import annotations

import os

import src.osm_configurator.model.project.active_project
import pathlib
import csv
from typing import TYPE_CHECKING
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationMethod
from src.osm_configurator.model.project.configuration.cut_out_configuration import CutOutMode
from src.osm_configurator.model.project.configuration.category import Category
from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea

if TYPE_CHECKING:
    from src.osm_configurator.model.project.active_project import ActiveProject
    from pathlib import Path


class ProjectIOHandler:
    """
    This class handles the I/O of a project.
    This includes:
    - loading a project from disk into memory that the user selected in the main menu
    - creating a project on the disk, if the user selected that
    """

    def __init__(self, active_project: ActiveProject):
        """
        Creates a new instance of the ProjectLoader. Therefore, it gets the current active project, which should be
        loaded if not newly created.

        Args:
            active_project (active_project.ActiveProject): The project the ProjectLoader shall load.
        """
        self._active_project: ActiveProject = active_project
        self.destination: Path = Path()

    def build_project(self, path: Path) -> bool:
        """
        This method is to build the given project. To do this it reads out the configurations and builts a folder
        structure on the disk.

        Args:
            path (pathlib.Path): The path pointing towards the project folder.

        Returns:
            bool: True if creating the project works, otherwise false.
        """
        pass

    def load_project(self, path: Path) -> bool:
        """
        Loads a project in from the disk into the memory.

        Args:
            path (pathlib.Path): The path pointing towards the project folder.

        Returns:
            bool: True if creating the project works, otherwise false.
        """
        self.destination = path

        # Loads the different parts of the project
        self._load_project_settings()

        self._load_config_phase()

        self._load_osm_configurator()

        self._load_aggregation_configuration()

        self._load_category_configuration()
        return True

    def _load_project_settings(self) -> bool:
        filepath = os.path.join(self.destination, "project_settings.csv")
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                reader = csv.reader(f)
                project_settings_data = list(reader)
            if len(project_settings_data) is 4:
                self._active_project.get_project_settings().set_name(project_settings_data[0][1])
                self._active_project.get_project_settings().set_description(project_settings_data[1][1])
                self._active_project.get_project_settings().set_location(Path(project_settings_data[2][1]))
                self._active_project.get_project_settings().set_calculation_phase_checkpoints_folder(
                    project_settings_data[3][1])
                return True
        return False

    def _load_config_phase(self) -> bool:
        filepath: Path = Path(os.path.join(self.destination, "last_step.txt"))
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                last_step: str = f.read()
            last_step_config_phase: ConfigPhase = ConfigPhase.equals(last_step)
            if last_step_config_phase is not None:
                self._active_project.set_last_step(last_step_config_phase)
                return True
        return False

    def _load_osm_configurator(self) -> bool:
        filepath: Path = Path(os.path.join(self.destination, "osm_path.txt"))
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                osm_path: str = f.read()
            self._active_project.get_config_manager().get_osm_data_configuration().set_osm_data(Path(osm_path))
            return True
        return False

    def _load_aggregation_configuration(self) -> bool:
        filepath: Path = Path(os.path.join(self.destination, "active_methods.csv"))
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                reader = csv.reader(f)
                aggregation = list(reader)
                # Todo equals in AggregationMethod
            for row in aggregation:
                method: AggregationMethod = AggregationMethod.equals(row[0])
                state: bool = False
                if row[1] is "True":
                    _state = True
                if row[1] is not "False":
                    return False
                self._active_project.get_config_manager().get_aggregation_configuration() \
                    .set_aggregation_method_active(method, state)
            return True
        return False

    def _load_cut_out_configurator(self) -> bool:
        filepath: Path = Path(os.path.join(self.destination, "cut_out_configuration.csv"))
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                reader = csv.reader(f)
                cut_out = list(reader)

            cut_out_path: Path = Path(cut_out[0][1])
            cut_out_mode: CutOutMode = CutOutMode.equals(cut_out[1][1])
            if os.path.exists(cut_out_path):
                self._active_project.get_config_manager().get_cut_out_configuration().set_cut_out_path(cut_out_path)
            else:
                return False
            if cut_out_mode is not None:
                self._active_project.get_config_manager().get_cut_out_configuration().set_cut_out_mode(cut_out_mode)
            else:
                return False
            return True
        return False

    def _load_category_configuration(self) -> bool:

        category_list: list[Category] = []

        for file in os.listdir(self.destination):
            if file.endswith(".csv"):
                # TODO check byte
                filepath: Path = Path(os.path.join(self.destination, file))
                with open(filepath, "r") as f:
                    reader = csv.reader(f)
                    category_data = list(reader)
                category: Category
                category.set_category_name(category_data[0][1])
                if category_data[1][1] is "True":
                    category.activate()
                if category_data[1][1] is not "False":
                    category.deactivate()
                else:
                    return False
                category.set_whitelist(category_data[2][1])
                category.set_blacklist(category_data[3][1])
                category.set_calculation_method_of_area(CalculationMethodOfArea.equals(category_data[4][1]))



                category.set_category_name(category_data[0][1])

        return False
