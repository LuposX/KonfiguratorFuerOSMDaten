from enum import Enum, unique

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Dict
    from src.osm_configurator.model.project.configuration.category import Category


def _calculate_property_area(category: Category, tags: Dict[str, str]) -> float:
    pass


def _calculate_number_of_floors(category: Category, tags: Dict[str, str]) -> float:
    pass


def _calculate_first_floor_area(category: Category, tags: Dict[str, str]) -> float:
    pass


@unique
class Attribute(Enum):
    """
    This enum provides a list of Attributes, the DefaultValueEntry and AttractivityAttributes can use.
    If you are interested how exactly these Attributes get used checkout AttractivityPhase.

    Each Attribute saves the name of the attribute, a list of tags that is needed to calculate the attribute and
    a function which describes how the value of the enum is calculated.
    """
    # TODO: Set the tags they need
    PROPERTY_AREA = ("Property Area", [], _calculate_property_area)  #: The area of the property of the osm-element
    NUMER_OF_FLOOR = ("Number of Floors", [], _calculate_number_of_floors)  #: the number of floors the osm element has
    FIRST_FLOOR_AREA = ("Floor Area", [], _calculate_first_floor_area)  #: the area that the first floor has

    def get_name(self) -> str:
        """
        Getter for the name of the enum type.

        Returns:
            str: Name of the Phase.
        """
        return self.value[0]

    def get_needed_tags(self) -> List[str]:
        """
        Getter for the tags of the enum type.

        Returns:
            List[str]: A list of tag names(keys) that the attribute needs.
        """
        return self.value[1]

    def calculate_attribute_value(self, category: Category, tags: Dict[str, str]) -> float:
        """
        Calculates the value of the attribute based on the provided data

        Args:
            category (Category): A category which is needed to calculate the value
            tags (Dict[str, str]): A dictionary which contains key, value pairs of tags needed for teh calculation.

        Returns:
            float: the calculated value
        """
        return self.value[2](category, tags)
