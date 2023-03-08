import os
from pathlib import Path

from src.osm_configurator.model.project.active_project import ActiveProject
from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.application.application_settings as application_settings_i


class TestUseCase22:
    def test_export_config(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True,
                                                           application_settings_o, "Project_UC22", "Test export config")
        assert self.active_project.get_export_manager().export_configuration(
            Path(os.path.join(TEST_DIR, "build/Export/UC22")))
