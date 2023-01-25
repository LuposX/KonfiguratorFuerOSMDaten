import os

from ......src.osm_configurator.model.parser.cut_out_parser import CutOutParser
from ......src_tests.definitions import TEST_DIR

import pyth


from pathlib import Path


def test_correct_parsing():
    geojson_path = os.path.join(TEST_DIR, "data/monaco-regions.geojson")
    parser = CutOutParser()
    df = parser.parse_cutout_file(Path(geojson_path))
    assert df["name"][3] == 3
    assert "7.430574755831088 43.74116219248498" in str(df["geometry"][5])
