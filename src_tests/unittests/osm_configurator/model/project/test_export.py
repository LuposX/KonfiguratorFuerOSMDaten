from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import TYPE_CHECKING

from src.osm_configurator.model.project.active_project import ActiveProject
from src.osm_configurator.model.project.calculation import file_deletion
from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.application.application_settings as application_settings_i


class TestExport:

    def test_export_project(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProjectExport", "Das sollte funktionieren")
        self.active_project.get_export_manager().export_project(Path(os.path.join(TEST_DIR, "build/Export/Project")))

    def test_export_configuration(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProjectExport", "Das sollte funktionieren")
        self.active_project.get_export_manager().export_configuration(Path(os.path.join(TEST_DIR, "build/Export/Configuration")))

    def test_export_calculation(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProjectExport", "Das sollte funktionieren")
        self.active_project.get_export_manager().export_calculation(Path(os.path.join(TEST_DIR, "build/Export/Calculation")))

    def test_export_map(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProjectExport", "Das sollte funktionieren")
        self.active_project.get_export_manager().export_map(Path(os.path.join(TEST_DIR, "build/Export/Map")))