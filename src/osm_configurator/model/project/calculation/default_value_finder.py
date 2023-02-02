from __future__ import annotations

import src.osm_configurator.model.parser.tag_parser as tag_parser_i
import src.osm_configurator.model.model_constants as model_constants_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
    from src.osm_configurator.model.parser.tag_parser import TagParser
    from typing import Tuple, List, Dict


class DefaultValueFinder:
    def find_default_value_entry_which_applies(self, default_value_list: List[DefaultValueEntry],
                                                osm_element_tags: List[str]):
        """
        This method figures out the first default value entry in the List which applies to the osm element.
        Where applies means that the osm element hast the same key-value pair then the default-value-entry.
        The Default-value-list has a priority the lowest index is the most important, if that element doesnt apply
        we iterate further along the list until we find a default-value-entry which applies.

        Args:
            default_value_list (List): A list of default-value entries
            osm_element_tags (List[str]): A list of unparsed tags of the osm element.
        """
        # Create a new Tag parser
        tag_parser_o: TagParser = tag_parser_i.TagParser()

        # These are the parsed tags from the osm element
        parsed_osm_element_tag_list = tag_parser_o.parse_tags(osm_element_tags)

        _default_value_entry: DefaultValueEntry
        for _default_value_entry in default_value_list:
            # This will return a dictionary with a single entry which is our tag
            parsed_default_value_tag = tag_parser_o.parse_tags(
                [_default_value_entry.get_default_value_entry_tag()])

            # Since teh dictionary has only one entry we can get the key this way
            key_tag_default_value_entry = parsed_default_value_tag.keys()[0]
            value_tag_default_value_entry = parsed_default_value_tag.get(key_tag_default_value_entry)

            # gets set to true when osm element applies to default_value_list entry
            is_osm_element_in_default_value: bool = False

            # get the first value of every tuple entry, which is the key of the tag
            # if this true this means the key value of the default value is also in the osm tag list.
            if key_tag_default_value_entry in parsed_osm_element_tag_list.keys():
                # The don't care symbol is "*" if thats set the value of the osm element for this tag
                # doesn't interest us.
                if value_tag_default_value_entry == model_constants_i.DONT_CARE_SYMBOL:
                    is_osm_element_in_default_value = True

                elif value_tag_default_value_entry == parsed_osm_element_tag_list.get(key_tag_default_value_entry):
                    is_osm_element_in_default_value = True

            if is_osm_element_in_default_value:
                return _default_value_entry

        return None