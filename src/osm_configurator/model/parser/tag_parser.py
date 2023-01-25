from __future__ import annotations

from typing import List

from src.osm_configurator.model.parser.tag_parser_interface import TagParserInterface


class TagParser(TagParserInterface):
    __doc__ = TagParserInterface.__doc__

    def __init__(self):
        """
        Creates a new instance of the TagParser.
        """
        pass

    def parse_tags(self, tags: List[str]):
        pass
