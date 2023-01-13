import src.osm_configurator.model.application.application_interface
import src.osm_configurator.model.project.calculation.calculation_state_enum
import src.osm_configurator.model.project.calculation.calculation_phase_enum


class CalculationController:
    """
    The CalculationController is responsible for forwarding requests to the model, regarding calculations.
    It may be used to gather information and to control the calculation-process of the currently selected project.
    """

    def __init__(self, model):
        """
        Creates a new instance of the CalculationController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def start_calculations(self, starting_phase):
        """
        Starts the calculations in the given calculation phase in the currently selected project.
        The calculation process is split in different calculation phases. This function starts the calculation in a given phase.

        Args:
            starting_phase (calculation_phase_enum.CalculationPhase): The phase in which the calculation should start.

        Returns:
            calculation_state_enum.CalculationState: The status of the calculation: RUNNING, if the calculation was started successfully. For details on the meaning of this return value, see CalculationState.
        """
        pass

    def get_calculation_state(self):
        """
        Gives the current calculation state of the selected project.

        Returns:
            calculation_state_enum.CalculationState: Returns the current state of the calculation. For details see documentation of CalculationState.
        """
        pass

    def get_current_calculation_phase(self):
        """
        Returns the calculation phase of the currently selected project.

        Returns:
            calculation_phase_enum.CalculationPhase: The phase that is currently running. NONE, if no phase is currently running.
        """
        pass

    def get_current_calculation_process(self):
        """
        Returns an approximation of the progress of the calculations in the currently selected project.
        The progress is given as a number between 0 and 1, where 0 indicates that the calculation has not started yet and 1 indicates, that the calculations are done.

        Returns:
            float: The value of the approximation.
        """
        pass

    def cancel_calculations(self):
        """
        Cancels the calculations of the currently selected project.
        The calculation phase that is currently running will be stopped.

        Returns:
            bool: True, if the calculation was canceled successfully; False, otherwise.
        """
        pass
