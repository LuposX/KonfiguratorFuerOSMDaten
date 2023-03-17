from __future__ import annotations

from src.osm_configurator.model.project.calculation.default_value_finder import find_default_value_entry_which_applies
from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List


class TestDefaultFinder:
    def test_default_finder_valid_simple(self):
        default_value_list: List[DefaultValueEntry] = []

        default_value_entry: DefaultValueEntry = DefaultValueEntry("building=true")

        default_value_list.append(default_value_entry)

        found_default_value: DefaultValueEntry = \
            find_default_value_entry_which_applies(default_value_list, {"building": "true"})

        assert found_default_value.get_default_value_entry_tag() == "building=true"

    def test_default_finder_valid_multiple(self):
        default_value_list: List[DefaultValueEntry] = []

        default_value_entry1: DefaultValueEntry = DefaultValueEntry("building=*")
        default_value_entry2: DefaultValueEntry = DefaultValueEntry("house=true")
        default_value_entry3: DefaultValueEntry = DefaultValueEntry("neco_arc=*")
        default_value_entry4: DefaultValueEntry = DefaultValueEntry("monke_man=*")
        default_value_entry4.set_attribute_default(Attribute.NUMBER_OF_FLOOR, 100)
        default_value_entry4.set_attribute_default(Attribute.FLOOR_AREA, 100)
        default_value_entry5: DefaultValueEntry = DefaultValueEntry("tohou:cirno=lol")

        default_value_list.append(default_value_entry5)
        default_value_list.append(default_value_entry4)
        default_value_list.append(default_value_entry3)
        default_value_list.append(default_value_entry2)
        default_value_list.append(default_value_entry1)

        found_default_value: DefaultValueEntry = \
            find_default_value_entry_which_applies(
                default_value_list,
                {"building": "true", "neco_arc": "*", "monke_man": "test"}
        )

        assert found_default_value.get_default_value_entry_tag() == "monke_man=*"
        assert found_default_value.get_attribute_default(Attribute.NUMBER_OF_FLOOR) == 100
        assert found_default_value.get_attribute_default(Attribute.FLOOR_AREA) == 100
        assert found_default_value.get_attribute_default(Attribute.PROPERTY_AREA) == 0

    def test_default_finder_invalid(self):
        default_value_list: List[DefaultValueEntry] = []

        default_value_entry: DefaultValueEntry = DefaultValueEntry("")

        default_value_list.append(default_value_entry)

        found_default_value: DefaultValueEntry = \
            find_default_value_entry_which_applies(default_value_list, {"building": "true"})

        assert found_default_value is None

    def test_default_finder_invalid_2(self):
        default_value_list: List[DefaultValueEntry] = []

        default_value_entry: DefaultValueEntry = DefaultValueEntry("landside=true")

        default_value_list.append(default_value_entry)

        found_default_value: DefaultValueEntry = \
            find_default_value_entry_which_applies(default_value_list, {"building": "true"})

        assert found_default_value is None
