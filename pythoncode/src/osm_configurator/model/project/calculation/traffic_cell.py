import shapely.geometry


class TrafficCell:
    """
    A TrafficCell is an object which describes an area on the earth, it has a name and a bounding box which
    entail the described area from the name.

    Examples:
        The "Karlsruher Schloss" is a trafficCell with the name="Karlsruher Schloss" and its bounding box being
        a polygon of coordinates(latitude, longitude) which entail the area of the "Karlsruher Schloss".
    """
    def __init__(self):
        """
        Creates a new instance of the TrafficCell.
        """
        pass

    def get_name(self):
        """
        Getter for the name of the TrafficCell.

        Returns:
            str: The name of the TrafficCell.
        """
        pass

    def get_bounding_box(self):
        """
        Getter for the bounding box of the TrafficCell.

        Returns:
            shapely.Polygon: A list of coordinates that describe the bounding box of the TrafficCell.
        """
        pass
