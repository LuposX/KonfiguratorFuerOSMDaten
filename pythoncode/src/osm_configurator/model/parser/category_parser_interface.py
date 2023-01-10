from abc import ABC, abstractmethod
import pathlib
import src.osm_configurator.model.project.configuration.category


class CategoryParserInterface(ABC):
    """
    The CategoryParser job, is to parse the category file that are created when creating a project and
    make an internal representation out of it. 
    In the category file there are the different categories from the project defined, for more look at the 
    documentation of :obj:`~category.Category`.
    """
    @abstractmethod
    def parse_category_file(self, path):
        """Creates an internal representation of the category file it go inputed.
        For what the Category includes check this: :obj:`~category.Category`.

        Args:
            path (pathlib.Path): the path to the category file.
            
        Returns:
           list[category.Category]: A List of categories, that describe each category from the category file.
        """
        pass

