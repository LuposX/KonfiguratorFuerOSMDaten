from __future__ import annotations

import osmium as osm
import numpy as np

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Tuple
    from typing import Set
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

        # This will be the list in which we save the output.
        self._osm_data: List = []

        # this is a temporary list that is used to save the tags for one osm element.
        self._tmp_tag_list: List = []

        self._category_manager: CategoryManager = categories
        self._activated_attributes: List = activated_attributes

        # Get a list of tags that are needed, the rest we can throw away.
        self._needed_tags: Set
        for category in categories.get_categories():
            self._needed_tags.add(category.get_activated_attribute())

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
            # only save the tags if we need them later.
            if tag.k in self._needed_tags:
                self._tmp_tag_list.append((tag.k, tag.v))

        # save the osm object data that we need.
        self._osm_data.append([elem_type,
                               len(self._tmp_tag_list),
                               np.asarray(self._tmp_tag_list, dtype=str),
                               np.asarray(categories_of_osm_element, dtype=np.uint16)])

    def _get_list_of_categories_of_the_osm_element(self, n: OSMObject) -> List[str]:
        """
        This class checks for a specific osm_element which categories apply to it.

        Args:
            n (OSMObject): The  osm object which we want to check.

        Returns:
            List[str]: A list of categories that apply to the osm element.
        """
        _categories_of_osm_element = []

        # check if the osm_element applies to a category.
        _category: Category
        for _category in self._category_manager.get_categories():
            _category_name = _category.get_category_name()
            _whitelist = _category.get_whitelist()
            _blacklist = _category.get_whitelist()

            # check if the node adheres to the whitelist.
            _all_tags_from_whitelist_correct: bool = True
            _tag_in_whitelist: Tuple
            for _tag_in_whitelist in _whitelist:

                # If we find a single tag from the whitelist which the node doesn't correctly have, don't add category.
                if n.tags.get(_tag_in_whitelist[0]) != _tag_in_whitelist[1]:
                    _all_tags_from_whitelist_correct = False
                    break

            # Only when the whitelist is correct do we need to check the blacklist.
            if _all_tags_from_whitelist_correct:

                # check if the node adheres to the blacklist.
                _all_tags_from_blacklist_correct: bool = True
                _tag_in_blacklist: Tuple
                for _tag_in_blacklist in _blacklist:

                    # If we find a single tag from the blacklist which the node doesn't adhere to,
                    # then the category doesn't apply to the osm_element.
                    if n.tags.get(_tag_in_blacklist[0]) == _tag_in_blacklist[1]:
                        _all_tags_from_whitelist_correct = False
                        break

            if _all_tags_from_whitelist_correct:
                _categories_of_osm_element.append(_category_name)

        return _categories_of_osm_element

    def node(self, n: Node) -> None:
        """
        This method gets called when reading the osm data file a node was found.

        Args:
            n (Node): The node we found
        """
        # Get all the categories that apply to the current osm element
        _categories_of_osm_element = self._get_list_of_categories_of_the_osm_element(n)

        # check that the categories aren't empty
        if _categories_of_osm_element:
            self._tag_inventory(n, "node", _categories_of_osm_element)

        del n

    def way(self, w: Way) -> None:
        """
        This method gets called when reading the osm data file a way was found.

        Args:
            w (Way): The way we found.
        """
        # Get all the categories that apply to the current osm element
        _categories_of_osm_element = self._get_list_of_categories_of_the_osm_element(w)

        # check that the categories aren't empty
        if _categories_of_osm_element:
            self._tag_inventory(w, "way", _categories_of_osm_element)

        del w

    def relation(self, r: Relation) -> None:
        """
        This method gets called when reading the osm data file a node was found.

        Args:
            r (Relation): The node we found
        """
        # Get all the categories that apply to the current osm element
        _categories_of_osm_element = self._get_list_of_categories_of_the_osm_element(r)

        # check that the categories aren't empty
        if _categories_of_osm_element:
            self._tag_inventory(r, "relation", _categories_of_osm_element)

        del r

    def get_osm_data(self):
        """
        Getter for the osm data.

        Returns:
            List: A list of osm Data
        """
        return self._osm_data
