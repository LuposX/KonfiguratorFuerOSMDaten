from __future__ import annotations

from src.osm_configurator.model.parser.tag_parser_interface import TagParserInterface
import src.osm_configurator.model.parser.custom_exceptions.tags_wrongly_formatted_exception as tags_wrongly_formatted_exception_i


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from typing import Tuple


class TagParser(TagParserInterface):
    __doc__ = TagParserInterface.__doc__

    def __init__(self):
        """
        Creates a new instance of the TagParser.
        """
        pass

    def parse_tags(self, tags: List[str]) -> List[Tuple[str, str]]:

        parsed_tags: List[Tuple[str, str]] = []
        tag: str
        for tag in tags:
            split_string = tag.split("=")

            if len(split_string) != 2:
                raise tags_wrongly_formatted_exception_i.TagsWronglyFormatted(str(tag))

            parsed_tags.append((split_string[0], split_string[1]))

        return parsed_tags
