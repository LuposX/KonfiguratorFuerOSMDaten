
from __future__ import annotations

from typing import TYPE_CHECKING

import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

from src.osm_configurator.model.application.application import Application
from src_tests.definitions import TEST_DIR

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
    try:
        shutil.copytree(path_old_data, path_to_new_project)
    except:
        pass

    with open(os.path.join(path_to_new_project, "application_settings.csv"), "w") as file:
        file.write(str(path_to_new_project))


class TestSettingsSaver:
    def test_save_settings(self):
        _prepare_application_folder(os.path.join(TEST_DIR, "build/application"), os.path.join(TEST_DIR, "data/application"))

        app: Application = Application(os.path.join(TEST_DIR, "build/application/application_settings.csv"))

        app.get_application_settings().set_default_location(os.path.join(TEST_DIR, "build/application"))

        app.save()

