from __future__ import annotations

from pathlib import Path
import os
from src_tests.definitions import TEST_DIR

import src.osm_configurator.control.project_controller as project_controller
import src.osm_configurator.control.osm_data_controller as osm_data_controller
import src.osm_configurator.control.cut_out_controller as cut_out_controller

import src.osm_configurator.model.application.application as application
import src.osm_configurator.model.project.configuration.cut_out_mode_enum as cut_out_mode_enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.control.project_controller_interface import IProjectController
    from src.osm_configurator.control.osm_data_controller_interface import IOSMDataController
    from src.osm_configurator.control.cut_out_controller_interface import ICutOutController

    from src.osm_configurator.model.application.application_interface import IApplication


class TestUseCase0304:
    def test_successful_project_loading(self):
        # Create Model and Controller
        model: IApplication = application.Application()
        project_ctrl: IProjectController = project_controller.ProjectController(model)
        data_ctrl: IOSMDataController = osm_data_controller.OSMDataController(model)
        cut_out_ctrl: ICutOutController = cut_out_controller.CutOutController(model)

        # Load project
        assert not project_ctrl.is_project_loaded()
        assert project_ctrl.load_project(Path(os.path.join(TEST_DIR, "data/use_cases/example_project/use_case_project")))
        assert project_ctrl.is_project_loaded()

        # Reference OSM Data
        osm_data: Path = Path(os.path.join(TEST_DIR, "data/monaco-latest.osm"))
        assert data_ctrl.set_osm_data_reference(osm_data)
        assert data_ctrl.get_osm_data_reference() == osm_data

        # Reference geojson Data
        geojson_data: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
        assert cut_out_ctrl.set_cut_out_reference(geojson_data)
        assert cut_out_ctrl.get_cut_out_reference() == geojson_data

        # Set cut out mode
        assert cut_out_ctrl.set_cut_out_mode(cut_out_mode_enum.CutOutMode.BUILDINGS_ON_EDGE_ACCEPTED)
        assert cut_out_ctrl.get_cut_out_mode() == cut_out_mode_enum.CutOutMode.BUILDINGS_ON_EDGE_ACCEPTED

        assert cut_out_ctrl.set_cut_out_mode(cut_out_mode_enum.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED)
        assert cut_out_ctrl.get_cut_out_mode() == cut_out_mode_enum.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED
