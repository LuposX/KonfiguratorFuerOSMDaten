from pathlib import Path

import os

from src.osm_configurator.model.application.passive_project import PassiveProject
from src_tests.definitions import TEST_DIR
from pathlib import Path


class TestPassiveProject:
    def test_passive_project(self):
        passive_project: PassiveProject = PassiveProject(Path(os.path.join(TEST_DIR, "data/application/project_settings.csv")))
        assert "TestProject1" == passive_project.get_name()
        assert "Das sollte funktionieren" == passive_project.get_description()
