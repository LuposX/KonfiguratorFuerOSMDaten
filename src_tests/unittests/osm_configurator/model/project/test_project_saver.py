import shutil
import unittest

from pathlib import Path
from typing import List

from src.osm_configurator.model.project.active_project import ActiveProject
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode
from src.osm_configurator.model.project.configuration.category import Category
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute


class MyTestCase(unittest.TestCase):
    def test_build(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, True, "TestProject1", "Das sollte funktionieren")
        self.active_project.get_project_saver().save_project()

    def test_save_settings(self):
        self.test_build()
        self.active_project.get_project_settings().change_name("ChangedName")
        self.active_project.get_project_settings().set_description("Hat bombe funktioniert")
        self.active_project.get_project_settings().change_calculation_phase_checkpoints_folder("tniokcehc")
        self.active_project.get_project_saver().save_project()

    def test_save_config_phase(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.active_project.set_last_step(ConfigPhase.CATEGORY_CONFIG_PHASE)
        self.active_project.get_project_saver().save_project()

    def test_save_osm_configurator(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.active_project.get_config_manager().get_osm_data_configuration() \
            .set_osm_data(Path("C:"))
        self.active_project.get_project_saver().save_project()

    def test_save_aggregation_configurator(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.active_project.get_config_manager().get_aggregation_configuration() \
            .set_aggregation_method_active(AggregationMethod.LOWER_QUARTILE, True)
        self.active_project.get_project_saver().save_project()

    def test_save_cut_out_configurator(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.active_project.get_config_manager().get_cut_out_configuration() \
            .set_cut_out_path(Path("C:"))
        self.active_project.get_config_manager().get_cut_out_configuration() \
            .set_cut_out_mode(CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED)
        self.active_project.get_project_saver().save_project()

    def test_save_categories(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        test_category: Category = Category()
        test_category.set_category_name("Category1")
        test_category.activate()
        white_list: list[str] = ["buildings=True", "test_False"]
        black_list: list[str] = ["buildings=False"]
        test_category.set_whitelist(white_list)
        test_category.set_blacklist(black_list)
        test_category.set_calculation_method_of_area(CalculationMethodOfArea.CALCULATE_BUILDING_AREA)
        test_category.set_attribute(Attribute.PROPERTY_AREA, True)
        test_category.set_strictly_use_default_values(True)
        test_attractivity_attribute_one: AttractivityAttribute = AttractivityAttribute("attribute1", 0)
        test_attractivity_attribute_two: AttractivityAttribute = AttractivityAttribute("attribute2", 5)
        test_category.add_attractivity_attribute(test_attractivity_attribute_one)
        test_category.add_attractivity_attribute(test_attractivity_attribute_two)

        test_category_two: Category = Category()
        test_category_two.set_category_name("Category2")
        test_category_two.activate()

        self.active_project.get_config_manager().get_category_manager().create_category(test_category)
        self.active_project.get_config_manager().get_category_manager().create_category(test_category_two)
        self.active_project.get_project_saver().save_project()


if __name__ == '__main__':
    unittest.main()
