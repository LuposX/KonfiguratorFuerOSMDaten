from __future__ import annotations

import os
from pathlib import Path

from src.osm_configurator.model.project.active_project import ActiveProject
import src.osm_configurator.model.application.application_settings as application_settings_i
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
from src.osm_configurator.model.project.configuration.category import Category
from src_tests.definitions import TEST_DIR


class TestUsecase12:
    def test_usecase(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True,
                                                           application_settings_o, "TestDefaultValues")
        test_category: Category = Category("CategoryOne")
        self.active_project.get_config_manager().get_category_manager().create_category(test_category)

        # Description part 1
        assert self.active_project.get_config_manager().get_category_manager().get_category("CategoryOne").set_strictly_use_default_values(True)

        # Description part 2
        assert self.active_project.get_config_manager().get_category_manager().get_category("CategoryOne").set_attribute(Attribute.PROPERTY_AREA, True)

        # Description part 3
        assert self.active_project.get_config_manager().get_category_manager().get_category("CategoryOne").set_calculation_method_of_area(CalculationMethodOfArea.CALCULATE_SITE_AREA)

        # Description part 4
        assert self.active_project.get_config_manager().get_category_manager().get_category("CategoryOne").set_attribute(Attribute.FLOOR_AREA, True)
