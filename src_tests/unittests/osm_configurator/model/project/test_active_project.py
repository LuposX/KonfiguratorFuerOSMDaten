import unittest

import shutil

from src.osm_configurator.model.project.active_project import ActiveProject
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
from pathlib import Path


class MyTestCase(unittest.TestCase):
    def test_build(self):
        self.assertEqual(True, True)  # add assertion here
        path: Path = Path("C:\Arbeitsplatz\AA_PSE_tests")
        self.active_project: ActiveProject = ActiveProject(path, True, "TestProject1", "Das sollte funktionieren")

    def test_load(self):
        shutil.rmtree("C:\Arbeitsplatz\AA_PSE_tests\TestProject2")
        path: Path = Path("C:\Arbeitsplatz\AA_PSE_tests")
        self.active_project: ActiveProject = ActiveProject(path, True, "TestProject2", "Das sollte funktionieren")
        self.active_project.get_project_saver().save_project()

    def test_getter_config(self):
        path: Path = Path("C:\Arbeitsplatz\AA_PSE_tests")
        self.active_project: ActiveProject = ActiveProject(path, True, "TestProject3", "Das sollte funktionieren")
        self.assertEqual(self.active_project.get_last_step(), ConfigPhase.DATA_CONFIG_PHASE)

    def test_setter_config(self):
        path: Path = Path("C:\Arbeitsplatz\AA_PSE_tests")
        self.active_project: ActiveProject = ActiveProject(path, True, "TestProject4", "Das sollte funktionieren")
        self.assertEqual(self.active_project.set_last_step(ConfigPhase.CATEGORY_CONFIG_PHASE), True)
        self.assertEqual(self.active_project.get_last_step(), ConfigPhase.CATEGORY_CONFIG_PHASE)

    def test_path(self):
        path: Path = Path("C:\Arbeitsplatz\AA_PSE_tests")
        self.active_project: ActiveProject = ActiveProject(path, True, "TestProject4", "Das sollte funktionieren")
        self.assertEqual(self.active_project.get_project_path(), Path("C:\Arbeitsplatz\AA_PSE_tests\TestProject4"))


if __name__ == '__main__':
    unittest.main()
