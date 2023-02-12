
from __future__ import annotations

from typing import TYPE_CHECKING


import os
from pathlib import Path

from src.osm_configurator.model.application.application import Application

from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion



from pathlib import Path
import os
import shutil

if TYPE_CHECKING:

    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion


def _prepare_application_folder(path_to_new_project: Path, path_old_data: Path):
    # Prepare result folder
    deleter: FileDeletion = file_deletion.FileDeletion()
    deleter.reset_folder(path_to_new_project)

    # move the files from data to it
    for file_name in os.listdir(path_old_data):
        shutil.copy2(os.path.join(path_old_data, file_name), path_to_new_project)


class TestSettingsSaver:
    def test_save_settings(self):
        _prepare_application_folder(os.path.join(TEST_DIR, "build/application"), os.path.join(TEST_DIR, "data/application"))

        app: Application = Application()
        app.get_application_settings().set_default_location(os.path.join(TEST_DIR, "build/application"))

        app.save(os.path.join(TEST_DIR, "build/application"))

