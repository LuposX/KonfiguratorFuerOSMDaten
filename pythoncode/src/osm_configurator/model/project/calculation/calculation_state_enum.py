from enum import Enum, unique


@unique
class CalculationState(Enum):
    """
    This enum provides a list of states the calculations can be in.
    The states can be positive, indicating the calculation is working correctly. But they can be negative as well,
    indicating an error in the calculation. Every state is defined by a unique description of the state.
    """

    NOT_STARTED_YET = ("Not started yet", "The calculation was not started yet.")
    RUNNING = ("Running", "The calculations are currently running.")
    ENDED_SUCCESSFULLY = ("Done", "The calculations ended successfully.")
    ERROR_INVALID_OSM_DATA = ("Invalid OSM Data", "Error: The osm data are not valid.")
    ERROR_INVALID_CUT_OUT_DATA = ("Invalid Cut Out Data", "Error: The cut out data are not valid.")
    ERROR_INVALID_CATEGORIES = ("Invalid Categories", "Error: The category configuration is not valid.")
    ERROR_INVALID_PREVIOUS_CALCULATIONS = ("Invalid calculation phase", "Error: This calculation phase can not be calculated, because a previous calculation has invalid results or wasn't run.")
    ERROR_PROJECT_NOT_SET_UP_CORRECTLY = ("Project did not got set up Correctly", "Error: The project folder structure did not get set up correctly.")

    def get_name(self):
        """
        Gives back the name of a calculation state.

        Returns:
            str: The name of the calculation state.
        """
        return self.value[0]

    def get_description(self):
        """
        Gives back the description of a calculation state.

        Returns:
            str: The description, that describes the state in natural language.
        """
        return self.value[1]