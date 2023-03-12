from __future__ import annotations

from pathlib import Path
import os
from src_tests.definitions import TEST_DIR

import src.osm_configurator.control.project_controller as project_controller
import src.osm_configurator.control.aggregation_controller as aggregation_controller

import src.osm_configurator.model.application.application as application
import src.osm_configurator.model.project.calculation.aggregation_method_enum as aggregation_method_enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.aggregation_controller_interface import IAggregationController

    from src.osm_configurator.model.application.application_interface import IApplication


class TestUseCase06:
    def test_successful_project_loading(self):
        # Create Model and Controller
        model: IApplication = application.Application()
        project_ctrl: IProjectController = project_controller.ProjectController(model)
        aggregation_ctrl: IAggregationController = aggregation_controller.AggregationController(model)

        # Load project
        assert not project_ctrl.is_project_loaded()
        assert project_ctrl.load_project(Path(os.path.join(TEST_DIR, "data/use_cases/example_project/use_case_project")))
        assert project_ctrl.is_project_loaded()

        # Check aggregtaion methods of project
        assert aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.MAXIMUM)
        assert aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.MINIMUM)
        assert not aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.STANDARD_DERIVATIVE)
        assert not aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.VARIANCE)
        assert not aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.SUM)

        # Set aggregation methods
        assert aggregation_ctrl.set_aggregation_method_active(aggregation_method_enum.AggregationMethod.MAXIMUM, False)
        assert aggregation_ctrl.set_aggregation_method_active(aggregation_method_enum.AggregationMethod.SUM, True)

        # Check aggregation methods again
        assert not aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.MAXIMUM)
        assert aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.MINIMUM)
        assert not aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.STANDARD_DERIVATIVE)
        assert not aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.VARIANCE)
        assert aggregation_ctrl.is_aggregation_method_active(aggregation_method_enum.AggregationMethod.SUM)