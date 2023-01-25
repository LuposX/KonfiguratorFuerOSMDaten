import os

import src.osm_configurator.model.parser.cut_out_parser as cop
from src_tests.definitions import TEST_DIR
from src.osm_configurator.model.parser import dataframe_column_names

from pathlib import Path


def test_correct_parsing():
    geojson_path = os.path.join(TEST_DIR, "data/monaco-regions.geojson")
    parser = cop.CutOutParser()
    df = parser.parse_cutout_file(Path(geojson_path))

    assert df[dataframe_column_names.TRAFFIC_CELL_NAME][3] == "3_traffic_cell"
    assert "7.430574755831088 43.74116219248498" in str(df[dataframe_column_names.GEOMETRY][5])
