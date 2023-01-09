from enum import Enum, unique


@unique
class AttractivityAttribute(Enum):
    """
    This enum provides a list of Attributes, the DefaultValueEntry and AttractivityAttributes can use.
    If you are interested how exactly these Attributes get used checkout AttractivityPhase.
    """
    PROPERTY_AREA = "Property Area"  #: The area of the property of the osm-element
    NUMER_OF_FLOOR = "Number of Floors"  #: the number of floors the osm element has
    FIRST_FLOOR_AREA = "Floor Area"  #: the area that the first floor has

    def get_name(self):
        """
        Getter for the name of the enum type.

        Returns:
            (str): Name of the Phase.
        """
        return self.value


