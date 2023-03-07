from __future__ import annotations

from pathlib import Path
import os
from src_tests.definitions import TEST_DIR

import src.osm_configurator.control.project_controller as project_controller
import src.osm_configurator.control.category_controller as category_controller

import src.osm_configurator.model.application.application as application

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.category_controller_interface import ICategoryController
    from src.osm_configurator.model.application.application_interface import IApplication
    from src.osm_configurator.model.project.configuration.category import Category


class TestUseCase11:
    def test_successful_category_removal(self):
        # Create Model and Controller
        model: IApplication = application.Application()
        project_ctrl: IProjectController = project_controller.ProjectController(model)
        category_ctrl: ICategoryController = category_controller.CategoryController(model)

        # Load project
        assert not project_ctrl.is_project_loaded()
        assert project_ctrl.create_project("project",
                                           "Description",
                                           Path(os.path.join(TEST_DIR, "build/use_cases/uc11/project")))
        assert project_ctrl.is_project_loaded()

        # Prepare categories
        # Default category exists by default
        cat_1: Category = category_ctrl.create_category("Category1")
        cat_2: Category = category_ctrl.create_category("Category2")

        # Check for valid categories
        assert len(category_ctrl.get_list_of_categories()) == 3
        assert cat_1 in category_ctrl.get_list_of_categories()
        assert cat_2 in category_ctrl.get_list_of_categories()

        # Test removal
        assert category_ctrl.delete_category(cat_1)
        assert len(category_ctrl.get_list_of_categories()) == 2
        assert cat_1 not in category_ctrl.get_list_of_categories()
        assert cat_2 in category_ctrl.get_list_of_categories()

        # Test removal of non existing category
        assert not category_ctrl.delete_category(cat_1)
        assert len(category_ctrl.get_list_of_categories()) == 2
        assert cat_1 not in category_ctrl.get_list_of_categories()
        assert cat_2 in category_ctrl.get_list_of_categories()

        # Test second removal
        assert category_ctrl.delete_category(cat_2)
        assert len(category_ctrl.get_list_of_categories()) == 1
        assert cat_1 not in category_ctrl.get_list_of_categories()
        assert cat_2 not in category_ctrl.get_list_of_categories()
