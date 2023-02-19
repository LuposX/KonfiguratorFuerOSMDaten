from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import TYPE_CHECKING

from src.osm_configurator.model.project.active_project import ActiveProject
from src.osm_configurator.model.project.calculation import file_deletion
from src_tests.definitions import TEST_DIR

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
    with open(os.path.join(path_to_new_project, "application_settings.json"), "w") as file:
        file.write(str(path_to_new_project))


class TestExport:
    def test_export(self):
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, "TestProjectExport", "Das sollte funktionieren")
        self.active_project.get_export_manager().export_project(Path(os.path.join(TEST_DIR, "build/Export/ProjectZIP")))
