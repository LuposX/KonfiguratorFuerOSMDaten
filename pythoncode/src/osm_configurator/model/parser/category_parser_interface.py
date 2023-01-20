import pathlib
import src.osm_configurator.model.project.configuration.category

from abc import ABC, abstractmethod


class CategoryParserInterface(ABC):
    """
    The CategoryParser job, is to parse the category file that are created when creating a project and
    make an internal representation out of it. 
    In the category file there are the different categories from the project defined, for more information about this
    look at the documentation of :obj:`~category.Category`.
    """
    @abstractmethod
    def parse_category_file(self, path):
        """Creates an internal representation of the category file it got as an input.
        What the Category includes, check this: :obj:`~category.Category`.

        Args:
            path (pathlib.Path): The path to the category file.
            
        Returns:
           list[category.Category]: A List of categories, that describe each category from the category file.
        """
        pass

