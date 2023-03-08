import os
from pathlib import Path

from src.osm_configurator.model.project.active_project import ActiveProject
from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.application.application_settings as application_settings_i


class TestUseCase21:

    def test_export_project(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True,
                                                           application_settings_o, "Project_UC22",
                                                           "Das sollte funktionieren")
        self.active_project.get_export_manager().export_project(
            Path(os.path.join(TEST_DIR, "build/Export/UC21")))
