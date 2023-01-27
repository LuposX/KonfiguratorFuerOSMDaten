import os

import src.osm_configurator.model.parser.cut_out_parser as cop
from src_tests.definitions import TEST_DIR, MONACO_TRAFFIC_CELL_0_POLYGON, MONACO_TRAFFIC_CELL_1_POLYGON
from osm_configurator.model import model_constants

from pathlib import Path

# without this you get a weird error, idk why
os.environ["PROJ_LIB"]=""


def test_correct_parsing():
    geojson_path = os.path.join(TEST_DIR, "data/monaco-regions.geojson")
    parser = cop.CutOutParser()
    df = parser.parse_cutout_file(Path(geojson_path))

    # Test non generated names
    assert df[model_constants.CL_TRAFFIC_CELL_NAME][0] == "0_super_traffic_cell"
    assert df[model_constants.CL_TRAFFIC_CELL_NAME][1] == "1_the_funny_cat"

    # Test auto generated names
    assert df[model_constants.CL_TRAFFIC_CELL_NAME][2] == "2_traffic_cell"
    assert df[model_constants.CL_TRAFFIC_CELL_NAME][3] == "3_traffic_cell"

    # Test parsed geometry
    assert MONACO_TRAFFIC_CELL_0_POLYGON == df[model_constants.CL_GEOMETRY][0]
    assert MONACO_TRAFFIC_CELL_1_POLYGON == df[model_constants.CL_GEOMETRY][1]
    assert "7.430574755831088 43.74116219248498" in str(df[model_constants.CL_GEOMETRY][5])
