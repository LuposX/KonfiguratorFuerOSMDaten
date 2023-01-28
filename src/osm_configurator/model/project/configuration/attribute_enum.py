from __future__ import annotations

from enum import Enum, unique

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Dict
    from typing import Tuple
    from src.osm_configurator.model.project.configuration.category import Category


def _calculate_property_area(category: Category, tags: Dict[str, str]) -> float:
    pass


def _calculate_number_of_floors(category: Category, tags: Dict[str, str]) -> float:
    pass


def _calculate_floor_area(category: Category, tags: Dict[str, str]) -> float:
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
    PROPERTY_AREA: Tuple[str, List[str], str] = ("Property Area", [], _calculate_property_area)  #: The area of the property of the osm-element
    NUMBER_OF_FLOOR: Tuple[str, List[str], str] = ("Number of Floors", [], _calculate_number_of_floors)  # the number of floors the osm element has
    FLOOR_AREA: Tuple[str, List[str], str] = ("Floor Area", ["building:levels"], _calculate_floor_area)  # the area that all floors together have

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

    @classmethod
    def get_all_tags(cls) -> List[str]:
        """
        Return all used Tags fromm all attributes:

        Returns:
            List[str]: A list of tags from the attributes.
        """
        all_tags: List[str] = []
        member: Attribute
        for member in cls:
            all_tags.extend(member.value[1])
        return all_tags
