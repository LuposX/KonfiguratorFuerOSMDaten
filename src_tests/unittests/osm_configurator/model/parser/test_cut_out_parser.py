from __future__ import annotations

from typing import TYPE_CHECKING

import os

import src.osm_configurator.model.parser.cut_out_parser as cop
from src_tests.definitions import TEST_DIR, MONACO_TRAFFIC_CELL_0_POLYGON, MONACO_TRAFFIC_CELL_1_POLYGON
from src.osm_configurator.model.parser import dataframe_column_names

from src.osm_configurator.model.parser.custom_exceptions.illegal_cut_out_exception import IllegalCutOutException
from pathlib import Path
import shapely as shp

if TYPE_CHECKING:
    from src.osm_configurator.model.parser.cut_out_parser_interface import CutOutParserInterface
    from geopandas import GeoDataFrame


# without this you get a weird error, idk why
os.environ["PROJ_LIB"] = ""


def test_correct_parsing():
    geojson_path: Path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
    parser: CutOutParserInterface = cop.CutOutParser()
    df: GeoDataFrame = parser.parse_cutout_file(geojson_path)

    # Test non generated names
    assert df[dataframe_column_names.TRAFFIC_CELL_NAME][0] == "0_super_traffic_cell"
    assert df[dataframe_column_names.TRAFFIC_CELL_NAME][1] == "1_the_funny_cat"

    # Test auto generated names
    assert df[dataframe_column_names.TRAFFIC_CELL_NAME][2] == "2_traffic_cell"
    assert df[dataframe_column_names.TRAFFIC_CELL_NAME][3] == "3_traffic_cell"

    # Test parsed geometry
    assert MONACO_TRAFFIC_CELL_0_POLYGON == df[dataframe_column_names.GEOMETRY][0]
    assert MONACO_TRAFFIC_CELL_1_POLYGON == df[dataframe_column_names.GEOMETRY][1]
    assert "7.430574755831088 43.74116219248498" in str(df[dataframe_column_names.GEOMETRY][5])


def test_illegal_path():
    geojson_path: Path = Path(os.path.join(TEST_DIR, "data/asassa/sdjladlas.geojson"))
    parser: CutOutParserInterface = cop.CutOutParser()
    try:
        parser.parse_cutout_file(geojson_path)
    except IllegalCutOutException as err:
        return

    assert False


def test_none_path():
    geojson_path: Path = Path(os.path.join(TEST_DIR))
    parser = cop.CutOutParser()
    try:
        df = parser.parse_cutout_file(geojson_path)
    except IllegalCutOutException as err:
        return

    assert False
