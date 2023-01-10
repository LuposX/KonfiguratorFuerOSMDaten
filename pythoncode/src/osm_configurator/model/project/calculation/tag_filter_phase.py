from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase
import src.osm_configurator.model.project.configuration.configuration_manager
import src.osm_configurator.model.project.calculation.calculation_state_enum

class TagFilterPhase(ICalculationPhase):
    """This calculation phase is responsible for sorting OSM-elements into their corresponding categories. 
    For details see the method calculate().
    """
    def calculate(self, configuration_manager):
        """Sorts OSM-elements into their corresponding categories.
        Firstly, this method reads in the OSM-files of the previously executed calculation phase. Every category has defined a tag filter in the configuration phase. The OSM-Elements are now sorted into the categories, depending on whether they do pass or not pass the corresponding tag filters. A tag filter is defined by a black- and a whitelist. Each list is a collection of constraints of the tags of the osm-elements. A osm-element passes a tag filter, if all constraints of the whitelist are satisfied and no entry of the blacklist is satisfied.
        After execution the results shall be stored again on the harddrive.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): The object containing all the configuration needed for execution

        Returns:
            calculation_state_enum.CalculationState: The state of the calculation, after this phase finished it's execution or failed trying so.
        """
        pass