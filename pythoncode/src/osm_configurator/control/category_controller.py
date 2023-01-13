import src.osm_configurator.model.application.application_interface
import src.osm_configurator.model.project.configuration.category
import src.osm_configurator.model.project.configuration.attractivity_attribute
import pathlib


class CategoryController:
    """
    The CategoryController is responsible for consistently forwarding requests to the model,
    regarding changes to the categories of the current project.
    """

    def __init__(self, model):
        """
        Creates a new instance of the CategoryController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        pass

    def check_conflicts_in_category_configuration(self, path):
        """
        Checks for a given file, if it is a valid category-file and checks, whether there are naming conflicts with the categories of the currently selected project.

        Args:
            path (pathlib.Path): The path to the category-file.

        Returns:
            bool: True, if there is currently a project selected and there are no naming conflicts; False, otherwise.
        """
        pass

    def import_category_configuration(self, path):
        """
        Imports the given categories into the currently selected project.
        Adds the given categories to the category list of the project.

        Args:
            path (pathlib.Path): The path to the category file.

        Returns:
            bool: True, if the categories where added successfully; False, if there is no project loaded, the category file is corrupted or the category file does not exist.
        """
        pass

    def get_list_of_categories(self):
        """
        Returns the list of all categories, that are currently in the currently selected project.

        Returns:
            list[category.Category]: A list of the categories of the project in no particular order.
        """
        pass

    def create_category(self):
        """
        Creates a new category in the currently selected project.
        A new category is added to the list of categories of the project. The category has empty properties, except for an arbitrary name.
        If the creation fails, none will be returned and there won't be a category added.

        Returns:
            category.Category: The newly created category, none if there was an error.
        """
        pass

    def delete_category(self, category):
        """
        Deletes the given category.
        Removes the given category from the list of categories of the currently selected project.

        Args:
            category (category.Category): The category to be deleted.

        Returns:
            bool: True, if the category was deleted successfully; False, otherwise.
        """
        pass

    def get_list_of_key_recommendations(self, current_input):
        """
        Returns a list of recommended keys, based on the input that is already entered by the user.

        Args:
            current_input (str): The input that is currently written by the user.

        Returns:
            list[str]: A list of key recommendations based on the current_input.
        """
        pass

    def get_attractivities_of_category(self, category):
        """
        Returns the attractivity attributes that are defined for the given category.

        Args:
            category (category.Category): The category, whose attractivities are of interest.

        Returns:
            list[attractivity_attribute.AttractivityAttribute]: The list of attractivity attributes of the given category.
        """
        pass
