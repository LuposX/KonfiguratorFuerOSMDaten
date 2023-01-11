from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
import src.osm_configurator.model.project.configuration.configuration_manager
import src.osm_configurator.model.project.calculation.calculation_state_enum


class ReductionPhase(ICalculationPhase):
    """
    This calculation phase is responsible for reducing bigger OSM-elements on single coordinates and for generating
    the values of the attributes for alle OSM-elements.
    For details see the method calculate().
    """
    def calculate(self, configuration_manager):
        """
        Reduces OSM-elements on single points and calculates their attributes.
        The calculation phase reads the data of the previous calculation phase. OSM-elements that are not just a single
        node, must be reduced on one coordinate. For that the centre of the given shape is calculated and set as the
        new coordinate. This calculation phase does also calculate the attributes of every OSM-element. There is no
        generic form for calculation attributes, every attribute has an individual calculation. If a method of
        calculation is not possible or if the user turned it off, the value of the attributes is defined by the
        default value list of the category. The value is given by the highest priority entry of the default value
        list, that matches the osm-element. After the calculations are done, the results are stored on the hard-drive.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): The object containing all the configuration required for an execution.

        Returns:
            calculation_state_enum.CalculationState: The state of the calculation after this phase finished its execution or failed trying so.
        """
        pass
