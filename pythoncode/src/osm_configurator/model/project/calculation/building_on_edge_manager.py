import pathlib
import shapely


class BuildingOnEdgeManager:
    """
    This class handles the edge-case when buildings are on the edge of
    specified bounding-box.
    It is mainly used to remove building which lie on said edge.
    """

    def __init__(self, file_paths, border):
        """
         Creates a new instance of the "BuildingOnEdgeManager".

        Args:
            file_paths (List[pathlib.Path]): a list of path each pointing towards a osm-data file from which we want
                                            to remove the buildings on the dge
            border (List[shapely.Polygon]): a list of polygon, each polygon belogns to one entry in the file_path list
                                            and specifies the border of said file.
        """
        pass

    def remove_buildings_on_edge(self):
        """
        Reads in the data from the file path it got, and removes all buildings
        from the data that lie on the edge.
        This means building which are on the edge, half in half out.

        Returns:
            (boolean): true when successful, otherwise false.
        """
        pass