from pathlib import Path
import os
from src_tests.definitions import TEST_DIR

import src.osm_configurator.control.project_controller as project_controller
import src.osm_configurator.control.category_controller as category_controller
import src.osm_configurator.control.aggregation_controller as aggregation_controller

import src.osm_configurator.model.application.application as application
import src.osm_configurator.model.project.calculation.aggregation_method_enum as aggregation_method_enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.category_controller_interface import ICategoryController
    from src.osm_configurator.control.aggregation_controller_interface import IAggregationController
    from src.osm_configurator.model.application.application_interface import IApplication


class TestUseCase0304:
    def test_successful_project_loading(self):
        # Create Model and Controller
        model: IApplication = application.Application()
        project_ctrl: IProjectController = project_controller.ProjectController(model)
        category_ctrl: ICategoryController = category_controller.CategoryController(model)
        aggregation_ctrl: IAggregationController = aggregation_controller.AggregationController(model)

        # Load project
        assert not project_ctrl.is_project_loaded()
        assert project_ctrl.load_project(Path(os.path.join(TEST_DIR, "data/use_cases/uc03_04/uc_03_project")))
        assert project_ctrl.is_project_loaded()

        # Test, if project was loaded correctly
        assert len(category_ctrl.get_list_of_categories()) == 2
        assert len(category_ctrl.get_attractivities_of_category(category_ctrl.get_list_of_categories()[0])) == 0
        assert len(category_ctrl.get_attractivities_of_category(category_ctrl.get_list_of_categories()[1])) == 1
        assert aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.MAXIMUM)
        assert not aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.VARIANCE)
        assert not aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.MEAN)
