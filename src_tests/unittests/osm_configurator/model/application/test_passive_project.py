from pathlib import Path

from src.osm_configurator.model.application.passive_project import PassiveProject


class TestPassiveProject:
    def test_passive_project(self):
        passive_project: PassiveProject = PassiveProject("project_settings.csv")
        assert "TestProject1" == passive_project.get_name()
        assert "Das sollte funktionieren" == passive_project.get_description()