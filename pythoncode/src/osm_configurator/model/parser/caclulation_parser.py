from src.osm_configurator.model.parser.calculation_parser_interface import CalculationParserInterface

class CalculationParser(CalculationParserInterface):
    # to inherit the documentation
    __doc__ = CalculationParserInterface.__doc__
    
    def __init__(self): 
        pass
    
    def check_validity_of_calculation_step(self, project_path, starting_point):
        pass 
    
    