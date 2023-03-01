from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geopandas import GeoDataFrame
    from pathlib import Path
    from typing import List
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState


class PrepareCalculationInformation:
    """
    This class purpose is to be a container of information that the various calculation classes needs, generated
    from the prepare_calculation_phase_method.
    """
    def __init__(self,
                cut_out_dataframe: GeoDataFrame = None,
                checkpoint_folder_path_last_phase: Path = None,
                checkpoint_folder_path_current_phase: Path = None,
                list_of_traffic_cell_checkpoints: List[Path] = None,
                calculation_state: CalculationState = None,
                error_message: str = None):
        """
        CalculationState is only set if there is an error.
        If there is an error the other parameters are not set

        Args:
            cut_out_dataframe: (GeoDataFrame) = None,
            checkpoint_folder_path_last_phase: (Path) = None,
            checkpoint_folder_path_current_phase: (Path) = None,
            list_of_traffic_cell_checkpoints: (List[Path]) = None,
            calculation_state: (CalculationState) = None,
            error_message: (str) = None
        """
        self._cut_out_dataframe = cut_out_dataframe
        self._checkpoint_folder_path_last_phase = checkpoint_folder_path_last_phase
        self._checkpoint_folder_path_current_phase = checkpoint_folder_path_current_phase
        self._list_of_traffic_cell_checkpoints = list_of_traffic_cell_checkpoints
        self._calculation_state = calculation_state
        self._error_message = error_message

    def get_cut_out_dataframe(self) -> GeoDataFrame | None:
        """
        Getter for the cut_out_dataframe.

        Returns:
            (GeoDataFrame | None): The cut_out dataframe.
        """
        return self._cut_out_dataframe

    def get_checkpoint_folder_path_last_phase(self) -> Path | None:
        """
        Getter for the checkpoint_folder_path_last_phase.

        Returns:
            (Path | None): The checkpoint_folder_path_last_phase.
        """
        return self._checkpoint_folder_path_last_phase

    def get_checkpoint_folder_path_current_phase(self) -> Path | None:
        """
        Getter for the checkpoint_folder_path_current_phase.

        Returns:
            (Path | None): The checkpoint_folder_path_current_phase.
        """
        return self._checkpoint_folder_path_current_phase

    def get_list_of_traffic_cell_checkpoints(self) -> List[Path] | None:
        """
        Getter for the list_of_traffic_cell_checkpoints.

        Returns:
            (List[Path] | None): The list of traffic cells.
        """
        return self._list_of_traffic_cell_checkpoints

    def get_calculation_state(self) -> CalculationState | None:
        """
        Getter for the calculation_state.

        Returns:
            (GeoDataFrame | None): The calculation state.
        """
        return self._calculation_state

    def get_error_message(self) -> str | None:
        """
        Getter for the error_message.

        Returns:
            (str | None): The error_message if it has one.
        """
        return self._error_message
