from __future__ import annotations

from enum import Enum, unique

import src.osm_configurator.model.model_constants as model_constants_i
import src.osm_configurator.model.parser.tag_parser as tag_parser_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Dict, Tuple, Callable, Final, Any
    from src.osm_configurator.model.project.configuration.category import Category
    from geopandas import GeoSeries

NUMBER_FLOOR_KEY: Final = "building:levels"

"""
If you want to add another Attribute to this method all you need to do is insert the approiate attribute in the enum
definition, notice orders matter.
And furthermore define what the function should calculate on the osm element.
Each function gets the category of the osm element, all previously calculated attributes in a dictionary and
a data, which is standard empty and needs to be changed manually if your function needs special data there.
"""


def _calculate_property_area(category: Category,
                             osm_element: GeoSeries,
                             prev_calculated_attributes: Dict[str, float],
                             data: Any) -> float:
    return osm_element[model_constants_i.CL_GEOMETRY].area


def _calculate_number_of_floors(category: Category,
                                osm_element: GeoSeries,
                                prev_calculated_attributes: Dict[str, float],
                                data: Any) -> float:
    tag_parser_o = tag_parser_i.TagParser()
    for tag in osm_element[model_constants_i.CL_TAGS]:
        parsed_tag = tag_parser_o.parse_tags(tag)
        if NUMBER_FLOOR_KEY in parsed_tag.keys():
            return float(parsed_tag.get(NUMBER_FLOOR_KEY))


def _calculate_floor_area(category: Category,
                          osm_element: GeoSeries,
                          prev_calculated_attributes: Dict[str, float],
                          data: Any) -> float:
    return prev_calculated_attributes.get(Attribute.PROPERTY_AREA.get_name()) * prev_calculated_attributes.get(Attribute.NUMBER_OF_FLOOR.get_name())


@unique
class Attribute(Enum):
    """
    This enum provides a list of Attributes, the DefaultValueEntry and AttractivityAttributes can use.
    If you are interested how exactly these Attributes get used checkout AttractivityPhase.

    Each Attribute saves the name of the attribute, a list of tags that is needed to calculate the attribute and
    a function which describes how the value of the enum is calculated.
    """
    # NOTICE: It is important in which order the Attributes are defined, because the defined order of the attributes
    # is the order in which they get calculated.
    PROPERTY_AREA: Tuple[str, List[str], Callable] = (
        "Property Area", [], _calculate_property_area)  #: The area of the property of the osm-element
    NUMBER_OF_FLOOR: Tuple[str, List[str], Callable] = (
        "Number of Floors", [], _calculate_number_of_floors)  # the number of floors the osm element has
    FLOOR_AREA: Tuple[str, List[str], Callable] = (
        "Floor Area", ["building:levels"], _calculate_floor_area)  # the area that all floors together have

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

    def calculate_attribute_value(self, category: Category,
                                  osm_element: GeoSeries,
                                  prev_calculated_attributes: Dict[str, float],
                                  data: Any):
        """
        Calculates the value of the attribute based on the provided data

        Args:
            category (Category): The Category of the osm element.
            osm_element (GeoSeries): The osm element from which we want to calculate the attribute value for.
            prev_calculated_attributes (Dict[str, float]): All previously calculated attributes in a dictionary accessible by its name, used if you have attributes which depend on each other.
            data (Any): Empty, can be used if your function needs additional data which isn't provided, needs to be changed manually.

        Returns:
            float: the calculated value
        """
        return self.value[2](category, osm_element, prev_calculated_attributes, data)

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
