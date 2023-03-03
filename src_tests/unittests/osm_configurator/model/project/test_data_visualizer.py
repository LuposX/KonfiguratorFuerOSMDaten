from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd

from src_tests.definitions import TEST_DIR
import src.osm_configurator.model.project.data_visualizer as data_visualizer_i
import src.osm_configurator.model.project.calculation.file_deletion as file_deletion

import pytest

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
        project_path: Path = Path(os.path.join(TEST_DIR, "build/data_visualizer_map/"))

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
        project_path: Path = Path(os.path.join(TEST_DIR, "build/data_visualizer_map/"))

        # create folder for test file
        deleter: FileDeletion = file_deletion.FileDeletion()
        deleter.reset_folder(project_path)

        assert data_visualizer_o.create_map(geojson_path, project_path, "map.html") == False

    def test_boxplot_correctly(self):
        # create the data visualizer object
        data_visualizer_o = data_visualizer_i.DataVisualizer()

        # read in data
        data: Path = Path(os.path.join(TEST_DIR, "data/data_visualizer/"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/data_visualizer/"))

        # create folder for test file
        deleter: FileDeletion = file_deletion.FileDeletion()
        deleter.reset_folder(project_path)

        assert data_visualizer_o.create_boxplot(data, project_path)

    def test_boxplot_wrongly(self):
        # create the data visualizer object
        data_visualizer_o = data_visualizer_i.DataVisualizer()

        # read in data
        data: Path = Path(os.path.join(TEST_DIR, "data/data_visualizer_invalid/"))
        project_path: Path = Path(os.path.join(TEST_DIR, "build/data_visualizer/"))

        # create folder for test file
        deleter: FileDeletion = file_deletion.FileDeletion()
        deleter.reset_folder(project_path)

        assert data_visualizer_o.create_boxplot(data, project_path) == False
