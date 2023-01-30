from __future__ import annotations

import osmium as osm
import shapely.wkb as wkb

import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i
import src.osm_configurator.model.model_constants as model_constants_i
import src.osm_configurator.model.parser.tag_parser as tag_parser_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
    from src.osm_configurator.model.project.configuration.category import Category
    from src.osm_configurator.model.parser.tag_parser import TagParser
    from typing import List, Tuple, Dict
    from osmium import Node  # type: ignore
    from osmium import Way  # type: ignore
    from osmium import Area  # type: ignore
    from osmium import Relation  # type: ignore
    from osmium.osm import OSMObject
    from shapely import Polygon
    from typing import Final

KEY_NOT_FOUND: str = "key_not_found"


class DataOSMHandler(osm.SimpleHandler):
    """
    This class is responsible for parsing osm data files into a dataframe format.
    """

    def __init__(self, category_manager_p: CategoryManager, cut_out_data_p: Polygon = None):
        """
        Creates a new "DataOSMHandler" object.

        Args:
            category_manager_p (CategoryManager): Needed to check if an osm object belongs to a specific category.
            cut_out_data_p (Polygon): This is a polygon which describe the border of the traffic cell.
        """
        osm.SimpleHandler.__init__(self)

        # This will be the list in which we save the output.
        self._osm_type = None
        self._osm_data: List = []

        self._category_manager: CategoryManager = category_manager_p

        # Get a list of tags that are needed, the rest we can throw away.
        self._needed_tags: List[str] = attribute_enum_i.Attribute.get_all_tags()

        # when cut_out_data is set we need to remove building which are on the edge
        self._cut_out_data: Polygon
        if cut_out_data_p is None:
            self._remove_building_on_edge = False
        else:
            self._remove_building_on_edge = True
            self._cut_out_data = cut_out_data_p

        self._wkbfab = osm.geom.WKBFactory()  # with this we create geometries for areas
        self._shapely_location = 0  # the location we save per osm element
        self._tmp_tag_list: List[
            str] = []  # this is a temporary list that is used to save the tags for one osm element.
        self._categories_of_osm_element: List[str] = []
        self._wkbshape = None  # used to temporarily save location
        self._osm_type: str  # saved the origin name for area(e.g. way or relation)
        self._osm_name: str

    def _attributes_to_tag_list(self) -> List[str]:
        """
        This method is used to extract all the tags that are needed for the calculation from the Attributes.

        Returns:
            List: Of tag names(keys) that the attributes needs.
        """
        _needed_tags: List[str] = []
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
        # we have one row of the osm element for each category the osm element applies to
        for category in self._categories_of_osm_element:
            self._osm_data.append([self._osm_type,
                                   self._osm_name,
                                   self._shapely_location,
                                   self._tmp_tag_list,
                                   category])

    def _get_list_of_categories_of_the_osm_element(self, osm_object: OSMObject) -> List[str]:
        """
        This class checks for a specific osm_element which categories apply to it.

        Args:
            osm_object (OSMObject): The  osm object which we want to check.

        Returns:
            List[str]: A list of categories that apply to the osm element.

        Raises:
            TagsWronglyFormatted: If a tag wasn't correctly formatted.
        """
        categories_of_osm_element: List[Category] = []

        tag_parser: TagParser = tag_parser_i.TagParser()

        # check if the osm_element applies to a category.
        category: Category
        for category in self._category_manager.get_categories():
            category_name: str = category.get_category_name()
            whitelist: Dict = category.get_whitelist()
            blacklist: Dict = category.get_blacklist()

            # parse the tags from List[str] to List[Tuple[str, str]]
            whitelist_parsed = tag_parser.parse_tags(whitelist)
            blacklist_parsed = tag_parser.parse_tags(blacklist)

            # check if the node adheres to the whitelist.
            all_tags_from_whitelist_correct: bool = True
            tag_in_whitelist: Tuple
            for key_tag, value_tag in whitelist_parsed.items():

                # Checks if the key is in the osm element
                if osm_object.tags.get(key_tag, KEY_NOT_FOUND) \
                        != KEY_NOT_FOUND:
                    # "*"
                    # The-don't-care symbol, says it doesn't matter what the value of the tag is.
                    if value_tag != model_constants_i.DONT_CARE_SYMBOL:
                        # If we find a single tag from the whitelist which the node doesn't correctly have
                        # don't add category.
                        if osm_object.tags.get(key_tag, KEY_NOT_FOUND) != value_tag:
                            all_tags_from_whitelist_correct = False
                            break

                # if the key wasn't in the osm_element
                else:
                    all_tags_from_whitelist_correct = False
                    break

            # check if the node adheres to the blacklist.
            all_tags_from_blacklist_correct: bool = True
            tag_in_blacklist: Tuple
            for key_tag, value_tag in blacklist_parsed.items():

                # Checks if the key is in the osm element
                # if the key isn't in the osm element, then we know that this tag is correct for the osm element
                if osm_object.tags.get(key_tag, KEY_NOT_FOUND) \
                        != KEY_NOT_FOUND:

                    # If we find a single tag from the blacklist which the node doesn't adhere to,
                    # then the category doesn't apply to the osm_element.
                    if value_tag != model_constants_i.DONT_CARE_SYMBOL:
                        if osm_object.tags.get(key_tag, KEY_NOT_FOUND) == value_tag:
                            all_tags_from_blacklist_correct = False
                            break

                    # if we have the don't-care symbol, it doesn't matter what the value of the osm element for
                    # this tag is, the osm element won't be added no matter what.
                    else:
                        all_tags_from_blacklist_correct = False
                        break

            if all_tags_from_whitelist_correct and all_tags_from_blacklist_correct:
                categories_of_osm_element.append(category_name)

        return categories_of_osm_element

    def node(self, n: Node) -> None:
        """
        This method gets called when reading the osm data file a node was found.

        Args:
            n (Node): The node we found

        Raises:
            TagsWronglyFormatted: If a tag wasn't correctly formatted.
        """
        self._shapely_location = None
        self._osm_type = model_constants_i.NODE_NAME
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

        Raises:
            TagsWronglyFormatted: If a tag wasn't correctly formatted.
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
                self._osm_type = model_constants_i.AREA_WAY_NAME
            else:
                self._osm_type = model_constants_i.AREA_RELATION_NAME

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
