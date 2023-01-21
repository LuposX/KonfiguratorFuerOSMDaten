
import src.osm_configurator.model.project.calculation.tag_filter_phase as tag_filter_phase
import src.osm_configurator.model.project.configuration.configuration_manager as configuration_manager
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum

import pathlib


class TestTagFilterPhase:
    def test_get_checkpoints_folder_path_from_phase(self):
        path_currentPath = pathlib.Path()

        config_manager = configuration_manager.ConfigurationManager(path_currentPath)

        tag_filter_phase._get_checkpoints_folder_path_from_phase(configuration_manager,
                                                                 calculation_phase_enum.CalculationPhase.TAG_FILTER_PHASE)

