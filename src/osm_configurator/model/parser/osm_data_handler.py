from __future__ import annotations

import osmium as osm
import numpy as np
import shapely.wkb as wkb

import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum
import osm_configurator.model.model_constants as model_constants_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Tuple
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.configuration.category import Category
    from osmium import Node
    from osmium import Way
    from osmium import Area
    from osmium import Relation
    from osmium.osm import OSMObject
    from shapely import Polygon
    from typing import Final



class DataOSMHandler(osm.SimpleHandler):
    """
    This class is responsible for parsing osm data files into a dataframe format.
    """

    KEY_NOT_FOUND: str = "key_not_found"

    def __init__(self, category_manager_p: CategoryManager, cut_out_data_p: Polygon = None):
        """
        Creates a new "DataOSMHandler" object.

        Args:
            category_manager_p (CategoryManager): Needed to check if an osm object belongs to a specific category.
            cut_out_data_p (Polygon): This is a polygon which describe the border of the traffic cell.
        """
        osm.SimpleHandler.__init__(self)

        # This will be the list in which we save the output.
        self._osm_data: List = []

        # this is a temporary list that is used to save the tags for one osm element.
        self._tmp_tag_list: List = []

        self._category_manager: CategoryManager = category_manager_p

        # Get a list of tags that are needed, the rest we can throw away.
        self._needed_tags: List = attribute_enum.Attribute.get_all_tags()

        # when cut_out_data is set we need to remove building which are on the edge
        self._cut_out_data: Polygon
        if cut_out_data_p is None:
            self._remove_building_on_edge = False
        else:
            self._remove_building_on_edge = True
            self._cut_out_data = cut_out_data_p

        self._wkbfab = osm.geom.WKBFactory()  # with this we create geometries for areas
        self._shapely_location = 0  # the location we save per osm element
        self._tmp_tag_list: List = []  # this is a temporary list that is used to save the tags for one osm element.
        self._categories_of_osm_element = []
        self._wkbshape = None  # used to temporarily save location
        self._osm_type: str # saved the origin name for area(e.g. way or relation)
        self._osm_name: str

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

    def _tag_inventory(self, elem: OSMObject) -> None:
        """
        This method is responsible to save the information about the osm elements.

        Args:
            elem (OSMObject): The osm element we want to save.
        """
        # Get a temporary list of tags from the osm object.
        self._tmp_tag_list: List = []
        for tag in elem.tags:
            # only save the tags if we need them later.
            if tag.k in self._needed_tags:
                self._tmp_tag_list.append((tag.k, tag.v))

        # save the osm object data that we need.
        self._osm_data.append([self._osm_type,
                               self._osm_name,
                               self._shapely_location,
                               np.asarray(self._tmp_tag_list, dtype=str),
                               np.asarray(self._categories_of_osm_element, dtype=str)])

    def _get_list_of_categories_of_the_osm_element(self, osm_object: OSMObject) -> List[str]:
        """
        This class checks for a specific osm_element which categories apply to it.

        Args:
            osm_object (OSMObject): The  osm object which we want to check.

        Returns:
            List[str]: A list of categories that apply to the osm element.
        """
        categories_of_osm_element: List[Category] = []

        # check if the osm_element applies to a category.
        category: Category
        for category in self._category_manager.get_categories():
            category_name: str = category.get_category_name()
            whitelist: List = category.get_whitelist()
            blacklist: List = category.get_whitelist()

            # check if the node adheres to the whitelist.
            all_tags_from_whitelist_correct: bool = True
            tag_in_whitelist: Tuple
            for tag_in_whitelist in whitelist:

                # Checks if the key is in the osm element
                if osm_object.tags.get(tag_in_whitelist[0], DataOSMHandler.KEY_NOT_FOUND) \
                        != DataOSMHandler.KEY_NOT_FOUND:

                    # The dont care symbols, says it doesn't matter what the value of the tag is.
                    if tag_in_whitelist[1] == model_constants_i.DONT_CARE_SYMBOL:
                        break
                    else:
                        # If we find a single tag from the whitelist which the node doesn't correctly have, don't add category.
                        if osm_object.tags.get(tag_in_whitelist[0], DataOSMHandler.KEY_NOT_FOUND) != tag_in_whitelist[1]:
                            all_tags_from_whitelist_correct = False
                            break

                # if the key wasn't in the osm_element
                else:
                    all_tags_from_whitelist_correct = False
                    break


            # Only when the whitelist is correct do we need to check the blacklist.
            if all_tags_from_whitelist_correct:

                # check if the node adheres to the blacklist.
                all_tags_from_blacklist_correct: bool = True
                tag_in_blacklist: Tuple
                for tag_in_blacklist in blacklist:

                    # Checks if the key is in the osm element
                    # if the key isn't in the osm element, then we know that this tag is correct for the osm element
                    if osm_object.tags.get(tag_in_blacklist[0], DataOSMHandler.KEY_NOT_FOUND) \
                            != DataOSMHandler.KEY_NOT_FOUND:

                        # If we find a single tag from the blacklist which the node doesn't adhere to,
                        # then the category doesn't apply to the osm_element.
                        if tag_in_blacklist[1] != model_constants_i.DONT_CARE_SYMBOL:
                            if osm_object.tags.get(tag_in_blacklist[0], DataOSMHandler.KEY_NOT_FOUND) == tag_in_blacklist[1]:
                                all_tags_from_blacklist_correct = False
                                break

                        # if we have the dont care symbol, it doesnt matter what the value of the osm element for
                        # this tag is, the osm element wont be added no matter what.
                        else:
                            all_tags_from_blacklist_correct = False
                            break

                    else:
                        all_tags_from_blacklist_correct = True

            if all_tags_from_whitelist_correct and all_tags_from_blacklist_correct:
                categories_of_osm_element.append(category_name)

        return categories_of_osm_element

    def node(self, n: Node) -> None:
        """
        This method gets called when reading the osm data file a node was found.

        Args:
            n (Node): The node we found
        """
        self._shapely_location = None
        self._osm_type = "node"
        self._osm_name = n.tags.get("name", model_constants_i.STANDARD_OSM_ELEMENT_NAME)

        # Get all the categories that apply to the current osm element
        self._categories_of_osm_element = self._get_list_of_categories_of_the_osm_element(n)

        # check that the categories aren't empty
        if self._categories_of_osm_element:

            # If building on the edge should be removed check whether the building is on the edge or not
            self._wkbshape = self._wkbfab.create_point(n)
            self._shapely_location = wkb.loads(self._wkbshape, hex=True)
            if self._remove_building_on_edge:
                if self._cut_out_data.contains(self._shapely_location):
                    self._tag_inventory(n)

            else:
                self._tag_inventory(n)

        del n

    def area(self, a: Area) -> None:
        """
        This method gets called when reading the osm data file an area was found.
        An Area is an OSMObject that is encircled, this means sth like a way or relation.

        Args:
            a (Area): The node we found
        """
        self._shapely_location = None
        self._osm_name = a.tags.get("name", model_constants_i.STANDARD_OSM_ELEMENT_NAME)

        # Get all the categories that apply to the current osm element
        self._categories_of_osm_element = self._get_list_of_categories_of_the_osm_element(a)

        # check that the categories aren't empty
        if self._categories_of_osm_element:
            # create location/multipolygon
            self._wkbshape = self._wkbfab.create_multipolygon(a)
            self._shapely_location = wkb.loads(self._wkbshape, hex=True)

            if a.from_way:
                self._osm_type = "area-way"
            else:
                self._osm_type = "area-relation"

            # If building on the edge should be removed check whether the building is on the edge or not
            if self._remove_building_on_edge:
                if self._cut_out_data.contains(self._shapely_location):
                    self._tag_inventory(a)

            else:
                self._tag_inventory(a)

        del a

    def get_osm_data(self):
        """
        Getter for the osm data.

        Returns:
            List: A list of osm Data
        """
        return self._osm_data
