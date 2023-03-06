from __future__ import annotations

from enum import Enum, unique
from typing import TYPE_CHECKING, Final

import src.osm_configurator.model.model_constants as model_constants_i
import src.osm_configurator.model.parser.tag_parser as tag_parser_i
import src.osm_configurator.model.project.calculation.default_value_finder as default_value_finder_i
import src.osm_configurator.model.project.configuration.calculation_method_of_area_enum \
    as calculation_method_of_area_enum_i


if TYPE_CHECKING:
    from typing import List, Dict, Tuple, Callable, Final, Any
    from src.osm_configurator.model.project.configuration.category import Category
    from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
    from geopandas import GeoSeries, GeoDataFrame
    from pandas import Series


NUMBER_FLOOR_KEY: Final = "building:levels"
BUILDING_KEY: Final = "building"

"""
If you want to add another Attribute to this method all you need to do is insert the appropriate attribute in the enum
definition, notice orders matter.
And furthermore define what the function should calculate on the osm element.
Each function gets the category of the osm element, all previously calculated attributes in a dictionary and
a data, which is standard empty and needs to be changed manually if your function needs special data there.
Additional curr_default_value are the default values for the osm element and category.
"""


def _calculate_property_area(category: Category,
                             osm_element: Series,
                             prev_calculated_attributes: Dict[str, float],
                             curr_default_value: DefaultValueEntry,
                             data: Any) -> float:
    df: GeoDataFrame = data

    # if the osm element we look at is a node, we can't calculate the value of it
    if osm_element[model_constants_i.CL_OSM_TYPE] == model_constants_i.NODE_NAME:
        return curr_default_value.get_attribute_default(Attribute.PROPERTY_AREA)

    # The site area of an osm element is described by its geometry, so we can calculate the area from it.
    if category.get_calculation_method_of_area() == calculation_method_of_area_enum_i.CalculationMethodOfArea\
            .CALCULATE_SITE_AREA:
        return osm_element[model_constants_i.CL_GEOMETRY].area

    # If we want to calculate the building area, we need to check which osm_element which are building are in the border
    # of the osm element and then sum up the area of these osm elements.
    elif category.get_calculation_method_of_area() == calculation_method_of_area_enum_i.CalculationMethodOfArea\
            .CALCULATE_BUILDING_AREA:
        tag_parser_o = tag_parser_i.TagParser()

        # Find out all osm element which lie in the given osm element
        # this gives us trues and false for each entry true if it lies in the osm element otherwise false
        found_areas_bool: GeoSeries = df.within(
            osm_element[model_constants_i.CL_GEOMETRY])  # TODO: This could be wrong if yes use contains() instead

        # we will use this to sum up the area of all buildings
        area_sum: int = 0

        # if the osm element is a building we don't need to check if other building are in it "doesn't make sense"
        osm_tags: List[Tuple[str, str]] = tag_parser_o.dataframe_tag_parser(osm_element[model_constants_i.CL_TAGS])
        osm_tags: Dict[str, str] = tag_parser_o.list_to_dict(osm_tags)
        if BUILDING_KEY in osm_tags.keys():
            return osm_element[model_constants_i.CL_GEOMETRY].area

        # Iterate over all found osm element and check if they have the building tag
        found_series: Series
        for i, found_series in df.loc[found_areas_bool].iterrows():
            # the found_series saves the tags as string representation of a list
            # we transform it into an actual list
            transformed_list: List[Tuple[str, str]] = tag_parser_o\
                .dataframe_tag_parser(found_series[model_constants_i.CL_TAGS])
            dict_transformed_list: Dict[str, str] = tag_parser_o.list_to_dict(transformed_list)

            if dict_transformed_list.get(BUILDING_KEY) is not None:
                # if its a node use default values for it
                if found_series[model_constants_i.CL_OSM_TYPE] == model_constants_i.NODE_NAME:
                    curr_default_value_list: List[DefaultValueEntry] = category.get_default_value_list()

                    default_value: DefaultValueEntry = default_value_finder_i\
                        .find_default_value_entry_which_applies(curr_default_value_list,
                                                                dict_transformed_list)

                    # add default values to the sum
                    area_sum += default_value.get_attribute_default(Attribute.PROPERTY_AREA)

                else:
                    # add the calculated area to the area sum of all osm elements.
                    area_sum += found_series[model_constants_i.CL_GEOMETRY].area

        return area_sum

    # For future expansion maybe used.
    else:
        return curr_default_value.get_attribute_default(Attribute.PROPERTY_AREA)


def _calculate_number_of_floors(category: Category,
                                osm_element: Series,
                                prev_calculated_attributes: Dict[str, float],
                                curr_default_value: DefaultValueEntry,
                                data: Any) -> float:
    tag_parser_o = tag_parser_i.TagParser()
    tag_list: List[Tuple[str, str]] = tag_parser_o.dataframe_tag_parser(osm_element[model_constants_i.CL_TAGS])
    dict_tag_list: Dict[str, str] = tag_parser_o.list_to_dict(tag_list)

    for key, value in dict_tag_list.items():
        if NUMBER_FLOOR_KEY == key:
            return float(value)

    return curr_default_value.get_attribute_default(Attribute.NUMBER_OF_FLOOR)


def _calculate_floor_area(category: Category,
                          osm_element: Series,
                          prev_calculated_attributes: Dict[str, float],
                          curr_default_value: DefaultValueEntry,
                          data: Any) -> float:

    return prev_calculated_attributes.get(Attribute.PROPERTY_AREA.get_name()) * \
        prev_calculated_attributes.get(Attribute.NUMBER_OF_FLOOR.get_name())


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
    NUMBER_OF_FLOOR: Tuple[str, List[str], Callable] = (
        "Number of Floors",
        _calculate_number_of_floors
    )  # the number of floors the osm element has

    PROPERTY_AREA: Tuple[str, List[str], Callable] = (
        "Property Area",
        _calculate_property_area
    )  #: The area of the property of the osm-element

    FLOOR_AREA: Tuple[str, List[str], Callable] = (
        "Floor Area",
        _calculate_floor_area
    )  # the area that all floors together have

    def get_name(self) -> str:
        """
        Getter for the name of the enum type.

        Returns:
            str: Name of the Phase.
        """
        return self.value[0]

    def calculate_attribute_value(self, category: Category,
                                  osm_element: Series,
                                  prev_calculated_attributes: Dict[str, float],
                                  curr_default_value: DefaultValueEntry,
                                  data: Any):
        """
        Calculates the value of the attribute based on the provided data

        Args:
            category (Category): The Category of the osm element.
            osm_element (Series): The osm element from which we want to calculate the attribute value for.
            prev_calculated_attributes (Dict[str, float]): All previously calculated attributes in a dictionary
                accessible by its name, used if you have attributes which depend on each other.
            curr_default_value (DefaultValueEntry): Default value for the osm element.
            data (Any): Empty, can be used if your function needs additional data which isn't provided,
                needs to be changed manually.

        Returns:
            float: the calculated value
        """
        return self.value[1](category, osm_element, prev_calculated_attributes, curr_default_value, data)

    @staticmethod
    def convert_str_to_attribute(name: str) -> Attribute | None:
        """
        Converts a given string to the associated Attribute.

        Args:
            name (str): The string.

        Returns:
            Attribute: Associated Attribute.
        """
        for attribute in Attribute:
            if attribute.get_name() == name:
                return attribute
        return None

