from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase


class GeoDataPhase(ICalculationPhase):
    """
    This Phase is responsible for three things:
    1. Converting the osm_data file into the right format
    2. Splitting the osm_data file into smaller pieces
    3. If chosen so, then removing building which are on the border
    of the traffic cell.
    For details see the method calculate().
    """

    def calculate(self, configuration_manager):
        """
        This method does three things:
        1. It splits the one big input osm_data file into multiple smaller one, there are three main reason to do that
        - Organisational, each file contains the osm elements of one previously defines traffic cell,
        this is more organized.
        - Parallelization, splitting the file into multiple smaller files allows, for better
        parallelization, since every thread/process can work with one file.
        - RAM usage, RAM capacity is limited we can't load one big file into the memory at once,
        so we need to splitt up the file.
        2. After that it converts the osm data files into files with the #
        ".pbf" osm data file format, this is done because the library we use internally used ".pbf" formats.
        3. If the option "buildings on edge are in" didn't get selected,
         it removes all building which lie on the edge/border.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): The object containing all
                                                                                 the configuration needed for execution
        Returns:
            calculation_state_enum.CalculationState: The state of the calculation, after this phase finished
                                                     it's execution or failed trying so.
        """
        pass