from __future__ import annotations

from typing import TYPE_CHECKING
from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.project.calculation.geo_data_phase as geo_data_phase
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.configuration.configuration_manager as configuration_manager
import src.osm_configurator.model.project.calculation.folder_path_calculator as folder_path_calculator_i
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
from pathlib import Path
import os

if TYPE_CHECKING:
    from src.osm_configurator.model.project.calculation.geo_data_phase import GeoDataPhase
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager


def _prepare_config(osm: Path, geojson: Path, project: Path, assert_existence: bool) -> ConfigurationManager:
    if assert_existence:
        assert os.path.exists(osm)
        assert os.path.exists(geojson)

    config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project)
    config_manager.get_cut_out_configuration().set_cut_out_path(geojson)
    config_manager.get_osm_data_configuration().set_osm_data(osm)
    return config_manager


class TestGeoDataPhase:
    def test_no_configuration(self):
        # Set up
        project_path: Path = Path(os.path.join(TEST_DIR, "build/geo_data_phase/projectXYZ"))
        config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project_path)

        # Execute phase, without setting any path's to the geojson and osm data
        phase: GeoDataPhase = geo_data_phase.GeoDataPhase()
        result: CalculationState = phase.calculate(config_manager)[0]
        assert result == calculation_state_enum.CalculationState.ERROR_INVALID_OSM_DATA or \
               calculation_state_enum.CalculationState.ERROR_INVALID_CUT_OUT_DATA


    def test_invalid_osm_path(self):
        # Set up paths
        osm_path: Path = Path(os.path.join(TEST_DIR, "data/monaco/suiadhoadh/asas.osm.pbf"))
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/geo_data_phase/projectABC"))

        config_manager: ConfigurationManager = _prepare_config(osm_path, geojson_path, project_path, False)

        # Execute test
        phase: GeoDataPhase = geo_data_phase.GeoDataPhase()
        result1: CalculationState = phase.calculate(config_manager)[0]
        assert result1 == calculation_state_enum.CalculationState.ERROR_PROJECT_NOT_SET_UP_CORRECTLY


    def test_invalid_geojson_path(self):
        # Set up paths
        osm_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-latest.osm.pbf"))
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/adhsiadh/auhdhidsa.geojson"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/geo_data_phase/projectABC"))

        config_manager: ConfigurationManager = _prepare_config(osm_path, geojson_path, project_path, False)

        # Execute test
        phase: GeoDataPhase = geo_data_phase.GeoDataPhase()
        result1: CalculationState = phase.calculate(config_manager)[0]
        assert result1 == calculation_state_enum.CalculationState.ERROR_INVALID_CUT_OUT_DATA


    def test_corrupted_osm_data(self):
        # Set up paths
        osm_path: Path = Path(os.path.join(TEST_DIR, "data/invalid_data.txt"))
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/geo_data_phase/projectAZ"))

        # Set up configurator
        config_manager: ConfigurationManager = _prepare_config(osm_path, geojson_path, project_path, True)

        # Execute test
        phase: GeoDataPhase = geo_data_phase.GeoDataPhase()
        result1: CalculationState = phase.calculate(config_manager)[0]
        assert result1 == calculation_state_enum.CalculationState.ERROR_INVALID_OSM_DATA


    def test_corrupted_geojson_data(self):
        # Set up paths
        osm_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-latest.osm.pbf"))
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/invalid_data.txt"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/geo_data_phase/projectAZ"))

        # Set up configurator
        config_manager: ConfigurationManager = _prepare_config(osm_path, geojson_path, project_path, True)

        # Execute test
        phase: GeoDataPhase = geo_data_phase.GeoDataPhase()
        result1: CalculationState = phase.calculate(config_manager)[0]
        assert result1 == calculation_state_enum.CalculationState.ERROR_INVALID_CUT_OUT_DATA


    def test_small_instance_successful(self):
        # Set up paths
        osm_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-latest.osm.pbf"))
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/geo_data_phase/projectXY"))

        # Set up configurator
        config_manager: ConfigurationManager = _prepare_config(osm_path, geojson_path, project_path, True)

        # Execute test
        phase: GeoDataPhase = geo_data_phase.GeoDataPhase()
        result1: CalculationState = phase.calculate(config_manager)[0]
        assert result1 == calculation_state_enum.CalculationState.RUNNING

        folder_path_calculator_o = folder_path_calculator_i.FolderPathCalculator()

        # Test if files were created
        test_file_path: Path = Path(os.path.join(TEST_DIR,
                                                 folder_path_calculator_o.get_checkpoints_folder_path_from_phase
                                                 (config_manager, calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE)),
                                    "0_super_traffic_cell.pbf")
        assert os.path.exists(test_file_path)

        # Test if execution works a second time
        result2: CalculationState = phase.calculate(config_manager)[0]
        assert result2 == calculation_state_enum.CalculationState.RUNNING
