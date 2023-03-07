from __future__ import annotations

from src.osm_configurator.model.application.application import Application
from src_tests.definitions import TEST_DIR
from src.osm_configurator.model.project.active_project import ActiveProject
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
import src.osm_configurator.model.application.application_settings as application_settings_i

from pathlib import Path
import os


class TestActiveProject:
    def test_build(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProject1", "Das sollte funktionieren")
        self.active_project.set_last_step(ConfigPhase.CATEGORY_CONFIG_PHASE)
        self.active_project.get_project_saver().save_project()

    def test_load(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), False, application_settings_o, "TestProject1")
        assert self.active_project.get_last_step() == ConfigPhase.CATEGORY_CONFIG_PHASE

    def test_load_without_name(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects/TestProject1")), False, application_settings_o)
        assert self.active_project.get_last_step() == ConfigPhase.CATEGORY_CONFIG_PHASE

    def test_getter_config(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProject3", "Das sollte funktionieren")
        assert self.active_project.get_last_step() == ConfigPhase.DATA_CONFIG_PHASE

    def test_setter_config(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProject4", "Das sollte funktionieren")
        assert self.active_project.set_last_step(ConfigPhase.CATEGORY_CONFIG_PHASE)
        assert self.active_project.get_last_step() == ConfigPhase.CATEGORY_CONFIG_PHASE

    def test_path(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProject4", "Das sollte sda")
        assert Path(self.active_project.get_project_path()) == Path(os.path.join(TEST_DIR, "build/Projects/TestProject4"))

    def test_change_name(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProject1")
        assert self.active_project.get_project_settings().change_name("TestProjectNewName")
        assert self.active_project.get_project_settings().get_name() == "TestProjectNewName"
        assert self.active_project.get_project_settings().change_name("TestProject1")

    def test_change_name_error(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProject1")
        assert not self.active_project.get_project_settings().change_name(2)

    def test_change_location_error(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestChangeLocationError")
        assert not self.active_project.get_project_settings().change_location(Path(os.path.join(TEST_DIR, "build/NotExistingFolder")))