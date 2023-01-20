from enum import Enum, unique


@unique
class CalculationPhase(Enum):
    """
    This enum provides a list of phases the calculation can be in.
    These phases will be worked through in order like a pipeline.
    An enum consists of two values a name which will be displayed and an order in which the phases will be calculated,
    also used to know in which order to display the phases.
    If you want to know more about the calculation phases refer to the "Pflichtenheft",
    or the documentation of the individual phases in `project.calculation`

    Each enum consists of three variables: (name, folder_name, order).
    The name of the phase is used in the GUI, to display the correct name of the phase.
    The folder_name is used to save the results of each phase in it.
    The order is used to differentiate in which order the phases get called.
    """

    NONE = ("None", "none", 0)
    GEO_DATA_PHASE = ("Data Input and Geo-Filter", "geo_data_phase_results", 1)
    TAG_FILTER_PHASE = ("Tag-filter", "tag_filter_phase", 2)
    REDUCTION_PHASE = ("Reduction", "reduction_phase_results", 3)
    ATTRACTIVITY_PHASE = ("Attractivity", "attractivity_phase_results", 4)
    AGGREGATION_PHASE = ("Aggregation", "aggregation_phase_result", 5)

    def get_name(self):
        """
        Getter for the name of the enum type.

        Returns:
            str: Name of the Phase.
        """
        return self.value[0]

    def get_folder_name_for_results(self) -> str:
        """
        Getter for the folder name of the enum type.

        Returns:
            str: The folder name of the enum.
        """
        return self.value[1]

    def get_order(self):
        """
        Getter for the order of the enum type.

        Returns:
            int: order of the enum.
        """
        return self.value[2]
