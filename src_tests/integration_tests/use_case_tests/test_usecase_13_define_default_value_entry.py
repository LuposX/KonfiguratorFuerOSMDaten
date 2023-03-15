from __future__ import annotations

import os
from pathlib import Path

from src.osm_configurator.model.project.active_project import ActiveProject
import src.osm_configurator.model.application.application_settings as application_settings_i
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.category import Category
from src.osm_configurator.model.project.configuration.default_value_entry import DefaultValueEntry
from src_tests.definitions import TEST_DIR


class TestUsecase13:
    def test_usecase(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True,
                                                           application_settings_o, "TestDefaultValues")
        test_category: Category = Category("CategoryOne")
        self.active_project.get_config_manager().get_category_manager().create_category(test_category)

        # Description part 3 - create default value entry
        new_default_value_entry_one: DefaultValueEntry = DefaultValueEntry("TestTag1")
        assert self.active_project.get_config_manager().get_category_manager().get_category(
            "CategoryOne").add_default_value_entry(new_default_value_entry_one)
        new_default_value_entry_two: DefaultValueEntry = DefaultValueEntry("TestTag2")
        assert self.active_project.get_config_manager().get_category_manager().get_category(
            "CategoryOne").add_default_value_entry(new_default_value_entry_two)

        # Desciption part 4 - display values of the new default value entry
        assert self.active_project.get_config_manager().get_category_manager().get_category(
            "CategoryOne").get_default_value_list()[1].get_default_value_entry_tag() == "TestTag1"
        assert self.active_project.get_config_manager().get_category_manager().get_category(
            "CategoryOne").get_default_value_list()[1].get_attribute_default(Attribute.FLOOR_AREA) == 0.0
        assert self.active_project.get_config_manager().get_category_manager().get_category(
            "CategoryOne").get_default_value_list()[1].get_attribute_default(Attribute.NUMBER_OF_FLOOR) == 0.0
        assert self.active_project.get_config_manager().get_category_manager().get_category(
            "CategoryOne").get_default_value_list()[1].get_attribute_default(Attribute.PROPERTY_AREA) == 0.0

        # Desciption part 5 - change the name
        assert self.active_project.get_config_manager().get_category_manager().get_category(
            "CategoryOne").get_default_value_list()[1].set_tag("NewNameForTag1")

        # Desciption part 6 - change the order of the default value entries
        assert not self.active_project.get_config_manager().get_category_manager().get_category(
            "CategoryOne").move_default_value_entry_up(new_default_value_entry_one)
        assert self.active_project.get_config_manager().get_category_manager().get_category(
            "CategoryOne").move_default_value_entry_up(new_default_value_entry_two)

        # Desciption part 7 - change the value of the attributes
        assert self.active_project.get_config_manager().get_category_manager().get_category(
            "CategoryOne").get_default_value_list()[1].set_attribute_default(Attribute.FLOOR_AREA, 5.0)
        assert self.active_project.get_config_manager().get_category_manager().get_category(
            "CategoryOne").get_default_value_list()[1].get_attribute_default(Attribute.FLOOR_AREA) == 5.0

