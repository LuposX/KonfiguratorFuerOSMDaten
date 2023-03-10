from __future__ import annotations

import os
from pathlib import Path

from src.osm_configurator.model.project.active_project import ActiveProject
from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.application.application_settings as application_settings_i


class TestExport:

    def test_export_project(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProjectExport", "Das sollte funktionieren")
        assert self.active_project.get_export_manager().export_project(Path(os.path.join(TEST_DIR, "build/Export/Project")))
        assert os.path.exists(Path(os.path.join(TEST_DIR, "build/Export/Project.zip")))

    def test_export_configuration(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProjectExport", "Das sollte funktionieren")
        assert self.active_project.get_export_manager().export_configuration(Path(os.path.join(TEST_DIR, "build/Export/Configuration")))
        assert os.path.exists(Path(os.path.join(TEST_DIR, "build/Export/Configuration.zip")))

    def test_export_calculation(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProjectExport", "Das sollte funktionieren")
        assert self.active_project.get_export_manager().export_calculation(Path(os.path.join(TEST_DIR, "build/Export/Calculation")))
        assert os.path.exists(Path(os.path.join(TEST_DIR, "build/Export/Calculation.zip")))

    def test_export_map(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProjectExport", "Das sollte funktionieren")
        self.active_project.get_config_manager().get_osm_data_configuration().set_osm_data(Path(os.path.join(TEST_DIR, "data/monaco-latest.osm")))
        self.active_project.get_config_manager().get_cut_out_configuration().set_cut_out_path(Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson")))
        assert self.active_project.get_export_manager().export_map(Path(os.path.join(TEST_DIR, "build/Export/Map")))
        assert os.path.exists(Path(os.path.join(TEST_DIR, "build/Export/Map.html")))
