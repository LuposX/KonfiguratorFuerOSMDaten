import unittest
from pathlib import Path

from src.osm_configurator.model.application.passive_project import PassiveProject


class MyTestCase(unittest.TestCase):
    def test_passive_project(self):
        passive_project: PassiveProject = PassiveProject("project_settings.csv")
        self.assertEqual("TestProject1", passive_project.get_name())
        self.assertEqual("Das sollte funktionieren", passive_project.get_description())
        # self.assertEqual(Path("C:"), passive_project.get_project_folder_path())


if __name__ == '__main__':
    unittest.main()
