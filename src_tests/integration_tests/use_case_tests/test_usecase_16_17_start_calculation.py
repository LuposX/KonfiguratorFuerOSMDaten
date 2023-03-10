from __future__ import annotations

import time
from pathlib import Path
import os
from src_tests.definitions import TEST_DIR

import src.osm_configurator.control.project_controller as project_controller
import src.osm_configurator.control.osm_data_controller as osm_data_controller
import src.osm_configurator.control.cut_out_controller as cut_out_controller
import src.osm_configurator.control.calculation_controller as calculation_controller

import src.osm_configurator.model.application.application as application
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.osm_data_controller_interface import IOSMDataController
    from src.osm_configurator.control.cut_out_controller_interface import ICutOutController
    from src.osm_configurator.control.calculation_controller_interface import ICalculationController

    from src.osm_configurator.model.application.application_interface import IApplication


class TestUseCase1617:
    def test_calculation_start(self):
        # Create Model and Controller
        model: IApplication = application.Application()
        project_ctrl: IProjectController = project_controller.ProjectController(model)
        data_ctrl: IOSMDataController = osm_data_controller.OSMDataController(model)
        cut_out_ctrl: ICutOutController = cut_out_controller.CutOutController(model)
        calculation_ctrl: ICalculationController = calculation_controller.CalculationController(model)

        # Prepare test project with valid OSM and geojson data
        assert not project_ctrl.is_project_loaded()
        assert project_ctrl.load_project(Path(os.path.join(TEST_DIR, "data/use_cases/example_project/use_case_project")))
        assert project_ctrl.is_project_loaded()
        osm_data: Path = Path(os.path.join(TEST_DIR, "data/monaco-latest.osm"))
        assert data_ctrl.set_osm_data_reference(osm_data)
        geojson_data: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
        assert cut_out_ctrl.set_cut_out_reference(geojson_data)

        # Test before calculation started
        assert calculation_ctrl.get_calculation_state()[0] == calculation_state_enum.CalculationState.NOT_STARTED_YET
        assert calculation_ctrl.get_current_calculation_phase() == calculation_phase_enum.CalculationPhase.NONE
        assert calculation_ctrl.get_current_calculation_progress() <= 0

        # Start calculation (Use case 16)
        assert calculation_ctrl.start_calculations(calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE)

        # Check if calculation is correctly starting up (waiting for it at most 10 seconds)
        i: int
        for i in range(20):
            time.sleep(0.5)
            if i == 19:
                assert False
            if calculation_ctrl.get_current_calculation_phase() == calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE:
                break

        assert calculation_ctrl.get_calculation_state()[0] == calculation_state_enum.CalculationState.RUNNING
        assert calculation_ctrl.get_current_calculation_phase() == calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE
        assert calculation_ctrl.get_current_calculation_progress() == 0

        # Canceling the calculation (Usecase 17)
        assert calculation_ctrl.cancel_calculations()

        # Testing if cancelation was successful
        assert calculation_ctrl.get_calculation_state()[0] == calculation_state_enum.CalculationState.CANCELED
