import os.path
from src_tests.definitions import TEST_DIR

import geopandas as gpd
from pathlib import Path
import src.osm_configurator.model.project.calculation.split_up_files as suf
import src.osm_configurator.model.model_constants as model_constants


def _prepare(result_folder):
    # Create output folders
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # Delete old build files
    delete_path = str(result_folder) + '//'
    for file_name in os.listdir(delete_path):
        # construct full file path
        file = delete_path + file_name
        if os.path.isfile(file):
            os.remove(file)


def test_illegal_origin_path():
    origin_path = os.path.join(TEST_DIR, "data/monaco-lasugpisaipfgafggoafgasfgatest.osm.pbf")
    result_folder = os.path.join(TEST_DIR, "build/split_up_files")
    geojson_path = os.path.join(TEST_DIR, "data/monaco-regions.geojson")

    df = gpd.read_file(geojson_path,
                       GEOM_POSSIBLE_NAMES=model_constants.CL_GEOMETRY,
                       KEEP_GEOM_COLUMNS="NO"
                       )
    split_up = suf.SplitUpFile(Path(origin_path), Path(result_folder))

    did_work = split_up.split_up_files(df[model_constants.CL_GEOMETRY])
    assert not did_work


def test_illegal_result_folder():
    origin_path = os.path.join(TEST_DIR, "data/monaco-latest.osm.pbf")
    result_folder = os.path.join(TEST_DIR, "build/split_up_filesadadaahsliahfilafiasfga")
    geojson_path = os.path.join(TEST_DIR, "data/monaco-regions.geojson")

    df = gpd.read_file(geojson_path,
                       GEOM_POSSIBLE_NAMES=model_constants.CL_GEOMETRY,
                       KEEP_GEOM_COLUMNS="NO"
                       )
    split_up = suf.SplitUpFile(Path(origin_path), Path(result_folder))

    did_work = split_up.split_up_files(df[model_constants.CL_GEOMETRY])
    assert not did_work


def test_no_name_column():
    # Declare paths
    origin_path = os.path.join(TEST_DIR, "data/monaco-latest.osm.pbf")
    result_folder = os.path.join(TEST_DIR, "build/split_up_files")
    geojson_path = os.path.join(TEST_DIR, "data/monaco-regions.geojson")

    # Clean up last src_tests
    _prepare(result_folder)

    # Begin test
    df = gpd.read_file(geojson_path,
                       GEOM_POSSIBLE_NAMES=model_constants.CL_GEOMETRY,
                       KEEP_GEOM_COLUMNS="NO"
                       )
    split_up = suf.SplitUpFile(Path(origin_path), Path(result_folder))

    did_work = split_up.split_up_files(df)
    assert not did_work


def test_correct_split_up():
    # Declare paths
    origin_path = os.path.join(TEST_DIR, "data/monaco-latest.osm.pbf")
    result_folder = os.path.join(TEST_DIR, "build/split_up_files")
    geojson_path = os.path.join(TEST_DIR, "data/monaco-regions.geojson")
    test_file_path1 = os.path.join(TEST_DIR, "build/split_up_files/3.pbf")
    test_file_path2 = os.path.join(TEST_DIR, "build/split_up_files/cell_with_a_name.pbf")

    _prepare(result_folder)

    # Begin test
    df = gpd.read_file(geojson_path,
                       GEOM_POSSIBLE_NAMES=model_constants.CL_GEOMETRY,
                       KEEP_GEOM_COLUMNS="NO"
                       )
    df[model_constants.CL_TRAFFIC_CELL_NAME] = df.index
    df[model_constants.CL_TRAFFIC_CELL_NAME][2] = "cell_with_a_name"
    split_up = suf.SplitUpFile(Path(origin_path), Path(result_folder))

    did_work = split_up.split_up_files(df)
    assert did_work
    assert os.path.exists(test_file_path1)
    assert os.path.exists(test_file_path2)
