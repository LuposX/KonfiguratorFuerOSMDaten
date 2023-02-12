from __future__ import annotations

import src.osm_configurator.model.project.configuration.category
import src.osm_configurator.model.project.configuration.category as category_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Dict, Set
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from src.osm_configurator.model.project.configuration.category import Category
    from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute


class CategoryManager:
    """
    Category Manager holds a list of categories and changes them according to the given needs.
    """

    def __init__(self):
        """
        Constructor of the class.
        """
        self._categories: List[Category] = []

    def get_activated_attribute(self) -> List[Attribute]:
        """
        Return a list of all used attributes, of all categories.
        This is used to know which tags we need to save.

        Returns:
            List[Attribute]: A list that contains all used attributes
        """
        _activated_attributes = []

        for category in self._categories:
            for attribute in category.get_activated_attribute():
                if attribute not in _activated_attributes:
                    _activated_attributes.append(attribute)
        return _activated_attributes

    def get_category(self, name: str) -> Category:
        """
        Gets a category based on the index.

        Args:
            name (str): IThe name of the category.

        Returns:
            Category: The Category we wanted.
        """
        item: Category
        for item in self._categories:
            if item.get_category_name() == name:
                return item

        # TODO: IDK WHAT TO DO HERE
        return None

    def get_categories(self) -> List[Category]:
        """
        Getter for all the Categories.

        Returns:
            List[Category]: List of the chosen categories.
        """
        return self._categories

    def create_category(self, new_category: Category) -> bool:
        """
        Creates a new category, that will be empty.

        Args:
            new_category (Category): Category that will be created.

        Returns:
            bool: True, if the element was created correctly, else false.
        """
        # Check that the category is not already saved
        found: bool = False
        if new_category.get_category_name() in self._get_all_categories_names():
            return False

        else:
            self._categories.append(new_category)
            return True

    def remove_category(self, category_to_remove: Category) -> bool:
        """
        Removes the given category from the categories list, if element is inside the List.

        Args:
            category_to_remove (Category): Category that will be removed.

        Returns:
            bool: True, if the element was removed correctly, else false.
        """
        # Check if the element is in the list
        found: bool = False
        category: Category
        for category in self._categories:
            if category_to_remove.get_category_name() == category.get_category_name():
                found = True
                self._categories.remove(category_to_remove)
                break

        if found:
            return True
        else:
            return False

    def override_categories(self, new_category_list: List[Category]):
        """
        Overwrites the list of categories with the given list, if both lists are not identical.

        Args:
            new_category_list (List[Categories]): List of categories, that will overwrite the already existing list.
        """
        self._categories = new_category_list

    def add_categories(self, category_input_list: List[Category]):
        """
       Merges the existing category list with the given list if both lists are not identical.

       Args:
           category_input_list (List[Category]): New list of categories that will be merged into the existing list.
       """
        for category in category_input_list:
            if category.get_category_name() not in self._get_all_categories_names():
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

    def _get_all_categories_names(self) -> List[str]:
        """
        This method return the names of all categories currently saved.
        """
        name_list: List[str] = []
        for category in self._categories:
            name_list.append(category.get_category_name())

        return name_list

