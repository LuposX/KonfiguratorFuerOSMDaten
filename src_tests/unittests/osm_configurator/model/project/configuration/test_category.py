from typing import List

from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
from src.osm_configurator.model.project.configuration.category import Category
from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry

import src.osm_configurator.model.model_constants as model_constants_i


class TestCategory:

    def test_is_active(self):
        self.category: Category = Category("TestName")
        assert self.category.is_active()

    def test_activate(self):
        self.category: Category = Category("TestName")
        assert self.category.is_active()

    def test_state(self):
        self.category: Category = Category("TestName")
        self.category.deactivate()
        assert not self.category.is_active()
        self.category.activate()
        assert self.category.is_active()

    def test_get_whitelist(self):
        self.category: Category = Category("TestName")
        assert self.category.get_whitelist() == []

    def test_set_whitelist(self):
        self.category: Category = Category("TestName")
        whitelist: list[str] = ["building=*"]
        self.category.set_whitelist(whitelist)
        assert self.category.get_whitelist() == whitelist

    def test_get_blacklist(self):
        self.category: Category = Category("TestName")
        assert self.category.get_blacklist() == []

    def test_set_blacklist(self):
        self.category: Category = Category("TestName")
        blacklist: list[str] = ["building=*"]
        self.category.set_blacklist(blacklist)
        assert self.category.get_blacklist() == blacklist

    def test_get_category_name(self):
        self.category: Category = Category("TestName")
        assert self.category.get_category_name() == "TestName"

    def test_set_category_name(self):
        self.category: Category = Category("TestName")
        self.category.set_category_name("NewName")
        assert self.category.get_category_name() == "NewName"

    def test_set_category_name_error(self):
        self.category: Category = Category("TestName")
        assert not self.category.set_category_name("")

    def test_get_activated_attribute(self):
        self.category: Category = Category("TestName")
        assert self.category.get_activated_attribute() == []

    def test_get_not_activated_attribute(self):
        self.category: Category = Category("TestName")
        attribute_list: List[Attribute] = []
        for attribute in Attribute:
            attribute_list.append(attribute)
        assert self.category.get_not_activated_attribute() == attribute_list

    def test_get_attribute(self):
        self.category: Category = Category("TestName")
        assert not self.category.get_attribute(Attribute.FLOOR_AREA)
        assert not self.category.get_attribute(Attribute.NUMBER_OF_FLOOR)
        assert not self.category.get_attribute(Attribute.PROPERTY_AREA)

    def test_set_attribute(self):
        self.category: Category = Category("TestName")
        self.category.set_attribute(Attribute.FLOOR_AREA, True)
        self.category.set_attribute(Attribute.NUMBER_OF_FLOOR, True)
        assert self.category.get_attribute(Attribute.FLOOR_AREA)
        assert self.category.get_attribute(Attribute.NUMBER_OF_FLOOR)
        assert not self.category.get_attribute(Attribute.PROPERTY_AREA)

    def test_get_strictly_use_default_values(self):
        self.category: Category = Category("TestName")
        assert not self.category.get_strictly_use_default_values()

    def test_set_strictly_use_default_values(self):
        self.category: Category = Category("TestName")
        self.category.set_strictly_use_default_values(True)
        assert self.category.get_strictly_use_default_values()

    def test_get_calculation_method_of_area(self):
        self.category: Category = Category("TestName")
        assert self.category.get_calculation_method_of_area() == CalculationMethodOfArea.CALCULATE_BUILDING_AREA

    def test_set_calculation_method_of_area(self):
        self.category: Category = Category("TestName")
        self.category.set_calculation_method_of_area(CalculationMethodOfArea.CALCULATE_SITE_AREA)
        assert self.category.get_calculation_method_of_area() == CalculationMethodOfArea.CALCULATE_SITE_AREA

    def test_get_attractivity_attributes(self):
        self.category: Category = Category("TestName")
        assert self.category.get_attractivity_attributes() == []

    def test_add_attractivity_attributes(self):
        self.category: Category = Category("TestName")
        attribute: AttractivityAttribute = AttractivityAttribute("TestNameAttribute")
        self.category.add_attractivity_attribute(attribute)
        assert self.category.get_attractivity_attributes() == [attribute]

    def test_add_empty_attractivity_attributes(self):
        self.category: Category = Category("TestName")
        attribute: AttractivityAttribute = AttractivityAttribute("")
        assert not self.category.add_attractivity_attribute(attribute)

    def test_add_existing_attractivity_attributes(self):
        self.category: Category = Category("TestName")
        attribute: AttractivityAttribute = AttractivityAttribute("TestNameAttribute")
        assert self.category.add_attractivity_attribute(attribute)
        assert not self.category.add_attractivity_attribute(attribute)

    def test_remove_attractivity_attribute(self):
        self.category: Category = Category("TestName")
        attribute: AttractivityAttribute = AttractivityAttribute("TestNameAttribute")
        self.category.add_attractivity_attribute(attribute)
        assert self.category.get_attractivity_attributes() == [attribute]
        self.category.remove_attractivity_attribute(attribute)
        assert self.category.get_attractivity_attributes() == []

    def test_remove_not_existing_attractivity_attribute(self):
        self.category: Category = Category("TestName")
        attribute: AttractivityAttribute = AttractivityAttribute("TestNameAttribute")
        assert not self.category.remove_attractivity_attribute(attribute)

    def test_get_default_value_list(self):
        self.category: Category = Category("TestName")
        default: DefaultValueEntry = DefaultValueEntry(model_constants_i.DEFAULT_DEFAULT_VALUE_ENTRY_TAG)
        test_list: List[DefaultValueEntry] = [default]
        for number in range(len(self.category.get_default_value_list())):
            assert self.category.get_default_value_list()[number].get_default_value_entry_tag() == test_list[number].get_default_value_entry_tag()

    def test_add_default_value_entry(self):
        self.category: Category = Category("TestName")
        default: DefaultValueEntry = DefaultValueEntry(model_constants_i.DEFAULT_DEFAULT_VALUE_ENTRY_TAG)
        default_value_entry: DefaultValueEntry = DefaultValueEntry("TestNameAttribute")
        self.category.add_default_value_entry(default_value_entry)
        test_list: List[DefaultValueEntry] = [default, default_value_entry]
        for number in range(len(self.category.get_default_value_list())):
            assert self.category.get_default_value_list()[number].get_default_value_entry_tag() == test_list[number].get_default_value_entry_tag()

    def test_add_empty_default_value_entry(self):
        self.category: Category = Category("TestName")
        default_value_entry: DefaultValueEntry = DefaultValueEntry("")
        assert not self.category.add_default_value_entry(default_value_entry)

    def test_add_existing_default_value_entry(self):
        self.category: Category = Category("TestName")
        default_value_entry: DefaultValueEntry = DefaultValueEntry("TestNameAttribute")
        assert self.category.add_default_value_entry(default_value_entry)
        assert not self.category.add_default_value_entry(default_value_entry)

    def test_remove_default_value_entry(self):
        self.category: Category = Category("TestName")
        default: DefaultValueEntry = DefaultValueEntry(model_constants_i.DEFAULT_DEFAULT_VALUE_ENTRY_TAG)
        default_value_entry: DefaultValueEntry = DefaultValueEntry("TestNameAttribute")
        test_list: List[DefaultValueEntry] = [default, default_value_entry]
        self.category.add_default_value_entry(default_value_entry)
        for number in range(len(self.category.get_default_value_list())):
            assert self.category.get_default_value_list()[number].get_default_value_entry_tag() == test_list[number].get_default_value_entry_tag()
        self.category.remove_default_value_entry(default_value_entry)
        test_list.remove(default_value_entry)
        for number in range(len(self.category.get_default_value_list())):
            assert self.category.get_default_value_list()[number].get_default_value_entry_tag() == test_list[
                number].get_default_value_entry_tag()

    def test_remove_not_existing_default_value_entry(self):
        self.category: Category = Category("TestName")
        default_value_entry: DefaultValueEntry = DefaultValueEntry("TestNameAttribute")
        assert not self.category.remove_default_value_entry(default_value_entry)

    def test_move_default_value_entry_up(self):
        self.category: Category = Category("TestName")
        default: DefaultValueEntry = DefaultValueEntry(model_constants_i.DEFAULT_DEFAULT_VALUE_ENTRY_TAG)
        default_value_entry_one: DefaultValueEntry = DefaultValueEntry("TestNameAttribute1")
        default_value_entry_two: DefaultValueEntry = DefaultValueEntry("TestNameAttribute2")

        self.category.add_default_value_entry(default_value_entry_one)
        self.category.add_default_value_entry(default_value_entry_two)
        assert self.category.move_default_value_entry_up(default_value_entry_two)

        test_list: List[DefaultValueEntry] = [default, default_value_entry_two, default_value_entry_one]
        for number in range(len(self.category.get_default_value_list())):
            assert self.category.get_default_value_list()[number].get_default_value_entry_tag() == test_list[number].get_default_value_entry_tag()

    def test_move_default_value_entry_down(self):
        self.category: Category = Category("TestName")
        default: DefaultValueEntry = DefaultValueEntry(model_constants_i.DEFAULT_DEFAULT_VALUE_ENTRY_TAG)
        default_value_entry_one: DefaultValueEntry = DefaultValueEntry("TestNameAttribute1")
        default_value_entry_two: DefaultValueEntry = DefaultValueEntry("TestNameAttribute2")

        self.category.add_default_value_entry(default_value_entry_one)
        self.category.add_default_value_entry(default_value_entry_two)
        assert self.category.move_default_value_entry_down(default_value_entry_one)

        test_list: List[DefaultValueEntry] = [default, default_value_entry_two, default_value_entry_one]
        for number in range(len(self.category.get_default_value_list())):
            assert self.category.get_default_value_list()[number].get_default_value_entry_tag() == test_list[
                number].get_default_value_entry_tag()

    def test_move_default_value_entry_up_first(self):
        self.category: Category = Category("TestName")
        default_value_entry_one: DefaultValueEntry = DefaultValueEntry("TestNameAttribute1")
        self.category.add_default_value_entry(default_value_entry_one)
        assert not self.category.move_default_value_entry_up(default_value_entry_one)

    def test_move_default_value_entry_down_first(self):
        self.category: Category = Category("TestName")
        default_value_entry_one: DefaultValueEntry = DefaultValueEntry("TestNameAttribute1")
        self.category.add_default_value_entry(default_value_entry_one)
        assert not self.category.move_default_value_entry_up(default_value_entry_one)

    def test_move_default_value_entry_down_last(self):
        self.category: Category = Category("TestName")
        default_value_entry_one: DefaultValueEntry = DefaultValueEntry("TestNameAttribute1")
        self.category.add_default_value_entry(default_value_entry_one)
        assert not self.category.move_default_value_entry_down(default_value_entry_one)

    def test_move_default_value_entry_up_not_existing(self):
        self.category: Category = Category("TestName")
        default_value_entry: DefaultValueEntry = DefaultValueEntry("TestNameAttribute1")
        assert not self.category.move_default_value_entry_up(default_value_entry)

    def test_move_default_value_entry_down_not_existing(self):
        self.category: Category = Category("TestName")
        default_value_entry: DefaultValueEntry = DefaultValueEntry("TestNameAttribute1")
        assert not self.category.move_default_value_entry_down(default_value_entry)