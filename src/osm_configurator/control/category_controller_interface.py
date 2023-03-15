from __future__ import annotations

from abc import ABC, abstractmethod

import pathlib

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.category import Category
    from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute


class ICategoryController(ABC):
    """
    The CategoryController is responsible for consistently forwarding requests to the model,
    regarding changes to the categories of the current project.
    """

    @abstractmethod
    def check_conflicts_in_category_configuration(self, path: pathlib.Path) -> bool:
        """
        Checks for a given file, if it is a valid category-file and checks, whether there are naming conflicts
        with the categories of the currently selected project.

        Args:
            path (pathlib.Path): The path to the category-file.

        Returns:
            bool: True, if there is currently a project selected and there are no naming conflicts; False, otherwise.
        """
        pass

    @abstractmethod
    def import_category_configuration(self, path: pathlib.Path) -> bool:
        """
        Imports the given categories into the currently selected project.
        Adds the given categories to the category list of the project.

        Args:
            path (pathlib.Path): The path to the category file.

        Returns:
            bool: True, if the categories where added successfully; False, if there is no project loaded, the category
                file is corrupted or the category file does not exist.
        """
        pass

    @abstractmethod
    def get_list_of_categories(self) -> List[Category]:
        """
        Returns the list of all categories, that are currently in the currently selected project.

        Returns:
            list[category.Category]: A list of the categories of the project in no particular order.
        """
        pass

    @abstractmethod
    def create_category(self, name: str) -> Category:
        """
        Creates a new category in the currently selected project.
        A new category is added to the list of categories of the project. The category has empty properties,
        except for an arbitrary name.
        If the creation fails, none will be returned and there won't be a category added.

        Args:
            name (str): The name, of the new Category.

        Returns:
            category.Category: The newly created category, none if there was an error.
        """
        pass

    @abstractmethod
    def delete_category(self, category: Category) -> bool:
        """
        Deletes the given category.
        Removes the given category from the list of categories of the currently selected project.

        Args:
            category (category.Category): The category to be deleted.

        Returns:
            bool: True, if the category was deleted successfully; False, otherwise.
        """
        pass

    @abstractmethod
    def get_list_of_key_recommendations(self, current_input: str) -> list[str]:
        """
        Returns a list of recommended keys, based on the input that is already entered by the user.

        Args:
            current_input (str): The input that is currently written by the user.

        Returns:
            list[str]: A list of key recommendations based on the current_input.
        """
        pass

    @abstractmethod
    def get_attractivities_of_category(self, category: Category) -> List[AttractivityAttribute]:
        """
        Returns the attractivity attributes that are defined for the given category.

        Args:
            category (category.Category): The category, whose attractivities are of interest.

        Returns:
            list[attractivity_attribute.AttractivityAttribute]: The list of attractivity attributes
                of the given category.
        """
        pass
