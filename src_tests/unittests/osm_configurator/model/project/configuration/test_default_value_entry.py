from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry


class TestDefaultValueEntry:
    def test_get_default_value_entry_tag(self):
        self.default_value_entry: DefaultValueEntry = DefaultValueEntry("TestName")
        assert self.default_value_entry.get_default_value_entry_tag() == "TestName"

    def test_set_tag(self):
        self.default_value_entry: DefaultValueEntry = DefaultValueEntry("TestName")
        self.default_value_entry.set_tag("NewName")
        assert self.default_value_entry.get_default_value_entry_tag() == "NewName"

    def test_set_tag_error(self):
        self.default_value_entry: DefaultValueEntry = DefaultValueEntry("TestName")
        assert not self.default_value_entry.set_tag("")

    def test_get_attribute_default(self):
        self.default_value_entry: DefaultValueEntry = DefaultValueEntry("TestName")
        assert self.default_value_entry.get_attribute_default(Attribute.PROPERTY_AREA) == 0.0
        assert self.default_value_entry.get_attribute_default(Attribute.NUMBER_OF_FLOOR) == 0.0
        assert self.default_value_entry.get_attribute_default(Attribute.FLOOR_AREA) == 0.0

    def test_set_attribute_default(self):
        self.default_value_entry: DefaultValueEntry = DefaultValueEntry("TestName")
        self.default_value_entry.set_attribute_default(Attribute.PROPERTY_AREA, 15.0)
        self.default_value_entry.set_attribute_default(Attribute.NUMBER_OF_FLOOR, 2.0)
        self.default_value_entry.set_attribute_default(Attribute.FLOOR_AREA, 3.0)
        assert self.default_value_entry.get_attribute_default(Attribute.PROPERTY_AREA) == 15.0
        assert self.default_value_entry.get_attribute_default(Attribute.NUMBER_OF_FLOOR) == 2.0
        assert self.default_value_entry.get_attribute_default(Attribute.FLOOR_AREA) == 3.0
