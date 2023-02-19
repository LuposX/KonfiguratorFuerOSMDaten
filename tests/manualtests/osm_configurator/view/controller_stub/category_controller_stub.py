import pathlib

from src.osm_configurator.control.category_controller_interface import ICategoryController
from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
from src.osm_configurator.model.project.configuration.category import Category


class CategoryControllerStub(ICategoryController):
    def check_conflicts_in_category_configuration(self, path: pathlib.Path) -> bool:
        """
        Returns:
            bool: True, if the path exists, else false
        """
        return path.exists()

    def import_category_configuration(self, path: pathlib.Path) -> bool:
        return True

    def get_list_of_categories(self) -> list[Category]:
        return []

    def create_category(self, name: str) -> Category:
        category = Category(name)
        return category

    def delete_category(self, category: Category) -> bool:
        return True

    def get_list_of_key_recommendations(self, current_input: str) -> list[str]:
        return []

    def get_attractivities_of_category(self, category: Category) -> list[AttractivityAttribute]:
        return []