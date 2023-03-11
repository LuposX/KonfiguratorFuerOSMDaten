from __future__ import annotations

import os
import shutil
from typing import TYPE_CHECKING

import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

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
from src.osm_configurator.model.project.project_io_handler import ProjectIOHandler
from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.application.application_settings as application_settings_i

if TYPE_CHECKING:
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion


def _prepare_project_folder(path_to_new_project: Path, path_old_data: Path):
    # Prepare result folder
    deleter: FileDeletion = file_deletion.FileDeletion()
    deleter.reset_folder(path_to_new_project)

    # move the files from data to it
    try:
        shutil.copytree(path_old_data, path_to_new_project)
    except:
        pass
    with open(os.path.join(path_to_new_project, "application_settings.json"), "w") as file:
        file.write(str(path_to_new_project))


class TestProjectIO:
    def prepare(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProject1", "This project is to test!")

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

    def test_build_project(self):

        application_settings_o = application_settings_i.ApplicationSettings()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True, application_settings_o, "TestProject5", "This project is to test the build!")
        self.project_io_handler: ProjectIOHandler = ProjectIOHandler(self.active_project)
        assert not self.project_io_handler.build_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProject5")))
        if os.path.exists(Path(os.path.join(TEST_DIR, "build/Projects/TestProject6"))):
            shutil.rmtree(Path(os.path.join(TEST_DIR, "build/Projects/TestProject6")))
            assert self.project_io_handler.build_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProject6")))
        else:
            assert self.project_io_handler.build_project(Path(os.path.join(TEST_DIR, "build/Projects/TestProject6")))

    def test_load_settings(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.prepare()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), False, application_settings_o,  "TestProject1")
        assert "TestProject1" == self.active_project.get_project_settings().get_name()
        assert "This project is to test!" == self.active_project.get_project_settings().get_description()
        assert Path(os.path.join(TEST_DIR, "build/Projects/TestProject1")) == self.active_project.get_project_settings().get_location()

    def test_load_config(self):
        application_settings_o = application_settings_i.ApplicationSettings()

        self.prepare()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), False, application_settings_o, "TestProject1")
        assert ConfigPhase.CATEGORY_CONFIG_PHASE == self.active_project.get_last_step()

    def test_load_osm(self):
        application_settings_o = application_settings_i.ApplicationSettings()

        self.prepare()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), False, application_settings_o, "TestProject1")
        assert Path(os.path.join(TEST_DIR, "data/monaco-latest.osm")) == self.active_project.get_config_manager().get_osm_data_configuration().get_osm_data()

    def test_load_aggregation(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.prepare()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), False, application_settings_o, "TestProject1")
        test_aggregation_configurator: AggregationConfiguration = self.active_project.get_config_manager().get_aggregation_configuration()
        assert test_aggregation_configurator.is_aggregation_method_active(AggregationMethod.MAXIMUM)
        assert not test_aggregation_configurator.is_aggregation_method_active(AggregationMethod.MEDIAN)

    def test_cut_out_config(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.prepare()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), False, application_settings_o, "TestProject1")
        test_cut_out_configurator: CutOutConfiguration = self.active_project.get_config_manager().get_cut_out_configuration()
        assert Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson")) == test_cut_out_configurator.get_cut_out_path()
        assert CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED == test_cut_out_configurator.get_cut_out_mode()

    def test_categories(self):
        application_settings_o = application_settings_i.ApplicationSettings()
        self.prepare()
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), False, application_settings_o, "TestProject1")
        test_category_manager: CategoryManager = self.active_project.get_config_manager().get_category_manager()
        test_cat_one: Category = test_category_manager.get_category("Category1")
        test_cat_two: Category = test_category_manager.get_category("Category2")
        assert "Category1" == test_cat_one.get_category_name()
        assert "Category2" == test_cat_two.get_category_name()

        assert test_cat_one.is_active()
        white_list: list[str] = ["buildings=True", "test_False"]
        black_list: list[str] = ["buildings=False"]
        assert white_list == test_cat_one.get_whitelist()
        assert black_list == test_cat_one.get_blacklist()

        assert CalculationMethodOfArea.CALCULATE_BUILDING_AREA == test_cat_one.get_calculation_method_of_area()
        assert test_cat_one.get_attribute(Attribute.PROPERTY_AREA)
        assert not test_cat_one.get_attribute(Attribute.FLOOR_AREA)
        assert test_cat_one.get_strictly_use_default_values()

        test_attractivity_attribute_one: AttractivityAttribute = AttractivityAttribute("attribute1")
        test_attractivity_attribute_one.set_base_factor(10)
        test_attractivity_attribute_two: AttractivityAttribute = AttractivityAttribute("attribute2")
        test_attractivity_attribute_two.set_base_factor(20)
        assert test_attractivity_attribute_one.get_attractivity_attribute_name() == test_cat_one.get_attractivity_attributes()[0].get_attractivity_attribute_name()
        assert test_attractivity_attribute_one.get_base_factor() == test_cat_one.get_attractivity_attributes()[0].get_base_factor()
        assert test_attractivity_attribute_two.get_attractivity_attribute_name() == test_cat_one.get_attractivity_attributes()[1].get_attractivity_attribute_name()
        assert test_attractivity_attribute_two.get_base_factor() == test_cat_one.get_attractivity_attributes()[1].get_base_factor()
