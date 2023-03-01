from __future__ import annotations
import pytest
from typing import TYPE_CHECKING

from pathlib import Path
import os
from src_tests.definitions import TEST_DIR

import src.osm_configurator.control.project_controller as project_controller
import src.osm_configurator.model.application.application as application
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

if TYPE_CHECKING:
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.model.application.application_interface import IApplication


def prepare_project_controller() -> IProjectController:
    model: IApplication = application.Application()
    project_ctrl: IProjectController = project_controller.ProjectController(model)
    return project_ctrl


class TestUseCase02:
    @pytest.mark.parametrize("name, description", [
        ("Projekt1", "asjafalsfhiaf"),
        ("Sieben", "hadahsdihas"),
        ("Hallo Welt", "Beschreibung \n klar")
    ])
    def test_successful_project_creation(self, name: str, description: str):
        # Prepare
        test_folder_path: Path = Path(os.path.join(TEST_DIR, "build/use_cases/uc02"))
        project_path: Path = Path(os.path.join(test_folder_path, name))
        file_deletion.FileDeletion().reset_folder(project_path)
        project_ctrl: IProjectController = prepare_project_controller()

        # Test if project creation is successful
        assert project_ctrl.create_project(name, description, test_folder_path)

        # Test if project was set up correctly
        assert project_ctrl.is_project_loaded()
        assert project_ctrl.get_project_path() == project_path
