from __future__ import annotations

import os

import src.osm_configurator.model.project.configuration.category as category_i
import src.osm_configurator.model.project.configuration.default_categories as default_categories_i
import pathlib
from pathlib import Path

from typing import TYPE_CHECKING

from src.osm_configurator.model.parser.category_parser import CategoryParser

if TYPE_CHECKING:
    from typing import List, Set
    from pathlib import Path
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from src.osm_configurator.model.project.configuration.category import Category
    from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute

CSV_ENDING: str = ".csv"


def _load_categories_from_path(path: Path) -> List[Category]:
    """
    Loads all categories from the given path.

    Args:
        path (pathlib.Path): Path to the folder that contains the categories.

    Returns:
        List[category_i.Category]: List of all categories.
    """
    category_parser: CategoryParser = CategoryParser()
    categories: List[Category] = []
    for file in os.listdir(path):
        category: Category = category_parser.parse_category_file(
            Path(str(os.path.join(path, file))))
        if category is not None:
            categories.append(category)
        else:
            return []
    return categories


class CategoryManager:
    """
    Category Manager holds a list of categories and changes them according to the given needs.
    """

    def __init__(self):
        """
        Constructor of the class.
        """
        self._categories: List[Category] = []
        building_category: Category = default_categories_i.create_building_category()

        self._categories.append(building_category)

    def get_activated_attribute(self) -> List[Attribute]:
        """
        Return a list of all used attributes, of all categories.
        This is used to know which tags we need to save.

        Returns:
            List[Attribute]: A list that contains all used attributes
        """
        _activated_attributes: List[Attribute] = []

        for category in self._categories:
            for attribute in category.get_activated_attribute():
                if attribute not in _activated_attributes:
                    _activated_attributes.append(attribute)
        return _activated_attributes

    def get_category(self, name: str) -> Category | None:
        """
        Gets a category based on the index.

        Args:
            name (str): IThe name of the category.

        Returns:
            category_i.Category: The Category we wanted.
        """
        for item in self._categories:
            if item.get_category_name() == name:
                return item
        return None

    def get_categories(self) -> List[Category]:
        """
        Getter for all the Categories.

        Returns:
            List[category_i.Category]: List of the chosen categories.
        """
        return self._categories

    def create_category(self, new_category: Category) -> bool:
        """
        Creates a new category, that will be empty.

        Args:
            new_category (category_i.Category): Category that will be created.

        Returns:
            bool: True, if the element was created correctly, else false.
        """

        if new_category.get_category_name() == "":
            return False
        # Check that the category is not already saved
        elif new_category.get_category_name() in self.get_all_categories_names():
            return False

        else:
            self._categories.append(new_category)
            return True

    def remove_category(self, category_to_remove: Category) -> bool:
        """
        Removes the given category from the categories list, if element is inside the List.

        Args:
            category_to_remove (category_i.Category): Category that will be removed.

        Returns:
            bool: True, if the element was removed correctly, else false.
        """
        # Check if the element is in the list
        for category in self._categories:
            if category_to_remove.get_category_name() == category.get_category_name():
                self._categories.remove(category_to_remove)
                return True
        return False

    def override_categories(self, new_category_list_path: Path) -> bool:
        """
        Overwrites the list of categories with the given list.

        Args:
            new_category_list_path (pathlib.Path): Path to a list of categories, that will overwrite the already existing list.

        Return:
            bool: True if overwriting works, otherwise false.
        """
        self._categories = _load_categories_from_path(new_category_list_path)
        return True

    def merge_categories(self, new_category_list_path: Path):
        """
        Overwrites the list of categories with the given list.

        Args:
            new_category_list_path (pathlib.Path): Path to a list of categories, that will overwrite the already existing list.

        Return:
            bool: True if merging works, otherwise false.
        """
        self.add_categories(_load_categories_from_path(new_category_list_path))
        return True

    def add_categories(self, category_input_list: List[Category]):
        """
        Merges the existing category list with the given list if both lists are not identical.

        Args:
           category_input_list (List[category_i.Category]): New list of categories that will be merged into the existing list.
        """
        for category in category_input_list:
            if category.get_category_name() not in self.get_all_categories_names():
                self._categories.append(category)

    def get_all_defined_attractivity_attributes(self) -> List[AttractivityAttribute]:
        """
        Gets all defined attractivity attributes.
        Doesn't have dupplicates.

        Returns:
            (List[AttractivityAttribute]): Attractivity Attributes
        """
        result: Set[AttractivityAttribute] = set([])

        category: Category
        for category in self._categories:
            result.update(category.get_attractivity_attributes())
        return list(result)

    def get_all_categories_names(self) -> List[str]:
        """
        This method return the names of all categories currently saved.
        """
        name_list: List[str] = []
        for category in self._categories:
            name_list.append(category.get_category_name())
        return name_list
