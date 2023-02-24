from __future__ import annotations

from typing import List

from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute


class TestAttractivityAttribute:
    def test_get_attractivity_attribute_name(self):
        self.attractivity_attribute: AttractivityAttribute = AttractivityAttribute("TestAttribute")
        assert self.attractivity_attribute.get_attractivity_attribute_name() == "TestAttribute"

    def test_set_attractivity_attribute_name(self):
        self.attractivity_attribute: AttractivityAttribute = AttractivityAttribute("TestAttribute")
        self.attractivity_attribute.set_attractivity_attribute_name("NewName")
        assert self.attractivity_attribute.get_attractivity_attribute_name() == "NewName"

    def test_get_attribute_factor(self):
        self.attractivity_attribute: AttractivityAttribute = AttractivityAttribute("TestAttribute")
        assert self.attractivity_attribute.get_attribute_factor(Attribute.PROPERTY_AREA) == 0.0
        assert self.attractivity_attribute.get_attribute_factor(Attribute.NUMBER_OF_FLOOR) == 0.0
        assert self.attractivity_attribute.get_attribute_factor(Attribute.FLOOR_AREA) == 0.0

    def test_set_attribute_factor(self):
        self.attractivity_attribute: AttractivityAttribute = AttractivityAttribute("TestAttribute")
        self.attractivity_attribute.set_attribute_factor(Attribute.PROPERTY_AREA, 15.0)
        self.attractivity_attribute.set_attribute_factor(Attribute.NUMBER_OF_FLOOR, 2.0)
        self.attractivity_attribute.set_attribute_factor(Attribute.FLOOR_AREA, 3.0)
        assert self.attractivity_attribute.get_attribute_factor(Attribute.PROPERTY_AREA) == 15.0
        assert self.attractivity_attribute.get_attribute_factor(Attribute.NUMBER_OF_FLOOR) == 2.0
        assert self.attractivity_attribute.get_attribute_factor(Attribute.FLOOR_AREA) == 3.0

    def test_get_base_factor(self):
        self.attractivity_attribute: AttractivityAttribute = AttractivityAttribute("TestAttribute")
        assert self.attractivity_attribute.get_base_factor() == 0.0

    def test_get_base_factor(self):
        self.attractivity_attribute: AttractivityAttribute = AttractivityAttribute("TestAttribute")
        self.attractivity_attribute.set_base_factor(6.9)
        assert self.attractivity_attribute.get_base_factor() == 6.9
