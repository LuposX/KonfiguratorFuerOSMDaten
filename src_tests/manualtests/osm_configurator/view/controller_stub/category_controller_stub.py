import pathlib
from typing import List

from src.osm_configurator.control.category_controller_interface import ICategoryController
from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
import src.osm_configurator.model.project.configuration.category as c


class CategoryControllerStub(ICategoryController):
    def check_conflicts_in_category_configuration(self, path: pathlib.Path) -> bool:
        """
        Returns:
            bool: True, if the path exists, else false
        """
        return path.exists()

    def import_category_configuration(self, path: pathlib.Path) -> bool:
        return True

    def get_list_of_categories(self) -> List[c.Category]:
        shit = c.Category("hello")
        shit.set_whitelist(["EINS EINRAG"])
        shit.set_blacklist(["AUCH EINS EINTRAG"])
        return [shit]

    def create_category(self, name: str) -> c.Category:
        category = c.Category(name)
        return category

    def delete_category(self, category: c.Category) -> bool:
        return True

    def get_list_of_key_recommendations(self, current_input: str) -> List[str]:
        return []

    def get_attractivities_of_category(self, category: c.Category) -> List[AttractivityAttribute]:
        return []