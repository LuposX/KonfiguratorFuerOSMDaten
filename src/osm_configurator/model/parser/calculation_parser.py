from __future__ import annotations

from src.osm_configurator.model.parser.calculation_parser_interface import CalculationParserInterface


class CalculationParser(CalculationParserInterface):
    __doc__ = CalculationParserInterface.__doc__

    def __init__(self):
        """
        Creates a new instance of the calculation_parser_interface.CalculationParser.
        """
        pass
    
    def check_validity_of_calculation_step(self, project_path, starting_point):
        pass 
    
    