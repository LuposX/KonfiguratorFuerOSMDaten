from __future__ import annotations

import src.osm_configurator.model.project.configuration.category as category_i
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.category import Category

BUILDING_CATEGORY_NAME: str = "Gebäude"
BUIlDING_CATEGORY_WHITELIST: str = "building=*"


def create_building_category() -> Category:
    """
    This method creates the default category named "building".

    Returns:
        The created Category.
    """
    building_category: Category = category_i.Category(BUILDING_CATEGORY_NAME)
    white_list: list[str] = [BUIlDING_CATEGORY_WHITELIST]
    building_category.set_whitelist(white_list)
    return building_category


class DefaultCategories:
    """
    This class is to creat some default categories.
    """
