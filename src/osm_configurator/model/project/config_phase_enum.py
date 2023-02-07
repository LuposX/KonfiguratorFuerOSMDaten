from __future__ import annotations

from enum import Enum, unique


@unique
class ConfigPhase(Enum):
    """
    This enum stores the different phases of the configuration and is used to restores the last step the user
    was working on.
    """

    DATA_CONFIG_PHASE = "Data Configuration Phase"
    CATEGORY_CONFIG_PHASE = "Category Configuration Phase"
    REDUCTION_CONFIG_PHASE = "Reduction Configuration Phase"
    ATTRACTIVITY_CONFIG_PHASE = "Attractivity Configuration Phase"
    AGGREGATION_CONFIG_PHASE = "Aggregation Configuration Phase"
    CALCULATION_CONFIG_PHASE = "Calculation Configuration Phase"

    def get_name(self):
        """
        Getter for the name of the phase.

        Returns:
            str: Name of the Phase.
        """
        return self.value

    def equals(self, phase: str) -> ConfigPhase | None:
        for config_phase in ConfigPhase:
            if config_phase.get_name() == phase:
                return config_phase
        return None
