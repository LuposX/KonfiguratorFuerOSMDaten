from ConfiguratorOSMData.model import CalculationPhase
from ConfiguratorOSMData.model import ConfigurationManager


class CalculationManager:
    """
    The CalculationManager manages Calculation of the Project.
    """

    def __init__(self, starting_point: CalculationPhase, configuration_manager: ConfigurationManager):
        """
        Gets called when we first create an object of this class, it saves all information it needs for
        starting a calculation.

        Args:
            starting_point: Describes in which calculation-phase we want to start the calculation.
            configuration_manager: Saves all information required to configure the calculation.
        """
        pass

    def cancel_calculation(self):
        """
        This method is used when we want to cancel an ongoing calculation.
        """
        pass

    def _validate_starting_point(self) -> bool:
        """
        Validates the correctness of the Staring Point.

        Returns:
            bool: If true then the starting_point is valid, this means every calculation up to this point exist
            and are saved in the project.
        """
        pass

    def _start_calculation(self):
        """
        Starts the calculation.
        """
        pass
