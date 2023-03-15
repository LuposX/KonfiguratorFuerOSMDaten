import os
from pathlib import Path

from src.osm_configurator.model.project.active_project import ActiveProject
from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.application.application_settings as application_settings_i


class TestUseCase20:

    def test_export_results(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True,
                                                           application_settings_o, "Project_UC20",
                                                           "Test export results")
        assert self.active_project.get_export_manager().export_calculation(
            Path(os.path.join(TEST_DIR, "build/Export/UC20")))
        assert os.path.exists(Path(os.path.join(TEST_DIR, "build/Export/UC20.zip")))
