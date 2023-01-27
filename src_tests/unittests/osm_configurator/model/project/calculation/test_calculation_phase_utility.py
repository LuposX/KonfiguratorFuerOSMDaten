import src.osm_configurator.model.project.calculation.calculation_phase_utility as calculation_phase_utility
from pathlib import Path
import os
from src_tests.definitions import TEST_DIR


def test_valid_path_generation():
    project_path: Path = Path(os.path.join(TEST_DIR, "build/calculation_phase_utility/ProjectX"))
