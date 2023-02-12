from __future__ import annotations
import pytest

import src.osm_configurator.model.project.calculation.calculation_manager as calculation_manager
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.configuration.configuration_manager as configuration_manager
from pathlib import Path
import os
from src_tests.definitions import TEST_DIR
import time

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_manager import CalculationManager
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase


def test_correct_state_passing_on_error():
    project_path: Path = Path(os.path.join(TEST_DIR, "build/calculation_manager/project1"))
    config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project_path)

    calc_manager: CalculationManager = calculation_manager.CalculationManager(config_manager)

    # Test if calculation tries to start
    result: CalculationState = calc_manager.start_calculation(calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE)[0]
    assert result == calculation_state_enum.CalculationState.RUNNING

    # Test if calculation fails
    time.sleep(3)
    new_state: CalculationState = calc_manager.get_calculation_state()[0]
    assert new_state != calculation_state_enum.CalculationState.RUNNING
    assert new_state != calculation_state_enum.CalculationState.ENDED_SUCCESSFULLY


@pytest.mark.parametrize("phase", [
    calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE,
    calculation_phase_enum.CalculationPhase.TAG_FILTER_PHASE,
    calculation_phase_enum.CalculationPhase.REDUCTION_PHASE,
    calculation_phase_enum.CalculationPhase.ATTRACTIVITY_PHASE,
    calculation_phase_enum.CalculationPhase.AGGREGATION_PHASE
])
def test_cancel_calculations(phase: CalculationPhase):
    # Start calculations in every phase and cancels them immediately
    project_path: Path = Path(os.path.join(TEST_DIR, "build/calculation_manager/project2"))
    config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project_path)

    calc_manager: CalculationManager = calculation_manager.CalculationManager(config_manager)

    # Start calculations
    result: CalculationState = calc_manager.start_calculation(phase)[0]
    assert result == calculation_state_enum.CalculationState.RUNNING

    # Cancel calculation
    succ: bool = calc_manager.cancel_calculation()
    assert succ

    assert calc_manager.get_calculation_state()[0] == calculation_state_enum.CalculationState.CANCELED


def test_illegal_cancel1():
    # Cancels the calculation before it even started
    project_path: Path = Path(os.path.join(TEST_DIR, "build/calculation_manager/project3"))
    config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project_path)

    calc_manager: CalculationManager = calculation_manager.CalculationManager(config_manager)

    assert not calc_manager.cancel_calculation()


def test_illegal_cancel2():
    # Cancels the calculation after it was already canceled
    project_path: Path = Path(os.path.join(TEST_DIR, "build/calculation_manager/project4"))
    config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project_path)

    calc_manager: CalculationManager = calculation_manager.CalculationManager(config_manager)
    calc_manager.start_calculation(calculation_phase_enum.CalculationPhase.GEO_DATA_PHASE)

    assert calc_manager.cancel_calculation()
    time.sleep(1)
    assert not calc_manager.cancel_calculation()
