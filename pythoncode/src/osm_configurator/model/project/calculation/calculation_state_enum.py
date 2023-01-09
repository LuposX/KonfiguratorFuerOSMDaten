from enum import Enum, unique


@unique
class CalculationState(Enum):
    """This enum provides a list of states, the calculations can be in. 
    The states can be positive, indicating a correct working of the calculation. But they can be negative as well,
    indicating an error in the calculations. Every state is defined by a unique description of the state.
    """

    NOT_STARTED_YET = "The calculation was not started yet"
    RUNNING = "The calculations are currently running"
    ENDED_SUCCESSFULLY = "The calculations ended successfully"
    ERROR_INVALID_OSM_DATA = "Error, the osm data are not valid"
    ERROR_INVALID_CUT_OUT_DATA = "Error, the cut out data are not valid"
    ERROR_INVALID_CATEGORIES = "Error, the category configuration is not valid"
    ERROR_INVALID_PREVIOUS_CALCULATIONS = "Error, this calculation phase can not be calculated, " \
                                          "because a previous calculation has invalid results or wasn't run"

    def get_description(self):
        """Gives the description of a calculation state.

        Returns:
            str: The description, that describes the state in natural language.
        """
        return self.value
