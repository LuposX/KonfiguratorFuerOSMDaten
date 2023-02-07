from __future__ import annotations

from enum import Enum, unique


@unique
class CutOutMode(Enum):
    """
    The job of this enum is to store the different cut-out-modes used in the reduction during the calculation.
    We differentiate on, if we should include building which are on the edge/border, this mean partially inside
    the traffic cell, or not.
    """
    BUILDINGS_ON_EDGE_ACCEPTED = "Buildings on edge are accepted"
    BUILDINGS_ON_EDGE_NOT_ACCEPTED = "Building on the edge are not accepted"

    def get_name(self):
        """
        Getter for the name of the enum type.

        Returns:
            str: the name of the enum
        """
        return self.value

    def equals(self, mode: str) -> CutOutMode | None:
        for cut_out_mode in CutOutMode:
            if cut_out_mode.get_name() == mode:
                return cut_out_mode
        return None
