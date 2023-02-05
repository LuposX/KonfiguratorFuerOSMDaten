from __future__ import annotations

from typing import TYPE_CHECKING
from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.project.calculation.tag_filter_phase as tag_filter_phase_i
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.configuration.configuration_manager as configuration_manager
import src.osm_configurator.model.project.calculation.folder_path_calculator as folder_path_calculator_i
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion
import src.osm_configurator.model.project.calculation.reduction_phase as reduction_phase_i

import src.osm_configurator.model.project.configuration.cut_out_mode_enum as cut_out_mode_enum_i

from src_tests.definitions import TEST_CATEGORY_SITE_AREA, TEST_CATEGORY_BUILDING_AREA, TEST_CATEGORY_SHOP, TEST_CATEGORY_NO_BUILDING

from pathlib import Path
import os
import shutil

if TYPE_CHECKING:
    from typing import Tuple
    from src.osm_configurator.model.project.calculation.tag_filter_phase import TagFilterPhase
    from src.osm_configurator.model.project.calculation.reduction_phase import ReductionPhase
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

    config_manager.get_cut_out_configuration().set_cut_out_mode(cut_out_mode)

    config_manager.get_category_manager().add_categories([TEST_CATEGORY_SITE_AREA,
                                                          TEST_CATEGORY_BUILDING_AREA,
                                                          TEST_CATEGORY_SHOP,
                                                          TEST_CATEGORY_NO_BUILDING])

    return config_manager


def _prepare_previous_phase_folder(path_to_new_proejct: Path, path_old_data: Path, iddir: bool):
    # Prepare result folder
    deleter: FileDeletion = file_deletion.FileDeletion()
    deleter.reset_folder(path_to_new_proejct)

    if iddir:
        # move the files from data to it
        for file_name in os.listdir(path_old_data):
            shutil.copy2(os.path.join(path_old_data, file_name), path_to_new_proejct)
    else:
        shutil.copy2(path_old_data, path_to_new_proejct)


class TestReductionPhase:
    def test_reduction_phase_minimal(self):
        # Set up paths
        project_path: Path = Path(os.path.join(TEST_DIR, "build/reduction_phase/projectXY"))
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))

        # Set up result folder from last phase
        # so delete folder from previous test runs and copy the data into it
        _prepare_previous_phase_folder(os.path.join(os.path.join(project_path, "results/"),
                                                    calculation_phase_enum.CalculationPhase.TAG_FILTER_PHASE
                                                    .get_folder_name_for_results()),
                                       os.path.join(TEST_DIR, "data/reduction_test_property_area.csv"),
                                       False
                                       )

        # Set up configurator
        config_manager: ConfigurationManager = _prepare_config(geojson_path, project_path, True,
                                                               cut_out_mode_enum_i.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED)

        # Execute test
        phase: ReductionPhase = reduction_phase_i.ReductionPhase()
        result1: CalculationState = phase.calculate(config_manager)

        assert result1[0] == calculation_state_enum.CalculationState.RUNNING

        # Test if files were created
        assert len(
            os.listdir(os.path.join(project_path, "results/" + calculation_phase_enum.CalculationPhase.REDUCTION_PHASE.get_folder_name_for_results()))) == 1

        # Test if execution works a second time
        result2: CalculationState = phase.calculate(config_manager)
        assert result2[0] == calculation_state_enum.CalculationState.RUNNING


    def test_reduction_phase_fully(self):
        # Set up paths
        project_path: Path = Path(os.path.join(TEST_DIR, "build/reduction_phase/projectXY"))
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))

        # Minimal test case is only one file.
        _prepare_previous_phase_folder(os.path.join(os.path.join(project_path, "results/"),
                                                    calculation_phase_enum.CalculationPhase.TAG_FILTER_PHASE
                                                    .get_folder_name_for_results()),
                                       os.path.join(TEST_DIR, "data/monaco_reduction_phase_valid/"),
                                       True
                                       )

        # Set up configurator
        config_manager: ConfigurationManager = _prepare_config(geojson_path, project_path, True,
                                                               cut_out_mode_enum_i.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED)

        # Execute test
        phase: ReductionPhase = reduction_phase_i.ReductionPhase()
        result1: CalculationState = phase.calculate(config_manager)

        assert result1[0] == calculation_state_enum.CalculationState.RUNNING

        # Test if files were created
        assert len(
            os.listdir(os.path.join(project_path, "results/" + calculation_phase_enum.CalculationPhase.REDUCTION_PHASE
                                    .get_folder_name_for_results()))) == 2

        # Test if execution works a second time
        result2: CalculationState = phase.calculate(config_manager)
        assert result2[0] == calculation_state_enum.CalculationState.RUNNING

    def test_reduction_phase_corrupted_data(self):
        # Set up paths
        project_path: Path = Path(os.path.join(TEST_DIR, "build/reduction_phase/projectXY"))
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))

        # Set up result folder from last phase
        # so delete folder from previous test runs and copy the data into it
        _prepare_previous_phase_folder(os.path.join(os.path.join(project_path, "results/"),
                                                    calculation_phase_enum.CalculationPhase.TAG_FILTER_PHASE
                                                    .get_folder_name_for_results()),
                                       os.path.join(TEST_DIR, "data/monaco_split_up_files_invalid/"),
                                       True
                                       )

        # Set up configurator
        config_manager: ConfigurationManager = _prepare_config(geojson_path, project_path, True,
                                                               cut_out_mode_enum_i.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED)

        # Execute test
        phase: ReductionPhase = reduction_phase_i.ReductionPhase()
        result1: CalculationState = phase.calculate(config_manager)

        assert result1[0] == calculation_state_enum.CalculationState.ERROR_FILE_NOT_FOUND

    def test_reduction_phase_invalid_path(self):
        # Set up paths
        project_path: Path = Path(os.path.join(TEST_DIR, "build/reduction_phdadadaase/projectXY"))
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/ada-radadadaegions.geojson"))

        # Set up result folder from last phase
        # so delete folder from previous test runs and copy the data into it
        _prepare_previous_phase_folder(os.path.join(os.path.join(project_path, "results/"),
                                                    calculation_phase_enum.CalculationPhase.TAG_FILTER_PHASE
                                                    .get_folder_name_for_results()),
                                       os.path.join(TEST_DIR, "data/monaco_split_up_files_invalid/"),
                                       True
                                       )

        # Set up configurator
        config_manager: ConfigurationManager = _prepare_config(geojson_path, project_path, False,
                                                               cut_out_mode_enum_i.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED)

        # Execute test
        phase: ReductionPhase = reduction_phase_i.ReductionPhase()
        result1: CalculationState = phase.calculate(config_manager)

        assert result1[0] == calculation_state_enum.CalculationState.ERROR_FILE_NOT_FOUND
