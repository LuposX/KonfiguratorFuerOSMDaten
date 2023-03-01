import pytest

import src.osm_configurator.model.parser.tag_parser as tag_parser_i


class TestTagParser:
    def test_user_tag_parser_correctly(self):
        tag_parser = tag_parser_i.TagParser()

        tags_not_formatted = ["building=yes", "waterfall=yes", "building:level=5", "poop=900"]
        tags_formatted = {"building": "yes", "waterfall": "yes", "building:level": "5", "poop": "900"}

        assert tags_formatted == tag_parser.parse_tags(tags_not_formatted)

        tags_wrongly_formated = ["building=yes=popp"]

        with pytest.raises(Exception):
            tag_parser.parse_tags(tags_wrongly_formated)

    def test_tag_parser_wrongly(self):
        tag_parser = tag_parser_i.TagParser()

        tags_wrongly_formated = ["building=yes=popp"]

        with pytest.raises(Exception):
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

    def test_tag_dataframe_parser_correctly(self):
        tag_parser = tag_parser_i.TagParser()

        tag1 = "[('addr:country', 'MC'), ('building', 'terrace'), ('building:levels', '8'), ('name', 'Les Eucalyptus')]"
        tag2 = "[('area', 'yes'), ('building', 'yes'), ('building:levels', '1'), ('highway', 'footway'), ('roof:shape', 'flat')]"
        tag3 = "[('area', 'yes')]"
        tag4 = "[]"

        tag1_formatted = [('addr:country', 'MC'), ('building', 'terrace'), ('building:levels', '8'),
                          ('name', 'Les Eucalyptus')]
        tag2_formatted = [('area', 'yes'), ('building', 'yes'),
                          ('building:levels', '1'),
                          ('highway', 'footway'),
                          ('roof:shape', 'flat')]
        tag3_formatted = [('area', 'yes')]
        tag4_formatted = []

        assert set(tag1_formatted) \
               == set(tag_parser.dataframe_tag_parser(tag1))

        assert set(tag2_formatted) \
               == set(tag_parser.dataframe_tag_parser(tag2))

        assert set(tag3_formatted) \
               == set(tag_parser.dataframe_tag_parser(tag3))

        assert set(tag4_formatted) \
               == set(tag_parser.dataframe_tag_parser(tag4))
