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

TABLE_FIRST_COLUMN: int = 0  # Describes the type of data stored in the following columns.
TABLE_SECOND_COLUMN: int = 1  # In this column specific data is stored
TABLE_FIRST_ROW: int = 0  # This row stores the name of the category
TABLE_SECOND_ROW: int = 1  # This row stores the status of the category
TABLE_THIRD_ROW: int = 2  # This row stores the white-list of the category
TABLE_FOURTH_ROW: int = 3  # This row stores the black-list of the category
TABLE_FIFTH_ROW: int = 4  # This row stores the calculation_method_of_area of the category
TABLE_SIXTH_ROW: int = 5  # This row stores the active_attributes of the category
TABLE_SEVENTH_ROW: int = 6  # This row stores the status of strictly_use_default_values of the category
TABLE_EIGHT_ROW: int = 7  # This row stores the attractivity_attributes of the category
TABLE_NINE_ROW: int = 8  # This row stores the default_value_list of the category

NAME: int = 0  # The name of an attractivity_attribute and a default_value_entry is stored in the first place of the list representing it
NAME_OF_ATTRIBUTE: int = 0  # The name of an attribute of an attractivity_attribute or a default_value_entry is stored in the second place of the list representing it
VALUE_OF_ATTRIBUTE: int = 1  # The value of an attribute of an attractivity_attribute or a default_value_entry is stored in the second place of the list representing it


class CategoryParser(CategoryParserInterface):
    __doc__ = CategoryParserInterface.__doc__

    def __init__(self):
        """
        Creates a new instance of the CategoryParser.
        """
        pass

    def parse_category_file(self, filepath: Path) -> Category | None:
        with open(filepath, READ) as f:
            reader = csv.reader(f)
            category_data: list[str] = list(reader)
        category_name: str = category_data[TABLE_FIRST_ROW][TABLE_SECOND_COLUMN]
        if isinstance(category_name, str):
            loaded_category: Category = Category(category_data[TABLE_FIRST_ROW][TABLE_SECOND_COLUMN])
        else:
            return None
        if CategoryParser.convert_bool(category_data[TABLE_SECOND_ROW][TABLE_SECOND_COLUMN]) is None:
            return None
        elif CategoryParser.convert_bool(category_data[TABLE_SECOND_ROW][TABLE_SECOND_COLUMN]):
            loaded_category.activate()
        else:
            loaded_category.deactivate()

        # Loads whitelist
        loaded_category.set_whitelist(category_data[TABLE_THIRD_ROW][TABLE_SECOND_COLUMN].split(DELIMITER_SEMICOLON))

        # Loads blacklist
        loaded_category.set_blacklist(category_data[TABLE_FOURTH_ROW][TABLE_SECOND_COLUMN].split(DELIMITER_SEMICOLON))

        # Loads calculation method of area
        loaded_category.set_calculation_method_of_area(
            CalculationMethodOfArea.convert_str_to_calculation_method_of_area(
                category_data[TABLE_FIFTH_ROW][TABLE_SECOND_COLUMN]))

        # Loads active attributes
        if category_data[TABLE_SIXTH_ROW][TABLE_SECOND_COLUMN] != EMPTY_STRING:
            active_attributes: list[str] = category_data[TABLE_SIXTH_ROW][TABLE_SECOND_COLUMN].split(
                DELIMITER_SEMICOLON)
            for active_attribute_str in active_attributes:
                active_attribute: Attribute = Attribute.convert_str_to_attribute(active_attribute_str)
                if active_attribute is not None:
                    loaded_category.set_attribute(active_attribute, True)
                else:
                    return None

        # Loads strictly use default values
        strictly_use_default_value_bool: bool = CategoryParser.convert_bool(category_data[TABLE_SEVENTH_ROW][TABLE_SECOND_COLUMN])
        if strictly_use_default_value_bool is not None:
            loaded_category.set_strictly_use_default_values(strictly_use_default_value_bool)
        else:
            return None

        # Loads attractivity attributes
        attractivity_attribute_list: list[str] = category_data[TABLE_EIGHT_ROW][TABLE_SECOND_COLUMN].split(
            DELIMITER_SEMICOLON)

        if len(attractivity_attribute_list) == 1 and '' in attractivity_attribute_list:
            pass
        else:
            for input_attractivity_attribute in attractivity_attribute_list:
                input_str: list[str] = input_attractivity_attribute.split(DELIMITER_COMMA)
                attractivity_attribute: AttractivityAttribute = AttractivityAttribute(
                    input_str[NAME])
                input_str.remove(input_str[NAME])
                for attribute_str in input_str:
                    attribute_str_split_up: list[str] = attribute_str.split(DELIMITER_COLON)
                    if attribute_str_split_up[NAME_OF_ATTRIBUTE] == BASE:
                        attractivity_attribute.set_base_factor(float(attribute_str_split_up[VALUE_OF_ATTRIBUTE]))
                    else:
                        attractivity_attribute.set_attribute_factor(
                            Attribute.convert_str_to_attribute(attribute_str_split_up[NAME_OF_ATTRIBUTE]),
                            float(attribute_str_split_up[VALUE_OF_ATTRIBUTE]))
                loaded_category.add_attractivity_attribute(attractivity_attribute)

            # Delete default-tag
        loaded_category.get_default_value_list().clear()

        # Loads default value entries
        default_value_entry_list: list[str] = category_data[TABLE_NINE_ROW][TABLE_SECOND_COLUMN].split(
            DELIMITER_SEMICOLON)
        for input_default_value_entry in default_value_entry_list:
            input_str: list[str] = input_default_value_entry.split(DELIMITER_COMMA)
            default_value_entry: DefaultValueEntry = DefaultValueEntry(input_str[NAME])
            input_str.remove(input_str[NAME])
            for default_value_entry_str in input_str:
                attribute_str_split_up: list[str] = default_value_entry_str.split(DELIMITER_COLON)
                default_value_entry.set_attribute_default(
                    Attribute.convert_str_to_attribute
                    (attribute_str_split_up[NAME_OF_ATTRIBUTE]), float(attribute_str_split_up[VALUE_OF_ATTRIBUTE]))
            loaded_category.add_default_value_entry(default_value_entry)
        return loaded_category

    @staticmethod
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
