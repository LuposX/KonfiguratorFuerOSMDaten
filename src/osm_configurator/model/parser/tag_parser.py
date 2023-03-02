from __future__ import annotations

from src.osm_configurator.model.parser.tag_parser_interface import TagParserInterface
from src.osm_configurator.model.parser.custom_exceptions.tags_wrongly_formatted_exception import TagsWronglyFormatted

import re

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Dict, Tuple


class TagParser(TagParserInterface):
    __doc__ = TagParserInterface.__doc__

    def __init__(self):
        """
        Creates a new instance of the TagParser.
        """
        pass

    def parse_tags(self, tags: List[str]) -> Dict[str, str]:
        if not tags:
            return {}

        parsed_tags: Dict[str, str] = {}
        tag: str
        for tag in tags:
            split_string = tag.split("=")

            if '' not in split_string:
                if len(split_string) != 2:
                    raise TagsWronglyFormatted(str(tag))

                parsed_tags.update({split_string[0]: split_string[1]})

        return parsed_tags

    @staticmethod
    def user_tag_parser(string: str) -> List[str]:
        """
        This method parses a string representation of a list to an actual list.
        These methods gets used to parse the input the string from the GUI.
        e.g. format '["building=yes", "pooop=funny_Cat"]'
        """
        tmp_str: str = re.sub(r'["\[\]\']', '', string)
        tmp_str_split: List[str] = tmp_str.split(",")

        # remove trailing whitespaces
        tmp_str_finish: List[str] = [x.strip(' ') for x in tmp_str_split]

        if len(tmp_str_finish) != 0:
            return list(filter(None, tmp_str_finish))
        else:
            return []

    @staticmethod
    def dataframe_tag_parser(string: str) -> List[Tuple[str, str]]:
        """
        This method parses a string representation of a list to an actual list.
        This method is used to parse teh tags from the dataframe file.
        The input format is in the form:
        e.g. "[('addr:country', 'MC'), ('building', 'terrace'), ('building:levels', '8')]"
        """
        return eval(string)

    @staticmethod
    def list_to_dict(string: List[Tuple[str, str]]) -> Dict[str, str]:
        """
        This function is used to convert a list of tuples into a dictionary.
        """
        return dict(string)
