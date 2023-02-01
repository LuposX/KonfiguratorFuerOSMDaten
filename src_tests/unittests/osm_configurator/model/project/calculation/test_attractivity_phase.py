from __future__ import annotations

from typing import TYPE_CHECKING

from pathlib import Path
import os
import shutil

from src_tests.definitions import TEST_DIR
import src_tests.definitions as definitions

import src.osm_configurator.model.project.calculation.attractivity_phase as attractivity_phase
import src.osm_configurator.model.project.calculation.calculation_phase_utility as calculation_utility
import src.osm_configurator.model.project.configuration.configuration_manager as configuration_manager
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.attractivity_phase import AttractivityPhase


def _prepare_config(project: Path, geojson: Path) -> ConfigurationManager:
    config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project)
    config_manager.get_cut_out_configuration().set_cut_out_path(geojson)
    return config_manager


def test_minimal_input_successfully():
    # Prepare configuration manager
    geojson_path: Path = Path(os.path.join(TEST_DIR, "data/attractivity_phase/minimal/cells.geojson"))
    project_path: Path = Path(os.path.join(TEST_DIR, "build/attractivity_phase/projectMinimal"))
    config_manager: ConfigurationManager = _prepare_config(project_path, geojson_path)

    # Prepare categories and attractivities
    cat_manager: CategoryManager = config_manager.get_category_manager()
    cat_manager.get_categories().append(definitions.TEST_CATEGORY_BUILDING)
    cat_manager.get_categories().append(definitions.TEST_CATEGORY_SHOP)

    # Copy results of reduction phase
    copy_from: Path = Path(os.path.join(TEST_DIR, "data/attractivity_phase/minimal/0_traffic_cell.csv"))
    input_folder: Path = calculation_utility.get_checkpoints_folder_path_from_phase\
        (config_manager, calculation_phase_enum.CalculationPhase.REDUCTION_PHASE)
    copy_to: Path = Path(os.path.join(input_folder, "0_traffic_cell.csv"))
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
    if os.path.exists(copy_to):
        os.remove(copy_to)
    shutil.copyfile(copy_from, copy_to)

    # Execute attractivity phase
    phase: AttractivityPhase = attractivity_phase.AttractivityPhase()
    result: CalculationState = phase.calculate(config_manager)[0]
    assert result == calculation_state_enum.CalculationState.RUNNING

    # TODO: Test the correctness of the output
