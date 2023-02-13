from __future__ import annotations

import csv

from src.osm_configurator.model.parser.category_parser_interface import CategoryParserInterface

from typing import TYPE_CHECKING, Final

from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
from src.osm_configurator.model.project.configuration.category import Category

if TYPE_CHECKING:
    from pathlib import Path
    from src.osm_configurator.model.project.configuration.category import Category

EMPTY_STRING: str = ""
READ: str = "r"
TRUE: str = "True"
FALSE: str = "False"
DELIMITER_SEMICOLON: str = ";"
DELIMITER_COMMA: str = ","
DELIMITER_COLON: str = ":"
BASE: str = "base"



def convert_bool(string: str) -> bool | None:
    """
    Converts a string to the associated boolean.

    Args:
        string(str): The string.

    Returns:
        bool: The value of the string.
    """
    if string == TRUE:
        return True
    if string == FALSE:
        return False
    else:
        return None


class CategoryParser(CategoryParserInterface):
    __doc__ = CategoryParserInterface.__doc__

    def __init__(self):
        """
        Creates a new instance of the CategoryParser.
        """
        pass

    def parse_category_file(self, filepath: Path) -> Category:
        with open(filepath, READ) as f:
            reader = csv.reader(f)
            category_data: list[str] = list(reader)
        loaded_category: Category = Category()
        loaded_category.set_category_name(category_data[0][1])
        if convert_bool(category_data[1][1]) is None:
            return False
        elif convert_bool(category_data[1][1]):
            loaded_category.activate()
        else:
            loaded_category.deactivate()

        # Loads whitelist
        loaded_category.set_whitelist(category_data[2][1].split(DELIMITER_SEMICOLON))

        # Loads blacklist
        loaded_category.set_blacklist(category_data[3][1].split(DELIMITER_SEMICOLON))

        # Loads calculation method of area
        loaded_category.set_calculation_method_of_area(
            CalculationMethodOfArea.convert_str_to_calculation_method_of_area(category_data[4][1]))

        # Loads active attributes
        if category_data[5][1] != EMPTY_STRING:
            active_attributes: list[str] = category_data[5][1].split(DELIMITER_SEMICOLON)
            for active_attribute_str in active_attributes:
                active_attribute: Attribute = Attribute.convert_str_to_attribute(active_attribute_str)
                if active_attribute is not None:
                    loaded_category.set_attribute(active_attribute, True)
                else:
                    return False

        # Loads strictly use default values
        strictly_use_default_value_bool: bool = convert_bool(category_data[6][1])
        if strictly_use_default_value_bool is not None:
            loaded_category.set_strictly_use_default_values(strictly_use_default_value_bool)
        else:
            return False

        # Loads attractivity attributes
        attractivity_attribute_list: list[str] = category_data[7][1].split(DELIMITER_SEMICOLON)
        for input_attractivity_attribute in attractivity_attribute_list:
            input_str: list[str] = input_attractivity_attribute.split(DELIMITER_COMMA)
            attractivity_attribute: AttractivityAttribute = AttractivityAttribute(input_str[0], 0)
            input_str.remove(input_str[0])
            for attribute_str in input_str:
                attribute_str_split_up: list[str] = attribute_str.split(DELIMITER_COLON)
                if attribute_str_split_up[0] == BASE:
                    attractivity_attribute.set_base_factor(float(attribute_str_split_up[1]))
                else:
                    attractivity_attribute.set_attribute_factor(
                        Attribute.convert_str_to_attribute(attribute_str_split_up[0]),
                        float(attribute_str_split_up[1]))
            loaded_category.add_attractivity_attribute(attractivity_attribute)

        # Loads default value entries
        default_value_entry_list: list[str] = category_data[8][1].split(DELIMITER_SEMICOLON)
        for input_default_value_entry in default_value_entry_list:
            input_str: list[str] = input_default_value_entry.split(DELIMITER_COMMA)
            default_value_entry: DefaultValueEntry = DefaultValueEntry(input_str[0])
            input_str.remove(input_str[0])
            for default_value_entry_str in input_str:
                attribute_str_split_up: list[str] = default_value_entry_str.split(DELIMITER_COLON)
                default_value_entry.set_attribute_default(Attribute.convert_str_to_attribute(attribute_str_split_up[0]),
                                                          float(attribute_str_split_up[1]))
            loaded_category.add_default_value_entry(default_value_entry)
        return loaded_category
