from __future__ import annotations

from src.osm_configurator.model.project.calculation.calculation_phase_interface import ICalculationPhase


class GeoDataPhase(ICalculationPhase):
    """
    This Phase is responsible for three things:
    1. Converting the osm_data file into the right format.
    2. Splitting the osm_data file into smaller pieces.
    3. If selected, removing building which are on the border of the traffic cell.
    For details see the method calculate().
    """

    def calculate(self, configuration_manager):
        """
        This method does three things:
        1. It splits the big input osm_data file into multiple smaller one. There are three main reason to do that
        - Organisational: Each file contains the osm elements of one previously defined traffic cell.
        This is more organized.
        - Parallelization: Splitting the file into multiple smaller files allows, for better
        parallelization, since every thread/process can work with one file.
        - RAM usage: RAM capacity is limited. We can't load one big file into the memory at once,
        so we need to split up the file.
        2. After that it converts the osm data files into files with the ".pbf" osm data file format, which is done
        since the library we use internally uses ".pbf" formats.
        3. If the option "buildings on edge are in" didn't get selected.
        It removes all buildings which are on the edge/border.

        Args:
            configuration_manager (configuration_manager.ConfigurationManager): The object containing all the configuration needed for an execution.
        Returns:
            calculation_state_enum.CalculationState: The state of the calculation after this phase finished its execution or failed trying so.
        """
        pass
