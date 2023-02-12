import unittest
from pathlib import Path

from src.osm_configurator.model.project.active_project import ActiveProject
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationConfiguration
from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
from src.osm_configurator.model.project.configuration.cut_out_configuration import CutOutConfiguration
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode
from src.osm_configurator.model.project.configuration.category_manager import CategoryManager
from src.osm_configurator.model.project.configuration.category import Category


class MyTestCase(unittest.TestCase):
    def prepare(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, True, "TestProject1", "This project is to test!")

        self.active_project.set_last_step(ConfigPhase.CATEGORY_CONFIG_PHASE)

        self.active_project.get_config_manager().get_osm_data_configuration() \
            .set_osm_data(Path("C:"))

        self.active_project.get_config_manager().get_aggregation_configuration() \
            .set_aggregation_method_active(AggregationMethod.LOWER_QUARTILE, True)

        self.active_project.get_config_manager().get_cut_out_configuration() \
            .set_cut_out_path(Path("C:"))
        self.active_project.get_config_manager().get_cut_out_configuration() \
            .set_cut_out_mode(CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED)

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

    def test_load_settings(self):
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.assertEqual("TestProject1", self.active_project.get_project_settings().get_name())
        self.assertEqual("This project is to test!", self.active_project.get_project_settings().get_description())
        self.assertEqual(Path("C:TestProject1"), self.active_project.get_project_settings().get_location())
        self.assertEqual("calculation_check_points",
                         self.active_project.get_project_settings().get_calculation_phase_checkpoints_folder())

    def test_load_config(self):
        self.prepare()
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.assertEqual(ConfigPhase.CATEGORY_CONFIG_PHASE, self.active_project.get_last_step())

    def test_load_osm(self):
        self.prepare()
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.assertEqual(Path("C:"),
                         self.active_project.get_config_manager().get_osm_data_configuration().get_osm_data())

    def test_load_aggregation(self):
        self.prepare()
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        test_aggregation_configurator: AggregationConfiguration = self.active_project.get_config_manager().get_aggregation_configuration()
        self.assertEqual(False, test_aggregation_configurator.is_aggregation_method_active(AggregationMethod.AVERAGE))
        self.assertEqual(True,
                         test_aggregation_configurator.is_aggregation_method_active(AggregationMethod.LOWER_QUARTILE))

    def test_cut_out_config(self):
        self.prepare()
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        test_cut_out_configurator: CutOutConfiguration = self.active_project.get_config_manager().get_cut_out_configuration()
        self.assertEqual(Path("C:"), test_cut_out_configurator.get_cut_out_path())
        self.assertEqual(CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED, test_cut_out_configurator.get_cut_out_mode())

    def test_categories(self):
        self.prepare()
        path: Path = Path("C:")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        test_category_manager: CategoryManager = self.active_project.get_config_manager().get_category_manager()
        test_cat_one: Category = test_category_manager.get_category(0)
        test_cat_two: Category = test_category_manager.get_category(1)
        self.assertEqual("Category1", test_cat_one.get_category_name())
        self.assertEqual("Category2", test_cat_two.get_category_name())

        self.assertEqual(True, test_cat_one.is_active())
        white_list: list[str] = ["buildings=True", "test_False"]
        black_list: list[str] = ["buildings=False"]
        self.assertEqual(white_list, test_cat_one.get_whitelist())
        self.assertEqual(black_list, test_cat_one.get_blacklist())

        self.assertEqual(CalculationMethodOfArea.CALCULATE_BUILDING_AREA, test_cat_one.get_calculation_method_of_area())
        self.assertEqual(True, test_cat_one.get_attribute(Attribute.PROPERTY_AREA))
        self.assertEqual(False, test_cat_one.get_attribute(Attribute.FLOOR_AREA))
        self.assertEqual(True, test_cat_one.get_strictly_use_default_values())

        test_attractivity_attribute_one: AttractivityAttribute = AttractivityAttribute("attribute1", 0)
        test_attractivity_attribute_two: AttractivityAttribute = AttractivityAttribute("attribute2", 5)
        self.assertEqual(test_attractivity_attribute_one.get_attractivity_attribute_name(),
                         test_cat_one.get_attractivity_attributes()[0].get_attractivity_attribute_name())
        self.assertEqual(test_attractivity_attribute_one.get_base_factor(),
                         test_cat_one.get_attractivity_attributes()[0].get_base_factor())
        self.assertEqual(test_attractivity_attribute_two.get_attractivity_attribute_name(),
                         test_cat_one.get_attractivity_attributes()[1].get_attractivity_attribute_name())
        self.assertEqual(test_attractivity_attribute_two.get_base_factor(),
                         test_cat_one.get_attractivity_attributes()[1].get_base_factor())


if __name__ == '__main__':
    unittest.main()
