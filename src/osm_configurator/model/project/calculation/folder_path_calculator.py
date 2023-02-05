from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from pathlib import Path


CALCULATION_PHASE_CHECKPOINT_FOLDER_NAME = "results"


class FolderPathCalculator:
    def get_checkpoints_folder_path_from_phase(self, configuration_manager_o: ConfigurationManager, phase: CalculationPhase) -> Path:
        """
        This method creates the full path which points toward the results/intermediate-step folder of a certain phase.
        It combines the path of the active_project with the result folder name and the phase result folder name.

        Args:
            configuration_manager_o (ConfigurationManager): Is used to find out the path towards the folder.
            phase (CalculationPhase): The phase from which we want to get the results/intermediate-step folder.

        Returns:
            (Path): The full path towards the desired calculation phase results folder.
        """
        # Get the path to the project path and the name of the folder where we save the results and add them together
        project_path: Path = configuration_manager_o.get_active_project_path()

        result_folder_name: str = CALCULATION_PHASE_CHECKPOINT_FOLDER_NAME
        phase_folder_name: str = phase.get_folder_name_for_results()

        checkpoint_folder_path: Path = project_path.joinpath(result_folder_name).joinpath(phase_folder_name)

        return checkpoint_folder_path
