from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
import src.osm_configurator.model.project.configuration.configuration_manager
import src.osm_configurator.model.project.calculation.calculation_state_enum


class AggregationPhase(ICalculationPhase):
    """
    This calculation phase is responsible for aggregating the attractivity attributes in the given traffic cells.
    For details see the method calculate().
    """

    def calculate(self, configuration_manager):
        """
        Aggregates the attractivity attributes in the given traffic cells.
        The calculation phase reads the data of the previous calculation phase. Now for every traffic cell all selected
        aggregation methods are performed for all attractivity attributes. For details on the different aggregation
        methods, see AggregationMethod.
        After the calculations are done, the results are stored on the hard-drive.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): The object containing all the configuration needed for execution.

        Returns:
            calculation_state_enum.CalculationState: The state of the calculation, after this phase finished its execution or failed trying so.
        """
        pass
