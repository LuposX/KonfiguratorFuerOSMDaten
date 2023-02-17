from __future__ import annotations

from typing import TYPE_CHECKING

import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
from src.osm_configurator.model.project.configuration.attribute_enum import Attribute
from src.osm_configurator.model.project.configuration.calculation_method_of_area_enum import CalculationMethodOfArea
from src.osm_configurator.model.project.configuration.category import Category
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode
from src_tests.definitions import TEST_DIR
from src.osm_configurator.model.project.active_project import ActiveProject
from src.osm_configurator.model.project.config_phase_enum import ConfigPhase

from pathlib import Path
import os
import shutil

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


class TestProjectSaver:
    def test_build(self):
        self.active_project: ActiveProject = ActiveProject(Path(os.path.join(TEST_DIR, "build/Projects")), True,
                                                           "TestProject1", "Das sollte funktionieren")
        self.active_project.get_project_saver().save_project()

    def test_save_settings(self):
        self.test_build()
        self.active_project.get_project_settings().change_name("ChangedName")
        self.active_project.get_project_settings().set_description("Hat bombe funktioniert")
        self.active_project.get_project_settings().change_calculation_phase_checkpoints_folder("tniokcehc")
        self.active_project.get_project_saver().save_project()

    def test_save_config_phase(self):
        self.test_build()
        self.active_project.set_last_step(ConfigPhase.CATEGORY_CONFIG_PHASE)
        self.active_project.get_project_saver().save_project()

    def test_save_osm_configurator(self):
        self.test_build()
        self.active_project.get_config_manager().get_osm_data_configuration() \
            .set_osm_data(Path(os.path.join(TEST_DIR, "data/monaco-latest.osm")))
        self.active_project.get_project_saver().save_project()

    def test_save_aggregation_configurator(self):
        self.test_build()
        self.active_project.get_config_manager().get_aggregation_configuration() \
            .set_aggregation_method_active(AggregationMethod.MAXIMUM, True)
        self.active_project.get_project_saver().save_project()

    def test_save_cut_out_configurator(self):
        self.test_build()
        self.active_project.get_config_manager().get_cut_out_configuration() \
            .set_cut_out_path(Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson")))
        self.active_project.get_config_manager().get_cut_out_configuration() \
            .set_cut_out_mode(CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED)
        self.active_project.get_project_saver().save_project()

    def test_save_categories(self):
        self.test_build()
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
