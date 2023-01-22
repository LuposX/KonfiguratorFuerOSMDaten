from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from pathlib import Path


def get_checkpoints_folder_path_from_phase(configuration_manager_o: ConfigurationManager, phase: CalculationPhase):
    # Get the path to the project path and the name of the folder where we save the results and add them together
    project_path: Path = configuration_manager_o.get_active_project_path()

    result_folder_name: str = configuration_manager_o.get_calculation_phase_checkpoints_folder_name()
    phase_folder_name: str = phase.get_folder_name_for_results()

    checkpoint_folder_path: Path = project_path.joinpath(result_folder_name).joinpath(phase_folder_name)

    return checkpoint_folder_path
