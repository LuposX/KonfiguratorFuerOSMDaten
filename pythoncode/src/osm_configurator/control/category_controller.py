from src.osm_configurator.control.category_controller_interface import ICategoryController
import pathlib

from typing import TYPE_CHECKING

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
        pass

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
