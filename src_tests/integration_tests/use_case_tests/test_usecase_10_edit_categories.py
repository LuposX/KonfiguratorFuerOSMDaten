from __future__ import annotations

from pathlib import Path
import os
from src_tests.definitions import TEST_DIR

import src.osm_configurator.control.project_controller as project_controller
import src.osm_configurator.control.category_controller as category_controller

import src.osm_configurator.model.application.application as application
import src.osm_configurator.model.project.configuration.category as category

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.category_controller_interface import ICategoryController
    from src.osm_configurator.model.application.application_interface import IApplication
    from src.osm_configurator.model.project.configuration.category import Category


class TestUseCase0304:
    def test_successful_project_loading(self):
        # Create Model and Controller
        model: IApplication = application.Application()
        project_ctrl: IProjectController = project_controller.ProjectController(model)
        category_ctrl: ICategoryController = category_controller.CategoryController(model)

        # Load project
        assert not project_ctrl.is_project_loaded()
        assert project_ctrl.create_project("project",
                                           "Description",
                                           Path(os.path.join(TEST_DIR, "build/use_cases/uc10/project")))
        assert project_ctrl.is_project_loaded()

        # Prepare categories
        # Default category exists by default
        cat_1: Category = category_ctrl.create_category("Category1")
        cat_2: Category = category_ctrl.create_category("Category2")

        # Check for valid categories
        assert len(category_ctrl.get_list_of_categories()) == 3
        assert cat_1.get_category_name() == "Category1"
        assert cat_2.get_category_name() == "Category2"

        # Edit categories
        # Edit names
        assert cat_1.set_category_name("Tom")
        assert cat_1.get_category_name() == "Tom"
        assert cat_2.get_category_name() == "Category2"

        # Edit black and whitelist
        cat_1.set_blacklist(["building=*", "time=5"])
        cat_1.set_whitelist(["building=hospital", "hello=True"])
        cat_2.set_whitelist(["building=hospital"])

        assert cat_1.get_blacklist() == ["building=*", "time=5"]
        assert cat_1.get_whitelist() == ["building=hospital", "hello=True"]
        assert cat_2.get_blacklist() == []
        assert cat_2.get_whitelist() == ["building=hospital"]

        # Extension 1a: Key Recommendations
        assert "building" in category_ctrl.get_list_of_key_recommendations("buildi")

        # Extension 2a: Activation/Deactivation of categories
        assert cat_1.is_active()
        assert cat_2.is_active()

        assert cat_1.activate()
        assert cat_2.activate()
        assert cat_1.is_active()
        assert cat_2.is_active()

        assert cat_1.deactivate()
        assert not cat_1.is_active()
        assert cat_2.is_active()
