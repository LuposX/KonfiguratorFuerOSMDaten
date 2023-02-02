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

            if len(split_string) != 2:
                raise TagsWronglyFormatted(str(tag))

            parsed_tags.update({split_string[0]: split_string[1]})

        return parsed_tags

    def string_to_list_parser(self, string: str) -> List[str]:
        """
        This method parses a string representation of a list to an actual list.
        """
        tmp_str: str = re.sub(r'["\[\]\']', '', string)
        tmp_str: str = tmp_str.split(",")

        # remove trailing whitespaces
        tmp_str = [x.strip(' ') for x in tmp_str]

        if len(tmp_str) != 0:
            return list(filter(None, tmp_str))
        else:
            return []
