from __future__ import annotations

import src.osm_configurator.model.project.configuration.category

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List


class CategoryManager:
    """
    Category Manager holds a list of categories and changes them according to the given needs.
    """

    _categories = [] # List of categories

    def __init__(self, categories):
        """
        Constructor of the class.

        Args:
            categories (Category): Starting list of categories.
        """
        self._categories = categories

    def get_category(self, index):
        """
        Gets a category based on the index.

        Args:
            index (int): Index in the categories-list, that will be returned.

        Returns:
            category.Category: The Category we wanted.
        """
        if index < 0 or index > len(self._categories):
            return -1
        return self._categories[index]

    def get_categories(self) -> List:
        """
        Getter for all the Categories.

        Returns:
            list[Category]: List of the chosen categories.
        """
        return self._categories

    def create_category(self, new_category):
        """
        Creates a new category, that will be empty.

        Returns:
            category.Category: The newly created category.
        """
        if new_category not in self._categories:
            self._categories.append(new_category)
            return True
        return False

    def remove_category(self, category):
        """
        Removes the given category from the categories list, if element is inside the List.

        Args:
            category (Category): Category that will be removed.

        Returns:
            bool: True, if the element was removed correctly, else false.
        """
        if category in self._categories:
            self._categories.remove(category)
            return True
        return False

    def override_categories(self, new_category_list):
        """
        Overwrites the list of categories with the given list, if both lists are not identical.

        Args:
            new_category_list (list[Categories]): List of categories, that will overwrite the already existing list.

        Returns:
            bool: True, if the replacement was successful, else False.
        """
        if self._categories != new_category_list:
            self._categories = new_category_list
            return True
        return False

    def merge_categories(self, category_input_list):
        """
        Merges the existing category list with the given list if both lists are not identical.

        Args:
            category_input_list (list[Category]): New list of categories that will be merged into the existing list.

        Returns:
            bool: True, if the merging was successful, else False.
        """
        if self._categories == category_input_list:
            return False

        for category in category_input_list:
            if category not in self._categories:
                self._categories.append(category)
        return True
