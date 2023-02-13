
from __future__ import annotations

from typing import TYPE_CHECKING

import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

import src.osm_configurator.model.application.application_settings_default_enum as application_settings_enum_i
import src.osm_configurator.model.application.application_settings as application_settings_i
from src.osm_configurator.model.application.application import Application
from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.application.application_settings_default_enum as application_settings_enum_i

from pathlib import Path
import os
import shutil
import json

if TYPE_CHECKING:
    from typing import Dict
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

    application_settings_i.ApplicationSettings.create_application_settings_file(path_to_new_project,
                                                                                "application_settings.json")


class TestSettingsSaver:
    def test_save_settings(self):
        _prepare_application_folder(os.path.join(TEST_DIR, "build/application"), os.path.join(TEST_DIR, "data/application"))

        app: Application = Application(Path(os.path.join(TEST_DIR, "build/application/application_settings.json")))

        app.get_application_settings().set_setting(application_settings_enum_i.ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER,
                                                   os.path.join(TEST_DIR, "build/application"))

