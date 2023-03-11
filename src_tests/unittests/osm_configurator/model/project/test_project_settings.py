from __future__ import annotations

import os
import shutil

from src.osm_configurator.model.project.active_project import ActiveProject
from src.osm_configurator.model.project.calculation import file_deletion
from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion
from src.osm_configurator.model.project.project_settings import ProjectSettings
from pathlib import Path

from src_tests.definitions import TEST_DIR


def _prepare_project_folder(path_to_new_project: Path, path_old_data: Path):
    # Prepare result folder
    deleter: FileDeletion = file_deletion.FileDeletion()
    deleter.reset_folder(path_to_new_project)

    # move the files from data to it
    try:
        shutil.copytree(path_old_data, path_to_new_project)
    except:
        pass
    with open(os.path.join(path_to_new_project, "application_settings.json"), "w") as file:
        file.write(str(path_to_new_project))

class TestProjectSettings:
    def test_get_getter(self):
        project_settings: ProjectSettings = ProjectSettings(Path(os.path.join(TEST_DIR, "build/Projects/TestName")),
                                                            "TestName", "TestDescription")
        project_settings.set_last_edit_date("TestDate")
        assert project_settings.get_location() == Path(os.path.join(TEST_DIR, "build/Projects/TestName"))
        assert project_settings.get_name() == "TestName"
        assert project_settings.get_description() == "TestDescription"
        assert project_settings.get_last_edit_date() == "TestDate"

    def test_set_name_error(self):
        project_settings: ProjectSettings = ProjectSettings(Path(os.path.join(TEST_DIR, "build/Projects/TestName")),
                                                            "TestName", "TestDescription")
        assert not project_settings.set_name(1)
        assert project_settings.get_name() == "TestName"

    def test_set_description_error(self):
        project_settings: ProjectSettings = ProjectSettings(Path(os.path.join(TEST_DIR, "build/Projects/TestName")),
                                                            "TestName", "TestDescription")
        assert not project_settings.set_description(1)
        assert project_settings.get_description() == "TestDescription"

    def test_set_location_error(self):
        project_settings: ProjectSettings = ProjectSettings(Path(os.path.join(TEST_DIR, "build/Projects/TestName")),
                                                            "TestName", "TestDescription")
        assert not project_settings.set_location(Path(os.path.join(TEST_DIR, "build/Projects/Other")))
        assert project_settings.get_location() == Path(os.path.join(TEST_DIR, "build/Projects/TestName"))
