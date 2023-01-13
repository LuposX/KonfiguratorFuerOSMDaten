import pathlib
from abc import abstractmethod, ABC
import src.osm_configurator.model.project.calculation.calculation_phase_enum


class CalculationParserInterface(ABC):
    """
    The CalculationParser job is to parse the calculation files, that are created from the calculation process.
    It ensures that all data required for a calculation step is there.
        
    Examples: The :obj:`~tag_filter_phase.TagFilterPhase` needs the
    files that got previously calculated in :obj:`~geo_data_phase.GeoDataPhase`.
    """

    @abstractmethod
    def check_validity_of_calculation_step(self, project_path, starting_point):
        """
        Checks whether the passed starting_point is valid.
        A starting_point is valid when all calculation files required for the next step are present in the project.
        
        Args:
            project_path (pathlib.Path): The path pointing towards the project, that needs to be validated.
            starting_point (calculation_phase_enum.CalculationPhase): The step we want to calculate next.

        Returns:
            bool: True when starting_point is valid, otherwise false.
        """
        pass
