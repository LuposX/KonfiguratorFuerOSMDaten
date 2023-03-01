from __future__ import annotations

from enum import Enum, unique


@unique
class CalculationState(Enum):
    """
    This enum provides a list of states the calculations can be in.
    The states can be positive, indicating the calculation is working correctly. But they can be negative as well,
    indicating an error in the calculation. Every state is defined by a unique description of the state.

    The first value is the name the second value is the description of the state.
    """

    NOT_STARTED_YET = ("Not started yet", "The calculation was not started yet.")
    RUNNING = ("Running", "The calculations are currently running.")
    CANCELED = ("Canceled", "The calculations was canceled")
    ENDED_SUCCESSFULLY = ("Done", "The calculations ended successfully.")
    ERROR_INVALID_OSM_DATA = ("Invalid OSM Data", "Error: The osm data are not valid.")
    ERROR_INVALID_CUT_OUT_DATA = ("Invalid Cut Out Data", "Error: The cut out data are not valid.")
    ERROR_INVALID_CATEGORIES = ("Invalid Categories", "Error: The category configuration is not valid.")
    ERROR_INVALID_PREVIOUS_CALCULATIONS = ("Invalid calculation phase", "Error: This calculation phase can not be calculated, because a previous calculation has invalid results or wasn't run.")
    ERROR_PROJECT_NOT_SET_UP_CORRECTLY = ("Project did not got set up Correctly", "Error: The project folder structure did not get set up correctly.")
    ERROR_TAGS_WRONGLY_FORMATTED = ("Tags wrongly formatted", "Error: while trying to parse your tags, the tags are not correctly formatted.")
    ERROR_COULDNT_OPEN_FILE = ("Couldn't open a file", "ERROR: While trying to open a file, do you have permission?")
    ERROR_ENCODING_THE_FILE = ("Encoding error", "ERROR: While writing to the file there was an encoding error.")
    ERROR_FILE_NOT_FOUND = ("File not found", "ERROR: While trying to open the file couldn't find the file.")

    def get_name(self) -> str:
        """
        Gives back the name of a calculation state.

        Returns:
            str: The name of the calculation state.
        """
        return self.value[0]

    def get_description(self) -> str:
        """
        Gives back the description of a calculation state.

        Returns:
            str: The description, that describes the state in natural language.
        """
        return self.value[1]