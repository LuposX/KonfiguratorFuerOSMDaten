from __future__ import annotations

from typing import TYPE_CHECKING

import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

from src.osm_configurator.model.application.application import Application
from src_tests.definitions import TEST_DIR
from src.osm_configurator.model.project.active_project import ActiveProject
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase

from pathlib import Path
import os
import shutil

if TYPE_CHECKING:
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion


def _prepare_project_folder(path_to_new_project: Path, path_old_data: Path):
    # Prepare result folder
    deleter: FileDeletion = file_deletion.FileDeletion()
    deleter.reset_folder(path_to_new_project)

    # move the files from data to it
    try:
        shutil.copytree(path_old_data, path_to_new_project)
    except:
        pass

    with open(os.path.join(path_to_new_project, "application_settings.csv"), "w") as file:
        file.write(str(path_to_new_project))



class TestActiveProject:
    def test_build(self):
        self.active_project: ActiveProject = ActiveProject(os.path.join(TEST_DIR, "data/"), True, "TestProject1", "Das sollte funktionieren")
        self.active_project.set_last_step(ConfigPhase.CATEGORY_CONFIG_PHASE)
        self.active_project.get_project_saver().save_project()

    def test_load(self):
        self.test_build()
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.assertEqual(self.active_project.get_last_step(), ConfigPhase.CATEGORY_CONFIG_PHASE)

    def test_load_without_name(self):
        self.test_build()
        path: Path = Path("C:\TestProject1")
        self.active_project: ActiveProject = ActiveProject(path, False,)
        self.assertEqual(self.active_project.get_last_step(), ConfigPhase.CATEGORY_CONFIG_PHASE)

    def test_getter_config(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, True, "TestProject3", "Das sollte funktionieren")
        self.assertEqual(self.active_project.get_last_step(), ConfigPhase.DATA_CONFIG_PHASE)

    def test_setter_config(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, True, "TestProject4", "Das sollte funktionieren")
        self.assertEqual(self.active_project.set_last_step(ConfigPhase.CATEGORY_CONFIG_PHASE), True)
        self.assertEqual(self.active_project.get_last_step(), ConfigPhase.CATEGORY_CONFIG_PHASE)

    def test_path(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, True, "TestProject4", "Das sollte sda")
        self.assertEqual(self.active_project.get_project_path(), Path("C:TestProject4"))

    def test_name_edit(self):
        self.test_build()
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.active_project.get_project_settings().change_name("TestProjectNewName")
        self.active_project.get_project_saver().save_project()
