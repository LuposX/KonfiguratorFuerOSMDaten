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
    from src.osm_configurator.model.project.configuration.category import Category


def prepare_controller(proj_to_load: Path) -> ICategoryController:
    model: IApplication = application.Application()
    model.load_project(proj_to_load)
    cat_ctrl: ICategoryController = category_controller.CategoryController(model)
    return cat_ctrl


class TestUseCase08:
    def test_successful_category_creation(self):
        # Prepare
        project_path: Path = Path(os.path.join(TEST_DIR, "data/use_case_07/heyo"))
        test_folder_path: Path = Path(os.path.join(TEST_DIR, "build/use_cases/uc08"))
        file_deletion.FileDeletion().reset_folder(test_folder_path)
        cat_ctrl: ICategoryController = prepare_controller(project_path)

        # Test if project creation is successful
        res_cat: Category | None = cat_ctrl.create_category("holy_Crackers")
        assert res_cat is not None
        assert res_cat.get_category_name() == "holy_Crackers"

        # Test if project creation is successful
        res_cat: Category | None = cat_ctrl.create_category("aud hahui huiahuidu 2 28948892")
        assert res_cat is not None
        assert res_cat.get_category_name() == "aud hahui huiahuidu 2 28948892"

    def test_unsuccessful_category_creation(self):
        # Prepare
        project_path: Path = Path(os.path.join(TEST_DIR, "data/use_case_07/heyo"))
        test_folder_path: Path = Path(os.path.join(TEST_DIR, "build/use_cases/uc08"))
        file_deletion.FileDeletion().reset_folder(test_folder_path)
        cat_ctrl: ICategoryController = prepare_controller(project_path)

        # Test if project creation is successful
        res_cat: Category | None = cat_ctrl.create_category("")
        assert res_cat is None

        # Test if project creation is successful
        res_cat: Category | None = cat_ctrl.create_category("/(/()§$§%")
        assert res_cat is None

