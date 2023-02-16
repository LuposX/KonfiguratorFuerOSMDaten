from src.osm_configurator.control.category_controller_interface import ICategoryController
import pathlib

from src.osm_configurator.model.parser.category_parser import CategoryParser
from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.osm_configurator.model.application.application_interface import IApplication
    from src.osm_configurator.model.project.configuration.category import Category
    from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute


class CategoryController(ICategoryController):
    __doc__ = ICategoryController.__doc__

    def __init__(self, model: IApplication):
        """
        Creates a new instance of the CategoryController, with an association to the model.

        Args:
            model (application_interface.IApplication): The interface which is used to communicate with the model.
        """
        self._model = model
        self._category_manager: CategoryManager = model.get_active_project().get_config_manager().get_category_manager()

    def check_conflicts_in_category_configuration(self, path: pathlib.Path) -> bool:
        category_parser: CategoryParser = CategoryParser()
        new_category: Category = category_parser.parse_category_file(path)
        if new_category is None:
            return False
        elif new_category.get_category_name() in self._category_manager.get_all_categories_names():
            return False
        return True

    def import_category_configuration(self, path: pathlib.Path) -> bool:
        return self._category_manager.merge_categories(path)

    def get_list_of_categories(self) -> List[Category]:
        return self._category_manager.get_categories()

    def create_category(self, name: str) -> Category:
        new_category: Category = Category(name)
        if self._category_manager.create_category(new_category):
            return new_category
        else:
            return None

    def delete_category(self, category: Category) -> bool:
        return self._category_manager.remove_category(category)

    def get_list_of_key_recommendations(self, current_input: str) -> list[str]:
        return self._model.get_key_recommendation_system().recommend_key(current_input)
    # Todo which path should be given to the method

    def get_attractivities_of_category(self, category: Category) -> List[AttractivityAttribute]:
        return category.get_attractivity_attributes()
