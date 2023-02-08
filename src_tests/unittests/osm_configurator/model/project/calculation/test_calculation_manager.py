from __future__ import annotations

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
