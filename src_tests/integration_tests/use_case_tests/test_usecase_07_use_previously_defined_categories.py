from __future__ import annotations
import pytest
from typing import TYPE_CHECKING

from pathlib import Path
import os
from src_tests.definitions import TEST_DIR

import src.osm_configurator.control.category_controller as category_controller
import src.osm_configurator.model.application.application as application
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

if TYPE_CHECKING:
    from src.osm_configurator.control.category_controller import ICategoryController
    from src.osm_configurator.model.application.application_interface import IApplication


def prepare_controller(proj_to_load: Path) -> ICategoryController:
    model: IApplication = application.Application()
    model.load_project(proj_to_load)
    cat_ctrl: ICategoryController = category_controller.CategoryController(model)
    return cat_ctrl


class TestUseCase07:
    def test_successful_category_import(self):
        # Prepare
        data_path: Path = Path(os.path.join(TEST_DIR, "data/use_case_07/categories"))
        project_path: Path = Path(os.path.join(TEST_DIR, "data/use_case_07/heyo"))

        test_folder_path: Path = Path(os.path.join(TEST_DIR, "build/use_cases/uc07"))

        file_deletion.FileDeletion().reset_folder(test_folder_path)

        cat_ctrl, model = prepare_controller(project_path)

        # Test if project creation is successful
        assert cat_ctrl.import_category_configuration(data_path)
