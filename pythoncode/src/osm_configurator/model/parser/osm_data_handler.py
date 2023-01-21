from __future__ import annotations

import osmium as osm
import numpy as np

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.configuration.category import Category
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from osmium import Node
    from osmium import Way
    from osmium import Relation
    from osmium.osm import OSMObject


class DataOSMHandler(osm.SimpleHandler):
    """
    This class is responsible for parsing osm data files into a dataframe format.
    """

    def __init__(self, categories: CategoryManager, activated_attributes: List[Attribute]):
        """
        Creates a new "DataOSMHandler" object.

        Args:
            categories (CategoryManager): Needed to check if an osm object belongs to a specific category.
            activated_attributes (List[Attribute]): Used to know which tags we want to save.
        """
        osm.SimpleHandler.__init__(self)

        # This will be the list in which we save the output
        self._osm_data: List = []

        # this is a temporary list that is used to save the tags for one osm element
        self._tmp_tag_list: List = []

        self._category_manager: CategoryManager = categories
        self._activated_attributes: List = activated_attributes

        # Get a list of tags that are needed, the rest we can throw away
        self._needed_tags: List = self._attributes_to_tag_list()

    def _attributes_to_tag_list(self) -> List:
        """
        This method is used to extract all the tags that are needed for the calculation from the Attributes.

        Returns:
            List: Of tag names(keys) that the attributes needs.
        """
        _needed_tags: List = []
        for attribute in self._activated_attributes:
            _needed_tags.extend(attribute.get_needed_tags())
        return _needed_tags

    def _tag_inventory(self, elem: OSMObject, elem_type: str, categories_of_osm_element) -> None:
        """
        This method is responsible to save the information about the osm elements.

        Args:
            elem (OSMObject): The osm element we want to save.
            elem_type (str): The type of the element we got passed as string.
            categories_of_osm_element: List: A list of categories the osm element belongs to.
        """
        # Get a temporary list of tags from the osm object.
        self._tmp_tag_list: List = []
        for tag in elem.tags:
            # only save the tags if we need them later
            if tag.k in self._needed_tags:
                self._tmp_tag_list.append((tag.k, tag.v))

        # save the osm object data that we need
        self._osm_data.append([elem_type,
                               len(self._tmp_tag_list),
                               np.asarray(self._tmp_tag_list, dtype=str),
                               np.asarray(categories_of_osm_element, dtype=np.uint16)])

    def node(self, n: Node) -> None:
        """
        This method gets called when reading the osm data file a node was found.

        Args:
            n (Node): The node we found
        """
        categories_of_osm_element: List = []

        # check if the osm_element applies to a category
        _category: Category
        for _category in self._category_manager.get_categories():
            _name = _category.get_category_name()
            _whitelist = _category.get_whitelist()
            _blacklist = _category.get_whitelist()

            if n.tags.get(whitelist[0]) == whitelist[1]:
                categories_of_osm_element.append(name)

        if categories_of_osm_element:
            self._tag_inventory(n, "node", categories_of_osm_element)

        del n

    def way(self, w: Way) -> None:
        """
          This method gets called when reading the osm data file a way was found.

          Args:
              w (Way): The way we found.
          """
        categories_of_osm_element = []

        # check if the osm_element applies to a category
        for category in self.category_whitelist:
            name = category[0]
            whitelist = category[1]

            if w.tags.get(whitelist[0]) == whitelist[1]:
                categories_of_osm_element.append(name)

        if categories_of_osm_element:
            self._tag_inventory(w, "way", categories_of_osm_element)

    def relation(self, r: Relation) -> None:
        """
        This method gets called when reading the osm data file a node was found.

        Args:
            r (Relation): The node we found
        """
        # It's really hard to get the location out of relations
        categories_of_osm_element = []

        # check if the osm_element applies to a category
        for category in self.category_whitelist:
            name = category[0]
            whitelist = category[1]

            if r.tags.get(whitelist[0]) == whitelist[1]:
                categories_of_osm_element.append(name)

        if categories_of_osm_element:
            self._tag_inventory(r, "relation", categories_of_osm_element)
