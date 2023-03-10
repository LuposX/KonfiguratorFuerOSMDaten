from __future__ import annotations

import os
from pathlib import Path

from src.osm_configurator.model.project.active_project import ActiveProject
import src.osm_configurator.model.application.application_settings as application_settings_i
from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
from src.osm_configurator.model.project.configuration.category import Category
from src_tests.definitions import TEST_DIR


class TestUsecase14:
    def test_usecase(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True,
                                                           application_settings_o, "TestDefaultValues")
        test_category: Category = Category("CategoryOne")
        self.active_project.get_config_manager().get_category_manager().create_category(test_category)

        # Description part 1 - create new attractivity attribute
        new_attribute: AttractivityAttribute = AttractivityAttribute("TestAttribute")
        assert self.active_project.get_config_manager().get_category_manager().get_category("CategoryOne").add_attractivity_attribute(new_attribute)

        # Description part 2 - change values
        assert self.active_project.get_config_manager().get_category_manager().get_category("CategoryOne")\
            .get_attractivity_attributes()[0].set_base_factor(6.0)
        assert self.active_project.get_config_manager().get_category_manager().get_category("CategoryOne")\
            .get_attractivity_attributes()[0].get_base_factor() == 6.0

        # Description part 2 - rename
        assert self.active_project.get_config_manager().get_category_manager().get_category("CategoryOne")\
            .get_attractivity_attributes()[0].set_attractivity_attribute_name("NewNameForTestAttribute")
        assert self.active_project.get_config_manager().get_category_manager().get_category("CategoryOne")\
                   .get_attractivity_attributes()[0].get_attractivity_attribute_name() == "NewNameForTestAttribute"

        # Description part 2 - delete
        assert self.active_project.get_config_manager().get_category_manager().get_category("CategoryOne")\
            .remove_attractivity_attribute(new_attribute)
