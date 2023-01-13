import pathlib
import shapely


class BuildingOnEdgeManager:
    """
    This class handles the edge-case when buildings are on the edge of
    specified bounding-box.
    It is mainly used to remove building that are on this edge.
    """

    def __init__(self, file_paths, border):
        """
         Creates a new instance of the "BuildingOnEdgeManager".

        Args:
            file_paths (List[pathlib.Path]): A list of path each pointing towards an osm-data file through which we want
                                            to remove the buildings on the edge.
            border (List[shapely.Polygon]): A list of polygon. Each polygon belongs to one entry in the file_path list
                                            and specifies the border of said file.
        """
        pass

    def remove_buildings_on_edge(self):
        """
        Reads in the data from the file path it got, and removes all buildings
        from the data that are on the edge.
        This means building which are on the edge, half in half out.

        Returns:
            bool: True when successful, otherwise false.
        """
        pass
