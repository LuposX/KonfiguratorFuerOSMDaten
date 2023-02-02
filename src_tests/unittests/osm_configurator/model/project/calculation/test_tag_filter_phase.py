from __future__ import annotations

from typing import TYPE_CHECKING
from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.project.calculation.tag_filter_phase as tag_filter_phase_i
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.configuration.configuration_manager as configuration_manager
import src.osm_configurator.model.project.calculation.calculation_phase_utility as calculation_phase_utility
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

import src.osm_configurator.model.project.configuration.cut_out_mode_enum as cut_out_mode_enum_i

from src_tests.definitions import TEST_CATEGORY_BUILDING, TEST_CATEGORY_NO_BUILDING, TEST_CATEGORY_SHOP

from pathlib import Path
import os
import shutil

if TYPE_CHECKING:
    from typing import Tuple
    from src.osm_configurator.model.project.calculation.tag_filter_phase import TagFilterPhase
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion
    from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode

# without this you get a weird error, idk why
os.environ["PROJ_LIB"] = ""


def _prepare_config(geojson: Path, project: Path, assert_existence: bool,
                    cut_out_mode: CutOutMode) -> ConfigurationManager:
    if assert_existence:
        assert os.path.exists(geojson)

    config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project)
    config_manager.get_cut_out_configuration().set_cut_out_path(geojson)

    config_manager.get_cut_out_configuration().set_cut_out_mode(cut_out_mode)

    config_manager.get_category_manager().add_categories([TEST_CATEGORY_BUILDING,
                                                          TEST_CATEGORY_NO_BUILDING,
                                                          TEST_CATEGORY_SHOP])

    return config_manager


def _prepare_previous_phase_folder(path_to_new_proejct: Path, path_old_data: Path):
    # Prepare result folder
    deleter: FileDeletion = file_deletion.FileDeletion()
    deleter.reset_folder(path_to_new_proejct)

    # move the files from data to it
    for file_name in os.listdir(path_old_data):
        shutil.copy2(os.path.join(path_old_data, file_name), path_to_new_proejct)


class TestTagFilterPhase:
    def test_no_configuration(self):
        # Set up
        project_path: Path = Path(os.path.join(TEST_DIR, "build/geo_data_phase/projectXYZ"))
        config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project_path)

        # Execute phase, without setting any path's to the geojson and osm data
        phase: TagFilterPhase = tag_filter_phase_i.TagFilterPhase()
        result: CalculationState = phase.calculate(config_manager)
        assert result[0] == calculation_state_enum.CalculationState.ERROR_INVALID_CUT_OUT_DATA

    def test_invalid_geojson_path(self):
        # Set up paths
        osm_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-latest.osm.pbf"))
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/adhsiadh/auhdhidsa.geojson"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/geo_data_phase/projectABC"))

        config_manager: ConfigurationManager = _prepare_config(geojson_path, project_path, False,
                                                               cut_out_mode_enum_i.CutOutMode.BUILDINGS_ON_EDGE_ACCEPTED                                                               )

        # Execute test
        phase: TagFilterPhase = tag_filter_phase_i.TagFilterPhase()
        result1: CalculationState = phase.calculate(config_manager)
        assert result1[0] == calculation_state_enum.CalculationState.ERROR_INVALID_CUT_OUT_DATA

    def test_full_monaco_instance_successful(self):
        # Set up paths
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/tag_filter_phase/projectXY"))

        # Set up result folder from last phase
        _prepare_previous_phase_folder(os.path.join(os.path.join(project_path, "results/"),
                                                    calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE
                                                    .get_folder_name_for_results()),
                                       os.path.join(TEST_DIR, "data/monaco_split_up_files/"))

        # Set up configurator
        config_manager: ConfigurationManager = _prepare_config(geojson_path, project_path, True,
                                                               cut_out_mode_enum_i.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED)

        # Execute test
        phase: TagFilterPhase = tag_filter_phase_i.TagFilterPhase()
        result1: CalculationState = phase.calculate(config_manager)
        assert result1[0] == calculation_state_enum.CalculationState.RUNNING

        # Test if files were created
        assert len(
            os.listdir(os.path.join(project_path, "results/" + calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE
                                    .get_folder_name_for_results()))) == 8

        # Test if execution works a second time
        result2: CalculationState = phase.calculate(config_manager)
        assert result2[0] == calculation_state_enum.CalculationState.RUNNING

    def test_corrupted_osm_data(self):
        # Set up paths
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/tag_filter_phase/projectXY"))

        # Set up result folder from last phase
        _prepare_previous_phase_folder(os.path.join(os.path.join(project_path, "results/"),
                                                    calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE
                                                    .get_folder_name_for_results()),
                                       os.path.join(TEST_DIR, "data/monaco_split_up_files_invalid/"))

        # Set up configurator
        config_manager: ConfigurationManager = _prepare_config(geojson_path, project_path, True,
                                                               cut_out_mode_enum_i.CutOutMode.BUILDINGS_ON_EDGE_ACCEPTED)

        # Execute test
        phase: TagFilterPhase = tag_filter_phase_i.TagFilterPhase()
        result1: CalculationState = phase.calculate(config_manager)
        assert result1[0] == calculation_state_enum.CalculationState.ERROR_INVALID_OSM_DATA
