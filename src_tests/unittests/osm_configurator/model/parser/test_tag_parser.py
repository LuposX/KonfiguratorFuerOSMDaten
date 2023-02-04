import pytest

import src.osm_configurator.model.parser.tag_parser as tag_parser_i


class TestTagParser:
    def test_tag_parser_correctly(self):
        tag_parser = tag_parser_i.TagParser()

        tags_not_formatted = ["building=yes", "waterfall=yes", "building:level=5", "poop=900"]
        tags_formatted = {"building": "yes", "waterfall": "yes", "building:level": "5", "poop": "900"}

        assert tags_formatted == tag_parser.parse_tags(tags_not_formatted)

        tags_wrongly_formated = ["building=yes=popp"]

        with pytest.raises(Exception) as e:
            tag_parser.parse_tags(tags_wrongly_formated)

    def test_tag_parser_wrongly(self):
        tag_parser = tag_parser_i.TagParser()

        tags_wrongly_formated = ["building=yes=popp"]

        with pytest.raises(Exception) as e:
            tag_parser.parse_tags(tags_wrongly_formated)

    def teste_string_to_list(self):
        tag_parser = tag_parser_i.TagParser()

        tag1 = '["buildin:=yes", "building=no", "poop=384893_?$%ada", "building:level=298398_Ssfs90"]'
        tag2 = "['buildin:=yes', 'building=no', 'poop=384893_?$%ada', 'building:level=298398_Ssfs90']"
        tag3 = "['buildin:=yes']"
        tag4 = '[]'

        assert set(["buildin:=yes", "building=no", "poop=384893_?$%ada", "building:level=298398_Ssfs90"]) \
               == set(tag_parser.user_tag_parser(tag1))

        assert set(['buildin:=yes', 'building=no', 'poop=384893_?$%ada', 'building:level=298398_Ssfs90']) \
               == set(tag_parser.user_tag_parser(tag2))

        assert set(['buildin:=yes']) \
               == set(tag_parser.user_tag_parser(tag3))

        assert set([]) \
               == set(tag_parser.user_tag_parser(tag4))
