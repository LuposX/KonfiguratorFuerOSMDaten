from __future__ import annotations

from typing import TYPE_CHECKING

from pathlib import Path
import os
import shutil
import pandas
import math

from src_tests.definitions import TEST_DIR
from src_tests.definitions import APPLICATION_MANAGER
from src_tests.definitions import APPLICATION_MANAGER2
import src_tests.definitions as definitions

import src.osm_configurator.model.project.calculation.attractivity_phase as attractivity_phase
import src.osm_configurator.model.project.calculation.folder_path_calculator as folder_path_calculator
import src.osm_configurator.model.project.configuration.configuration_manager as configuration_manager
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion
import src.osm_configurator.model.application.application_settings_default_enum as application_settings_enum


if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.attractivity_phase import AttractivityPhase
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion
    from pandas import DataFrame


def _prepare_config(project: Path, geojson: Path) -> ConfigurationManager:
    config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project)
    config_manager.get_cut_out_configuration().set_cut_out_path(geojson)

    # Prepare categories and attractivities
    cat_manager: CategoryManager = config_manager.get_category_manager()
    cat_manager.get_categories().append(definitions.TEST_CATEGORY_BUILDING_AREA)
    cat_manager.get_categories().append(definitions.TEST_CATEGORY_SITE_AREA)
    cat_manager.get_categories().append(definitions.TEST_CATEGORY_NO_BUILDING)
    cat_manager.get_categories().append(definitions.TEST_CATEGORY_SHOP)

    return config_manager


def test_minimal_input_successfully():
    # Prepare configuration manager
    geojson_path: Path = Path(os.path.join(TEST_DIR, "data/attractivity_phase/minimal/cells.geojson"))
    project_path: Path = Path(os.path.join(TEST_DIR, "build/attractivity_phase/projectMinimal"))
    config_manager: ConfigurationManager = _prepare_config(project_path, geojson_path)

    # Copy results of reduction phase
    copy_from: Path = Path(os.path.join(TEST_DIR, "data/attractivity_phase/minimal/0_traffic_cell.csv"))
    input_folder: Path = folder_path_calculator.FolderPathCalculator().get_checkpoints_folder_path_from_phase\
        (config_manager, calculation_phase_enum.CalculationPhase.REDUCTION_PHASE)
    copy_to: Path = Path(os.path.join(input_folder, "0_traffic_cell.csv"))
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
    if os.path.exists(copy_to):
        os.remove(copy_to)
    shutil.copyfile(copy_from, copy_to)

    # Execute attractivity phase
    phase: AttractivityPhase = attractivity_phase.AttractivityPhase()
    result: CalculationState = phase.calculate(config_manager, APPLICATION_MANAGER2)[0]
    assert result == calculation_state_enum.CalculationState.RUNNING

    # Check whether calculation has correct results
    result_path: Path = Path(os.path.join(folder_path_calculator.FolderPathCalculator().get_checkpoints_folder_path_from_phase
                                          (config_manager, calculation_phase_enum.CalculationPhase.ATTRACTIVITY_PHASE),
                                          "0_traffic_cell.csv"))
    df: DataFrame = pandas.read_csv(result_path)
    assert df["coolness"][0] == 210
    assert df["coolness"][1] == 907
    assert df["coolness"][4] == 2001

    assert df["trading"][0] == 810
    assert math.isnan(df["trading"][3])
    assert df["trading"][5] == 42


def test_temp_test():
    assert APPLICATION_MANAGER2.get_setting(application_settings_enum.ApplicationSettingsDefault.NUMBER_OF_PROCESSES) == 4


def test_illegal_configuration():
    config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(
        Path(os.path.join(TEST_DIR, "build/attractivity_phase/projectIllegal")))
    phase: AttractivityPhase = attractivity_phase.AttractivityPhase()
    result: CalculationState = phase.calculate(config_manager, APPLICATION_MANAGER2)[0]
    assert result == calculation_state_enum.CalculationState.ERROR_INVALID_CUT_OUT_DATA


def test_big_input_successfully():
    # Prepare configuration manager
    geojson_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
    project_path: Path = Path(os.path.join(TEST_DIR, "build/attractivity_phase/projectBig"))
    config_manager: ConfigurationManager = _prepare_config(project_path, geojson_path)

    # Reset and Copy results of reduction phase
    copy_from: Path = Path(os.path.join(TEST_DIR, "data/attractivity_phase/big"))
    copy_to: Path = folder_path_calculator.FolderPathCalculator().get_checkpoints_folder_path_from_phase \
        (config_manager, calculation_phase_enum.CalculationPhase.REDUCTION_PHASE)

    deleter: FileDeletion = file_deletion.FileDeletion()
    deleter.reset_folder(copy_to)

    for file_name in os.listdir(copy_from):
        shutil.copy2(os.path.join(copy_from, file_name), copy_to)

    # Execute attractivity phase
    phase: AttractivityPhase = attractivity_phase.AttractivityPhase()
    result: CalculationState = phase.calculate(config_manager, APPLICATION_MANAGER2)[0]
    assert result == calculation_state_enum.CalculationState.RUNNING

    # Do further testing
    result_path: Path = Path(os.path.join(folder_path_calculator.FolderPathCalculator().get_checkpoints_folder_path_from_phase
                                          (config_manager, calculation_phase_enum.CalculationPhase.ATTRACTIVITY_PHASE),
                                          "6_traffic_cell.csv"))
    df: DataFrame = pandas.read_csv(result_path)

    assert df["trading"][100] == 42
    assert math.isnan(df["coolness"][100])
