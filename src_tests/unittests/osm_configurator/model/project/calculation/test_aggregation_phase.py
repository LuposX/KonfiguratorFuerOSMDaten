from __future__ import annotations

from typing import TYPE_CHECKING

from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.configuration.configuration_manager as configuration_manager
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion
import src.osm_configurator.model.project.calculation.aggregation_phase as aggregation_phase_i
import src.osm_configurator.model.project.calculation.aggregation_method_enum as aggregation_method_enum_i
import src.osm_configurator.model.project.configuration.attractivity_attribute as attractivity_attribute_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i
import src.osm_configurator.model.project.configuration.category as category_i

from pathlib import Path
import os
import shutil

if TYPE_CHECKING:
    from typing import Tuple, List
    from src.osm_configurator.model.project.calculation.calculation_state_enum import CalculationState
    from src.osm_configurator.model.project.configuration.configuration_manager import ConfigurationManager
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion
    from src.osm_configurator.model.project.calculation.aggregation_phase import AggregationPhase
    from src.osm_configurator.model.project.calculation.aggregation_method_enum import AggregationMethod
    from src.osm_configurator.model.project.configuration.attractivity_attribute import AttractivityAttribute
    from src.osm_configurator.model.project.configuration.category import Category


# without this you get a weird error, idk why
os.environ["PROJ_LIB"] = ""


def _prepare_config(project: Path, aggregation_methods: List[AggregationMethod]) -> ConfigurationManager:
    config_manager: ConfigurationManager = configuration_manager.ConfigurationManager(project)

    for agg in aggregation_methods:
        config_manager.get_aggregation_configuration().set_aggregation_method_active(agg, True)

    # create the test attractivity
    test1: AttractivityAttribute = attractivity_attribute_i.AttractivityAttribute("coolness")
    test1.set_attribute_factor(attribute_enum_i.Attribute.FLOOR_AREA, 1)
    test1.set_base_factor(1)

    test2: AttractivityAttribute = attractivity_attribute_i.AttractivityAttribute("trading")
    test2.set_attribute_factor(attribute_enum_i.Attribute.FLOOR_AREA, 1)
    test2.set_base_factor(1)

    # create test category
    category: Category = category_i.Category("test")
    category.set_attribute(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, True)
    category.add_attractivity_attribute(test1)
    category.add_attractivity_attribute(test2)

    # add the category to category manager
    config_manager.get_category_manager().add_categories([category])

    return config_manager


def _prepare_previous_phase_folder(path_to_new_proejct: Path, path_old_data: Path, iddir: bool):
    # Prepare result folder
    deleter: FileDeletion = file_deletion.FileDeletion()
    deleter.reset_folder(path_to_new_proejct)

    if iddir:
        # move the files from data to it
        for file_name in os.listdir(path_old_data):
            shutil.copy2(os.path.join(path_old_data, file_name), path_to_new_proejct)
    else:
        shutil.copy2(path_old_data, path_to_new_proejct)


class TestAggregationPhase:
    def test_corrupted_data(self):
        # Set up paths
        project_path: Path = Path(os.path.join(TEST_DIR, "build/aggregation_phase/projectXY"))

        # Set up result folder from last phase
        # so delete folder from previous test runs and copy the data into it
        _prepare_previous_phase_folder(os.path.join(os.path.join(project_path, "results/"),
                                                    calculation_phase_enum.CalculationPhase.ATTRACTIVITY_PHASE
                                                    .get_folder_name_for_results()),
                                       os.path.join(TEST_DIR, "data/monaco_split_up_files_invalid/"),
                                       True
                                       )

        # Set up configurator
        config_manager: ConfigurationManager = _prepare_config(project_path, [aggregation_method_enum_i.AggregationMethod.SUM])

        # Execute test
        phase: AggregationPhase = aggregation_phase_i.AggregationPhase()
        result1: CalculationState = phase.calculate(config_manager)

        assert result1[0] == calculation_state_enum.CalculationState.ERROR_INVALID_OSM_DATA

    def test_correct_data(self):
        # Set up paths
        project_path: Path = Path(os.path.join(TEST_DIR, "build/aggregation_phase/projectXY"))

        # Set up result folder from last phase
        # so delete folder from previous test runs and copy the data into it
        _prepare_previous_phase_folder(os.path.join(os.path.join(project_path, "results/"),
                                                    calculation_phase_enum.CalculationPhase.ATTRACTIVITY_PHASE
                                                    .get_folder_name_for_results()),
                                       os.path.join(TEST_DIR, "data/monaco_needed_data_for_aggregation_phase/"),
                                       True
                                       )

        # Set up configurator
        config_manager: ConfigurationManager = _prepare_config(project_path,
                                                               [aggregation_method_enum_i.AggregationMethod.SUM,
                                                                aggregation_method_enum_i.AggregationMethod.VARIANCE,
                                                                aggregation_method_enum_i.AggregationMethod.QUANTILE_25,
                                                                aggregation_method_enum_i.AggregationMethod.MAXIMUM,
                                                                aggregation_method_enum_i.AggregationMethod.MEAN
                                                                ])

        # Execute test
        phase: AggregationPhase = aggregation_phase_i.AggregationPhase()
        result1: (CalculationState, str) = phase.calculate(config_manager)

        assert result1[0] == calculation_state_enum.CalculationState.RUNNING

        # Test if files were created
        assert len(
            os.listdir(os.path.join(project_path, "results/" + calculation_phase_enum.CalculationPhase.AGGREGATION_PHASE
                                    .get_folder_name_for_results()))) == 5

        # Test if execution works a second time
        result2: (CalculationState, str) = phase.calculate(config_manager)
        assert result2[0] == calculation_state_enum.CalculationState.RUNNING