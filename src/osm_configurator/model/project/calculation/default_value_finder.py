from __future__ import annotations

import src.osm_configurator.model.parser.tag_parser as tag_parser_i
import src.osm_configurator.model.model_constants as model_constants_i

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
    from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
    from src.osm_configurator.model.parser.tag_parser import TagParser
    from typing import Tuple, List, Dict


class DefaultValueFinder:
    def find_default_value_entry_which_applies(self, default_value_list: List[DefaultValueEntry],
                                                osm_element_tags: Dict[str, str]):
        """
        This method figures out the first default value entry in the List which applies to the osm element.
        Where applies means that the osm element hast the same key-value pair then the default-value-entry.
        The Default-value-list has a priority the lowest index is the most important, if that element doesnt apply
        we iterate further along the list until we find a default-value-entry which applies.

        Args:
            default_value_list (List): A list of default-value entries
            osm_element_tags (Dict[str, str]): A parsed dictionary of tags.
        """
        # Because circular-dependency issues is the import here.
        import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i
        import src.osm_configurator.model.project.configuration.default_value_entry as default_value_entry_i

        # Create a new Tag parser
        tag_parser_o: TagParser = tag_parser_i.TagParser()

        _default_value_entry: DefaultValueEntry
        for _default_value_entry in default_value_list:

            # check that the default value has even an entry
            default_tag: str = _default_value_entry.get_default_value_entry_tag()
            if not default_tag:
                continue

            # If its the default default tag
            if default_tag == model_constants_i.DEFAULT_DEFAULT_VALUE_ENTRY_TAG:
                return _default_value_entry

            # This will return a dictionary with a single entry which is our tag
            parsed_default_value_tag = tag_parser_o.parse_tags([default_tag])

            # Since the dictionary has only one entry we can get the key this way
            key_tag_default_value_entry = list(parsed_default_value_tag.keys())[0]
            value_tag_default_value_entry = parsed_default_value_tag.get(key_tag_default_value_entry)

            # gets set to true when osm element applies to default_value_list entry
            is_osm_element_in_default_value: bool = False

            # get the first value of every tuple entry, which is the key of the tag
            # if this true this means the key value of the default value is also in the osm tag list.
            if key_tag_default_value_entry in osm_element_tags.keys():
                # The don't care symbol is "*" if thats set the value of the osm element for this tag
                # doesn't interest us.
                if value_tag_default_value_entry == model_constants_i.DONT_CARE_SYMBOL:
                    is_osm_element_in_default_value = True

                elif value_tag_default_value_entry == osm_element_tags.get(key_tag_default_value_entry):
                    is_osm_element_in_default_value = True

            if is_osm_element_in_default_value:
                return _default_value_entry

        # TODO: THIS SHOULDNT BE HERE, BUT CONFIGURATION DIDNT IMPLEMENT THIS, SO I NEED TO DO THIS MYSELF
        default_default_value_entry: DefaultValueEntry = default_value_entry_i.DefaultValueEntry()
        if len(osm_element_tags) != 0:
            default_default_value_entry.set_tag(osm_element_tags.get(list(osm_element_tags.keys())[0]))

        for attribute in attribute_enum_i.Attribute:
            default_default_value_entry.set_attribute_default(attribute, 1)

        return default_default_value_entry