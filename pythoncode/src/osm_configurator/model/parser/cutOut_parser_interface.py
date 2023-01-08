from abc import ABC, abstractmethod
from pathlib import Path
from src.osm_configurator.model.project.calculation.traffic_cell import TrafficCell


class CutOutParserInterface(ABC):
    """This Class parses cut_out files to an internal Representation of the  cut_out_file
    """
    
    @abstractmethod
    def parse_cutout_file(self, path):
        """
        This method takes in the path to a cut_out file and parses to a 
        internal representation of Traffic Cells.
        
        A cut_out file is a `.geojson` file that consists of multiple TrafficCells each TrafficCell has 
        a name and a polygon which is the bounding box of the Traffic Cell.
        
        Args:
            path (pathlib.Path):  The path pointing towards cut_out file we want to parse.
        
        Returns:
           list(TrafficCell): Our cut_out file transformed into a list of TrafficCells.
            
        Examples:
            To see an example for a cut_out file check out the file `data/partOfKarlsruhe.geojson`.
        """
        pass

