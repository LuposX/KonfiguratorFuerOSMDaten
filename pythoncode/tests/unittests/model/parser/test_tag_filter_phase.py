
import src.osm_configurator.model.project.calculation.tag_filter_phase as tag_filter_phase
import src.osm_configurator.model.project.configuration.configuration_manager as configuration_manager
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum

import pathlib


class TestTagFilterPhase:
    def test_get_checkpoints_folder_path_from_phase(self):
        active_project = pathlib.Path("../../data/active_project_simulation")

        config_manager = configuration_manager.ConfigurationManager(active_project)

        created_path = tag_filter_phase._get_checkpoints_folder_path_from_phase(config_manager,
                                                                 calculation_phase_enum.CalculationPhase.TAG_FILTER_PHASE)

        assert pathlib.Path("../../data/active_project_simulation/Results/tag_filter_phase/") == created_path



