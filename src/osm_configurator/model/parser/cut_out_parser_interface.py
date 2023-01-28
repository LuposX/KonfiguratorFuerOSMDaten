from __future__ import annotations
from typing import TYPE_CHECKING

from pathlib import Path

from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from geopandas import GeoDataFrame


class CutOutParserInterface(ABC):
    """
    This Class parses cut_out files to an internal representation of the cut_out_file.
    """
    
    @abstractmethod
    def parse_cutout_file(self, path: Path) -> GeoDataFrame:
        """
        This method takes in the path to a cut_out file and parses to an
        internal representation of TrafficCells. (DataFrames)
        
        A cut_out file is a `.geojson` file that consists of multiple TrafficCells. Each TrafficCell has
        a name and a polygon, which is the bounding box of the Traffic Cell.
        
        Args:
            path (pathlib.Path):  The path pointing towards cut_out file we want to parse.
        
        Returns:
           DataFrame: Our cut_out file transformed into a DataFrame, None if an error occurs
            
        Examples:
            To see an example for a cut_out file check out the file `data/partOfKarlsruhe.geojson`.
        """
        pass