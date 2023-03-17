from __future__ import annotations

import os
from pathlib import Path
import src.osm_configurator.model.project.configuration.cut_out_mode_enum as cut_out_mode_enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode


class CutOutConfiguration:
    """
    This class job is to store the cut-out mode and the cut-out file path. Both are required during the reduction-phase
    in the calculation.
    """

    def __init__(self):
        """
        Creates a new instance of the "CutOutConfiguration" class.
        """
        self._cut_out_mode: CutOutMode = cut_out_mode_enum.CutOutMode.BUILDINGS_ON_EDGE_ACCEPTED
        self._cut_out_path: Path | None = None

    def get_cut_out_mode(self) -> CutOutMode:
        """
        Gives back the used cut-out mode.

        Returns:
            cut_out_mode_enum.CutOutMode: The used cut-out mode.
        """
        return self._cut_out_mode

    def set_cut_out_mode(self, new_cut_out_mode: CutOutMode) -> bool:
        """
        Changes the cut-out mode used during the reduction phase in the calculation.

        Args:
            new_cut_out_mode (cut_out_mode_enum.CutOutMode): The new cut-out mode for the calculation.

        Returns:
            bool: True if changing the cut-out mode, otherwise false.
        """
        if new_cut_out_mode in cut_out_mode_enum.CutOutMode:
            self._cut_out_mode = new_cut_out_mode
            return True
        return False

    def get_cut_out_path(self) -> Path:
        """
        Gives back the path pointing towards the cut-out file.

        Returns:
            Path: The path pointing towards the cut-out.
        """
        return self._cut_out_path

    def set_cut_out_path(self, new_path: Path) -> bool:
        """
        Changes the path pointing towards the cut-out file.

        Args:
            new_path (Path): The new path.

        Returns:
            bool: True if changing the path, otherwise false.
        """
        if os.path.exists(new_path):
            self._cut_out_path = new_path
            return True
        return False
