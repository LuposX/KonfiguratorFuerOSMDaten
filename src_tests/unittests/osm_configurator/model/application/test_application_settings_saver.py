import unittest
from pathlib import Path

from src.osm_configurator.model.application.application import Application


class MyTestCase(unittest.TestCase):
    def test_save_settings(self):
        self.app: Application = Application()
        self.app.get_application_settings().set_default_location(Path("C:"))
        self.app.save(Path("C:"))


if __name__ == '__main__':
    unittest.main()
