from __future__ import annotations
import pytest
from typing import TYPE_CHECKING

from pathlib import Path
import os
from src_tests.definitions import TEST_DIR

import src.osm_configurator.control.category_controller as category_controller
import src.osm_configurator.control.aggregation_controller as aggregation_controller
import src.osm_configurator.control.project_controller as project_controller
import src.osm_configurator.control.data_visualization_controller as data_visualization_controller
import src.osm_configurator.model.application.application as application
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

if TYPE_CHECKING:
    from src.osm_configurator.control.category_controller import ICategoryController
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.aggregation_controller_interface import IAggregationController
    from src.osm_configurator.model.application.application_interface import IApplication


class TestUseCase18:
    def test_successful_category_import(self):
        pass

        # Works only locally, not in github.
        # --------------------
        # # Create Model and Controller
        # model: IApplication = application.Application()
        # project_ctrl: IProjectController = project_controller.ProjectController(model)
        # category_ctrl: ICategoryController = category_controller.CategoryController(model)
        # aggregation_ctrl: IAggregationController = aggregation_controller.AggregationController(model)
        # data_viz_controller = data_visualization_controller.DataVisualizationController(model)
        #
        # # Load project
        # assert not project_ctrl.is_project_loaded()
        # assert project_ctrl.load_project(
        #     Path(os.path.join(TEST_DIR, "data/UseCase18")))
        # assert project_ctrl.is_project_loaded()
        #
        # # Test if visualization is successful
        # assert data_viz_controller.generate_calculation_visualization() is not None
        # assert data_viz_controller.generate_cut_out_map() is not None
