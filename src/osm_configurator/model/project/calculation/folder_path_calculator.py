from __future__ import annotations

import os

from typing import TYPE_CHECKING

import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum_i

from pathlib import Path

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.calculation_phase_enum import CalculationPhase
    from pathlib import Path


CALCULATION_PHASE_CHECKPOINT_FOLDER_NAME = "results"


class FolderPathCalculator:
    @classmethod
    def get_checkpoints_folder_path_from_phase(cls, configuration_manager_o: ConfigurationManager,
                                               phase: CalculationPhase) -> Path:
        """
        This method creates the full path which points toward the results/intermediate-step folder of a certain phase.
        It combines the path of the active_project with the result folder name and the phase result folder name.

        Args:
            configuration_manager_o (ConfigurationManager): Is used to find out the path towards the folder.
            phase (CalculationPhase): The phase from which we want to get the results/intermediate-step folder.

        Returns:
            (Path): The full path towards the desired calculation phase results folder.
        """
        if phase == calculation_phase_enum_i.CalculationPhase.NONE:
            return configuration_manager_o.get_osm_data_configuration().get_osm_data()

        # Get the path to the project path and the name of the folder where we save the results and add them together
        project_path: Path = configuration_manager_o.get_active_project_path()

        result_folder_name: str = CALCULATION_PHASE_CHECKPOINT_FOLDER_NAME
        phase_folder_name: str = phase.get_folder_name_for_results()

        checkpoint_folder_path: Path = Path(
            os.path.join(os.path.join(project_path, result_folder_name), phase_folder_name))

        return Path(checkpoint_folder_path)
