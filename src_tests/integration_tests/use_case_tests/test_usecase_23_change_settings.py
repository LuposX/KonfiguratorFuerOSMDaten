import os
from pathlib import Path

from src.osm_configurator.model.application.application import Application
from src.osm_configurator.model.project.active_project import ActiveProject
import src.osm_configurator.model.application.application_settings as application_settings_i
from src_tests.definitions import TEST_DIR

def prepare(self):
    application_settings_o = application_settings_i.ApplicationSettings()
    self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/use_cases")), True,
                                                       application_settings_o, "Project23",
                                                       "This project is to test!")
    self.active_project.get_project_saver().save_project()


class TestUseCase23:
    def test_change_name(self):
        test_folder_path: Path = Path(os.path.join(TEST_DIR, "build/use_cases"))
        self.application: Application = Application()
        self.application.create_project("Project23", "This project is to test!", test_folder_path)
        assert self.application.get_active_project().get_project_settings().get_name() == "Project23"
        assert self.application.get_active_project().get_project_settings().change_name("ChangedProject23")
        assert self.application.get_active_project().get_project_settings().get_name() == "ChangedProject23"
        self.application.get_active_project().get_project_settings().change_name("Project23")

    def test_change_description(self):
        test_folder_path: Path = Path(os.path.join(TEST_DIR, "build/use_cases"))
        self.application: Application = Application()
        self.application.create_project("Project23", "This project is to test!", test_folder_path)
        assert self.application.get_active_project().get_project_settings().get_description() == "This project is to test!"
        assert self.application.get_active_project().get_project_settings().set_description("Changed")
        assert self.application.get_active_project().get_project_settings().get_description() == "Changed"

    """
     def test_change_location(self):
        test_folder_path: Path = Path(os.path.join(TEST_DIR, "build/use_cases"))
        self.application: Application = Application()
        self.application.create_project("Project23", "This project is to test!", test_folder_path)
        assert Path(self.application.get_active_project().get_project_settings().get_location()) == Path(os.path.join(TEST_DIR, "build/use_cases/Project23"))
        assert self.application.get_active_project().get_project_settings().change_location(Path(os.path.join(TEST_DIR, "build/export")))
        assert Path(self.application.get_active_project().get_project_settings().get_location()) == Path(os.path.join(TEST_DIR, "build/export/Project23"))
        self.application.get_active_project().get_project_settings().change_location(test_folder_path)
    """
