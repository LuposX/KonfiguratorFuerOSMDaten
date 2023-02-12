import os
import unittest
from pathlib import Path

from src.osm_configurator.model.application.application import Application


class MyTestCase(unittest.TestCase):
    def test_save_settings(self):
        os.makedirs("ApplicationTest")
        self.app: Application = Application()
        self.app.save(Path("ApplicationTest"))


if __name__ == '__main__':
    unittest.main()
