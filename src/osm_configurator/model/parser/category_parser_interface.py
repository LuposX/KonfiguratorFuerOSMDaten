from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
    from src.osm_configurator.model.project.configuration.category import Category


class CategoryParserInterface(ABC):
    """
    The CategoryParser job, is to parse the category file that are created when creating a project and
    make an internal representation out of it.
    In the category file there are the different categories from the project defined, for more information about this
    look at the documentation of :obj:`~category.Category`.
    """
    @abstractmethod
    def parse_category_file(self, path: Path) -> Category:
        """Creates an internal representation of the category file it got as an input.
        What the Category includes, check this: :obj:`~category.Category`.

        Args:
            path (Path): The path to the category file.
            
        Returns:
           category.Category: A category.
        """

