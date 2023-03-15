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


class TestUseCase09:
    def test_successful_inspect_category(self):
        # Prepare
        project_path: Path = Path(os.path.join(TEST_DIR, "data/use_case_07/heyo"))
        test_folder_path: Path = Path(os.path.join(TEST_DIR, "build/use_cases/uc08"))
        file_deletion.FileDeletion().reset_folder(test_folder_path)
        cat_ctrl: ICategoryController = prepare_controller(project_path)

        # Test if project creation is successful
        res_cat: Category | None = cat_ctrl.create_category("holy_Crackers")
        res_cat.set_whitelist(["hallo", "copium", "kobeni", "power"])
        res_cat.set_blacklist(["2838", "fsifios32", "29jfis"])
        assert res_cat is not None
        assert res_cat.get_category_name() == "holy_Crackers"
        assert res_cat.get_whitelist() == ["hallo", "copium", "kobeni", "power"]
        assert res_cat.get_blacklist() == ["2838", "fsifios32", "29jfis"]
