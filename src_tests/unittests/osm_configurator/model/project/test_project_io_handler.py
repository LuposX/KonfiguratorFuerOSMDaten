import unittest
from pathlib import Path

from src.osm_configurator.model.project.active_project import ActiveProject
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
from src.osm_configurator.model.project.configuration.aggregation_configuration import AggregationConfiguration
from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
from src.osm_configurator.model.project.configuration.cut_out_configuration import CutOutConfiguration
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode


class MyTestCase(unittest.TestCase):
    def test_load_settings(self):
        path: Path = Path("C:\Arbeitsplatz\AA_PSE_tests")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.assertEqual("TestProject1", self.active_project.get_project_settings().get_name())
        self.assertEqual("Das sollte funktionieren", self.active_project.get_project_settings().get_description())
        self.assertEqual(Path("C:\Arbeitsplatz\AA_PSE_tests\TestProject1"), self.active_project.get_project_settings().get_location())
        self.assertEqual("calculation_check_points", self.active_project.get_project_settings().get_calculation_phase_checkpoints_folder())

    def test_load_config(self):
        path: Path = Path("C:\Arbeitsplatz\AA_PSE_tests")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.assertEqual(ConfigPhase.CATEGORY_CONFIG_PHASE, self.active_project.get_last_step())

    def test_load_osm(self):
        path: Path = Path("C:\Arbeitsplatz\AA_PSE_tests")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        self.assertEqual(Path("C:\Arbeitsplatz\KIT.docx"), self.active_project.get_config_manager().get_osm_data_configuration().get_osm_data())

    def test_load_aggregation(self):
        path: Path = Path("C:\Arbeitsplatz\AA_PSE_tests")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        test_aggregation_configurator: AggregationConfiguration = self.active_project.get_config_manager().get_aggregation_configuration()
        self.assertEqual(False, test_aggregation_configurator.is_aggregation_method_active(AggregationMethod.AVERAGE))
        self.assertEqual(True, test_aggregation_configurator.is_aggregation_method_active(AggregationMethod.LOWER_QUARTILE))

    def test_cut_out_config(self):
        path: Path = Path("C:\Arbeitsplatz\AA_PSE_tests")
        self.active_project: ActiveProject = ActiveProject(path, False, "TestProject1")
        test_cut_out_configurator: CutOutConfiguration = self.active_project.get_config_manager().get_cut_out_configuration()
        self.assertEqual(Path("C:\Arbeitsplatz\KIT.docx"), test_cut_out_configurator.get_cut_out_path())
        self.assertEqual(CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED, test_cut_out_configurator.get_cut_out_mode())


if __name__ == '__main__':
    unittest.main()
