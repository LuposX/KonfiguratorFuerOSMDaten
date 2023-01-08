from abc import ABC, abstractmethod
from pathlib import Path
from src.osm_configurator.model.project.calculation.calculation_phase import CalculationPhase


class CalculationParserInterface(ABC):
    """
    The CalculationParser job, is to parse the calculation files 
    that are created from the calculation process.
    It needs to make sure that all data that is needed for a calculation step is there.
        
    Examples:
        The :obj:`~src.osm_configurator.model.project.calculation.tag_filter_phase.TagFilterPhase` needs the files that got previously calculated in
        :obj:`~src.osm_configurator.model.project.calculation.geo_data_phase.GeoDataPhase`.
    """
    
    @abstractmethod
    def check_validity_of_calculation_step(self, project_path, starting_point):
        """
        Checks whether the passed starting_point is valid.
        A starting_point is valid when all calculation files needed for the next step are presen in the project.
        
        Args:
            project_path (pathlib.Path): The path pointing towards the project, that needs to be validated.
            starting_point (CalculationPhase): The Step which we want to calculate next.

        Returns:
            bool: true when starting_point is valid, otherwise false.
        """
        pass
