from enum import Enum, unique
import src.osm_configurator.model.parser.calculation_parser_interface


@unique
class CalculationPhase(Enum):
    """
    This enum provides a list of phases the calculation can be in.
    These phases will be worked through in order like a pipeline.
    An enum consists of two values a name which will be displayed and an order in which the phases will be calculated,
    also used to know in which order to display the phases.
    If you want to know more about the calculation phases refer to the "Pflichtenheft",
    or the documentation of the individual phases in `project.calculation`
    """

    NONE = ("None", 0)  #: When we are currently not in a calculation phase.
    GEO_DATA_PHASE = ("Data Input and Geo-Filter", 1)  #: When we are currently in the GeoDataPhase
    TAG_FILTER_PHASE = ("Tag-filter", 2)   #: When we are currently in the TagFilterPhase
    REDUCTION_PHASE = ("Reduction", 3)   #: When we are currently in the ReductionPhase
    ATTRACTIVITY_PHASE = ("Attractivity", 4)   #: When we are currently in the AttractivityPhase
    AGGREGATION_PHASE = ("Aggregation", 5)   #: When we are currently in the AggregationPhase

    def get_name(self):
        """
        Getter for the name of the enum type.

        Returns:
            (str): Name of the Phase.
        """
        return self.value[0]

    def get_order(self):
        """
        Getter for the order of the enum type.

        Returns:
            (int): order of the enum.
        """
        return self.value[1]
