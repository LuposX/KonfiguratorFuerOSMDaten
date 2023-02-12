import pathlib

from src.osm_configurator.control.category_controller_interface import ICategoryController
from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
from src.osm_configurator.model.project.configuration.category import Category


class CategoryControllerStub(ICategoryController):
    def check_conflicts_in_category_configuration(self, path: pathlib.Path) -> bool:
        pass

    def import_category_configuration(self, path: pathlib.Path) -> bool:
        pass

    def get_list_of_categories(self) -> list[Category]:
        pass

    def create_category(self) -> Category:
        pass

    def delete_category(self, category: Category) -> bool:
        pass

    def get_list_of_key_recommendations(self, current_input: str) -> list[str]:
        pass

    def get_attractivities_of_category(self, category: Category) -> list[AttractivityAttribute]:
        pass