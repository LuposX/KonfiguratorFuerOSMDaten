from __future__ import annotations

import csv
import os
import shutil
from pathlib import Path

from src.osm_configurator.model.application.application import Application
from src.osm_configurator.model.project.active_project import ActiveProject
from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase
from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
from src.osm_configurator.model.project.configuration.category import Category
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode
from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.application.application_settings as application_settings_i
from src.osm_configurator.model.application.application_settings_default_enum import ApplicationSettingsDefault


class TestApplication:

    def prepare(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True,
                                                           application_settings_o, "TestProjectApplication",
                                                           "This project is to test!")

        self.active_project.set_last_step(ConfigPhase.CATEGORY_CONFIG_PHASE)

        self.active_project.get_config_manager().get_osm_data_configuration() \
            .set_osm_data(Path(os.path.join(TEST_DIR, "data/monaco-latest.osm")))

        self.active_project.get_config_manager().get_aggregation_configuration() \
            .set_aggregation_method_active(AggregationMethod.MAXIMUM, True)

        self.active_project.get_config_manager().get_cut_out_configuration() \
            .set_cut_out_path(Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson")))
        self.active_project.get_config_manager().get_cut_out_configuration() \
            .set_cut_out_mode(CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED)

        test_category: Category = Category("Category1")
        test_category.activate()
        white_list: list[str] = ["buildings=True", "test_False"]
        black_list: list[str] = ["buildings=False"]
        test_category.set_whitelist(white_list)
        test_category.set_blacklist(black_list)
        test_category.set_calculation_method_of_area(CalculationMethodOfArea.CALCULATE_BUILDING_AREA)
        test_category.set_attribute(Attribute.PROPERTY_AREA, True)
        test_category.set_strictly_use_default_values(True)
        test_attractivity_attribute_one: AttractivityAttribute = AttractivityAttribute("attribute1")
        test_attractivity_attribute_one.set_base_factor(10)
        test_attractivity_attribute_two: AttractivityAttribute = AttractivityAttribute("attribute2")
        test_attractivity_attribute_two.set_base_factor(20)
        test_category.add_attractivity_attribute(test_attractivity_attribute_one)
        test_category.add_attractivity_attribute(test_attractivity_attribute_two)
        test_category_two: Category = Category("Category2")
        test_category_two.activate()
        self.active_project.get_config_manager().get_category_manager().create_category(test_category)
        self.active_project.get_config_manager().get_category_manager().create_category(test_category_two)
        self.active_project.get_project_saver().save_project()

    def test_load_project(self):
        self.prepare()
        application: Application = Application()
        application.load_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))

    def test_load_project_with_wrong_path(self):
        self.prepare()
        application: Application = Application()
        application.load_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplicationWrong")))

    def test_get_passive_project_list(self):
        self.prepare()
        application: Application = Application(Path(os.path.join(TEST_DIR, "build/Projects")))
        application.get_application_settings().set_setting(ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER,
                                                           Path(os.path.join(TEST_DIR, "build/Projects")))
        assert application.get_passive_project_list() != []

    def test_get_key_recommendation_system(self):
        self.prepare()
        application: Application = Application()
        assert application.get_key_recommendation_system() is not None

    def test_create_passive_project_list_wrong_path(self):
        self.prepare()
        application: Application = Application(Path(os.path.join(TEST_DIR, "build/Projects")))
        application.get_application_settings().set_setting(ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER,
                                                           Path(os.path.join(TEST_DIR, "build/Projects")))
        assert application._create_passive_project_list(Path(os.path.join(TEST_DIR, "build/Projects/WrongPath"))) == []

    def test_unload_project(self):
        self.prepare()
        application: Application = Application(Path(os.path.join(TEST_DIR, "build/Projects")))
        application.get_application_settings().set_setting(ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER, Path(os.path.join(TEST_DIR, "build/Projects")))
        application.load_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))
        application.unload_project()
        assert application.get_active_project() is None

    def test_load_project_with_missing_configuration(self):
        self.prepare()
        application: Application = Application(Path(os.path.join(TEST_DIR, "build/Projects")))
        application.get_application_settings().set_setting(ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER,
                                                           Path(os.path.join(TEST_DIR, "build/Projects")))
        filename: Path = Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication/configuration"))
        shutil.rmtree(filename)
        assert not application.load_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))
        assert application.get_active_project() is None
        shutil.rmtree(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))

    def test_load_project_with_missing_categories(self):
        self.prepare()
        application: Application = Application(Path(os.path.join(TEST_DIR, "build/Projects")))
        application.get_application_settings().set_setting(ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER,
                                                           Path(os.path.join(TEST_DIR, "build/Projects")))
        filename: Path = Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication/configuration/categories"))
        shutil.rmtree(filename)
        assert not application.load_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))
        assert application.get_active_project() is None
        shutil.rmtree(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))

    def test_load_project_with_missing_project(self):
        self.prepare()
        application: Application = Application(Path(os.path.join(TEST_DIR, "build/Projects")))
        application.get_application_settings().set_setting(ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER,
                                                           Path(os.path.join(TEST_DIR, "build/Projects")))
        filename: Path = Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication"))
        shutil.rmtree(filename)
        assert not application.load_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))
        assert application.get_active_project() is None

    def test_load_project_with_missing_project_settings(self):
        self.prepare()
        application: Application = Application(Path(os.path.join(TEST_DIR, "build/Projects")))
        application.get_application_settings().set_setting(ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER,
                                                           Path(os.path.join(TEST_DIR, "build/Projects")))
        filename: Path = Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication/project_settings.csv"))
        os.remove(filename)
        assert not application.load_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))
        assert application.get_active_project() is None
        shutil.rmtree(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))

    def test_load_project_with_missing_last_step(self):
        self.prepare()
        application: Application = Application(Path(os.path.join(TEST_DIR, "build/Projects")))
        application.get_application_settings().set_setting(ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER,
                                                           Path(os.path.join(TEST_DIR, "build/Projects")))
        filename: Path = Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication/last_step.txt"))
        os.remove(filename)
        assert not application.load_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))
        assert application.get_active_project() is None
        shutil.rmtree(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))

    def test_load_project_with_missing_aggregation(self):
        self.prepare()
        application: Application = Application(Path(os.path.join(TEST_DIR, "build/Projects")))
        application.get_application_settings().set_setting(ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER,
                                                           Path(os.path.join(TEST_DIR, "build/Projects")))
        filename: Path = Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication/configuration/aggregation_methods.csv"))
        os.remove(filename)
        assert not application.load_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))
        assert application.get_active_project() is None
        shutil.rmtree(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))

    def test_load_project_with_missing_cut_out(self):
        self.prepare()
        application: Application = Application(Path(os.path.join(TEST_DIR, "build/Projects")))
        application.get_application_settings().set_setting(ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER,
                                                           Path(os.path.join(TEST_DIR, "build/Projects")))
        filename: Path = Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication/configuration/cut_out_configuration.csv"))
        os.remove(filename)
        assert not application.load_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))
        assert application.get_active_project() is None
        shutil.rmtree(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))

    def test_load_project_with_missing_osm(self):
        self.prepare()
        application: Application = Application(Path(os.path.join(TEST_DIR, "build/Projects")))
        application.get_application_settings().set_setting(ApplicationSettingsDefault.DEFAULT_PROJECT_FOLDER,
                                                           Path(os.path.join(TEST_DIR, "build/Projects")))
        filename: Path = Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication/configuration/osm_path.txt"))
        os.remove(filename)
        assert not application.load_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))
        assert application.get_active_project() is None
        shutil.rmtree(Path(os.path.join(TEST_DIR, "build/Projects/TestProjectApplication")))
