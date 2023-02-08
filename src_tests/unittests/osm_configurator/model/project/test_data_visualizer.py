from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd

from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.project.calculation.geo_data_phase as geo_data_phase
import src.osm_configurator.model.project.calculation.calculation_state_enum as calculation_state_enum
import src.osm_configurator.model.project.configuration.configuration_manager as configuration_manager
import src.osm_configurator.model.project.calculation.calculation_phase_utility as calculation_phase_utility
import src.osm_configurator.model.project.calculation.calculation_phase_enum as calculation_phase_enum
import src.osm_configurator.model.project.data_visualizer as data_visualizer_i
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

from pathlib import Path
import os

if TYPE_CHECKING:
    from src.osm_configurator.model.project.calculation.file_deletion import FileDeletion


class TestDataVisualizer:
    def test_map_correctly(self):
        # create the data visualizer object
        data_visualizer_o = data_visualizer_i.DataVisualizer()

        # read in the test geojson
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/data_visualizer/"))

        # create folder for test file
        deleter: FileDeletion = file_deletion.FileDeletion()
        deleter.reset_folder(project_path)

        assert data_visualizer_o.create_map(geojson_path, project_path, "map.html") == True
        assert os.path.exists(os.path.join(project_path, "map.html"))

    def test_map_invalid_data(self):
        # create the data visualizer object
        data_visualizer_o = data_visualizer_i.DataVisualizer()

        # read in the test geojson
        geojson_path: Path = Path(os.path.join(TEST_DIR, "data/invalid_data.txt"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/data_visualizer/"))

        # create folder for test file
        deleter: FileDeletion = file_deletion.FileDeletion()
        deleter.reset_folder(project_path)

        assert data_visualizer_o.create_map(geojson_path, project_path, "map.html") == False

    def test_boxplot_correctly(self):
        # create the data visualizer object
        data_visualizer_o = data_visualizer_i.DataVisualizer()

        # read in data
        data: Path = Path(os.path.join(TEST_DIR, "data/boxplot_test_data.csv"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/data_visualizer/"))

        # create folder for test file
        deleter: FileDeletion = file_deletion.FileDeletion()
        deleter.reset_folder(project_path)

        assert data_visualizer_o.create_boxplot(data, project_path, "boxplot.png")
        assert os.path.exists(os.path.join(project_path, "boxplot.png"))

    def test_boxplot_invalid_data(self):
        # create the data visualizer object
        data_visualizer_o = data_visualizer_i.DataVisualizer()

        # read in data
        data: Path = Path(os.path.join(TEST_DIR, "data/invalid_data.txt"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/data_visualizer/"))

        # create folder for test file
        deleter: FileDeletion = file_deletion.FileDeletion()
        deleter.reset_folder(project_path)

        assert data_visualizer_o.create_boxplot(data, project_path, "boxplot.png") == False
