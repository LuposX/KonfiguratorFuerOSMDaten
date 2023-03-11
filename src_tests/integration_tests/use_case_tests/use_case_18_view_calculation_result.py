from __future__ import annotations
import pytest
from typing import TYPE_CHECKING

from pathlib import Path
import os
from src_tests.definitions import TEST_DIR

import src.osm_configurator.control.data_visualization_controller as data_visualization_controller_i
import src.osm_configurator.model.application.application as application
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

if TYPE_CHECKING:
    from src.osm_configurator.control.data_visualization_controller import DataVisualizationController
    from src.osm_configurator.model.application.application_interface import IApplication
    from src.osm_configurator.model.project.configuration.category import Category


def prepare_controller(proj_to_load: Path) -> DataVisualizationController:
    model: IApplication = application.Application()
    model.load_project(proj_to_load)
    data_viz_cont: DataVisualizationController = data_visualization_controller_i.DataVisualizationController()
    return data_viz_cont


class TestUseCase18:
    def test_successful_category_creation(self):
        # Prepare
        project_path: Path = Path(os.path.join(TEST_DIR, "data/use_cases/example_project/use_case_project_2"))
        test_folder_path: Path = Path(os.path.join(TEST_DIR, "build/use_cases/uc18"))
        file_deletion.FileDeletion().reset_folder(test_folder_path)
        data_viz_cont: DataVisualizationController = prepare_controller(project_path)

        # Test if project creation is successful
        res_cat: Category | None = use_case_project
        assert res_cat is not None
        assert res_cat.get_category_name() == "holy_Crackers"

        # Test if project creation is successful
        res_cat: Category | None = cat_ctrl.create_category("aud hahui huiahuidu 2 28948892")
        assert res_cat is not None
        assert res_cat.get_category_name() == "aud hahui huiahuidu 2 28948892"

    def test_unsuccessful_category_creation(self):
        # Prepare
       pass
