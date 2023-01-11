from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
import src.osm_configurator.model.project.configuration.configuration_manager
import src.osm_configurator.model.project.calculation.calculation_state_enum

class AttractivityPhase(ICalculationPhase):
    """This calculation phase is responsible for calculating the attractivity attributes of the OSM-elements.
    For details see the method calculate().
    """
    def calculate(self, configuration_manager):
        """Calculates the attractivity attributes of the osm-elements
        The calculation phase reads the data of the previous calculation phase. Now it calculates the attractivity attributes of every OSM-element. The attractivity attributes that are calculated for a osm-element are dependent on the category, this element is in. The value of an attractivity attribute is computed as a linear function with the previously computed attributes. The factors of this linear function are given in the configuration of the category. After the calculations are done, the results are stored on the harddrive.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): The object containing all the configuration needed for execution

        Returns:
            calculation_state_enum.CalculationState: The state of the calculation, after this phase finished it's execution or failed trying so.
        """
        pass