import os
from pathlib import Path

from src.osm_configurator.model.application.application import Application

from src_tests.definitions import TEST_DIR

class TestSettingsSaver:
    def test_save_settings(self):
        try:
            os.makedirs(os.path.join(TEST_DIR, "build/ApplicationTest"), 0o666)
        except:
            pass
        app: Application = Application()
        app.save(os.path.join(TEST_DIR, "build/ApplicationTest"))
