from __future__ import annotations

import src.osm_configurator.model.project.calculation.calculation_phase_enum as cpe
import src.osm_configurator.model.project.calculation.folder_path_calculator as folder_path_calculator_i
import src.osm_configurator.model.project.configuration.configuration_manager as configuration_manager
from pathlib import Path
import os
import pytest
from src_tests.definitions import TEST_DIR

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase


@pytest.mark.parametrize("phase", [
    cpe.CalculationPhase.NONE,
    cpe.CalculationPhase.GEO_DATA_PHASE,
    cpe.CalculationPhase.TAG_FILTER_PHASE,
    cpe.CalculationPhase.REDUCTION_PHASE,
    cpe.CalculationPhase.ATTRACTIVITY_PHASE,
    cpe.CalculationPhase.AGGREGATION_PHASE
])
def test_valid_path_generation(phase: CalculationPhase):
    project_path: Path = Path(os.path.join(TEST_DIR, "build/calculation_phase_utility/ProjectX"))
    config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project_path)

    folder_path_calculator_o = folder_path_calculator_i.FolderPathCalculator()

    result: Path = folder_path_calculator_o.get_checkpoints_folder_path_from_phase(config_manager, phase)

    # The method must decide what's the name of the folder on it's own, the tests do not specify it.
    assert result is not None
