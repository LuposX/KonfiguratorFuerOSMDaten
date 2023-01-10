import shapely
import pathlib

class SplitUpFile:
    """
    This class responsible to split up osm-data files, into multiple smaller osm-data files.
    This is useful, since an osm-data file loaded into the ram can be bigger than the capacity of the RAM.
    """

    def __init__(self, file_path):
        """
        Creates a new instance of "SplitUpFile".

        Args:
            file_path (pathlib.Path): the path to the osm_data file we want to split
        """
        pass

    def split_up_files(self, coordinates):
        """
        This method splits up the file into multiple smaller ones based on the coordinates it
        receives.

        Args:
            coordinates (List[shapely.Polygon]): A list of polygon, each polygon ist the bounding box of one traffic-cell we want to split up.

        Returns:
            (boolean): true if successful, otherwise false
        """
        pass