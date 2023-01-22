import os.path
from tests.definitions import TEST_DIR

import geopandas as gpd
from pathlib import Path
import src.osm_configurator.model.project.calculation.split_up_files as suf


def _clean_up(result_folder):
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

    df = gpd.read_file(geojson_path)
    split_up = suf.SplitUpFile(Path(origin_path), Path(result_folder))

    did_work = split_up.split_up_files(df["geometry"])
    assert not did_work


def test_illegal_result_folder():
    origin_path = os.path.join(TEST_DIR, "data/monaco-latest.osm.pbf")
    result_folder = os.path.join(TEST_DIR, "build/split_up_filesadadaahsliahfilafiasfga")
    geojson_path = os.path.join(TEST_DIR, "data/monaco-regions.geojson")

    df = gpd.read_file(geojson_path)
    split_up = suf.SplitUpFile(Path(origin_path), Path(result_folder))

    did_work = split_up.split_up_files(df["geometry"])
    assert not did_work


def test_no_name_column():
    # Declare paths
    origin_path = os.path.join(TEST_DIR, "data/monaco-latest.osm.pbf")
    result_folder = os.path.join(TEST_DIR, "build/split_up_files")
    geojson_path = os.path.join(TEST_DIR, "data/monaco-regions.geojson")

    # Clean up last tests
    # Create build directory
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    _clean_up(result_folder)

    # Begin test
    df = gpd.read_file(geojson_path)
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

    _clean_up(result_folder)

    # Begin test
    df = gpd.read_file(geojson_path)
    df["name"] = df.index
    df["name"][2] = "cell_with_a_name"
    split_up = suf.SplitUpFile(Path(origin_path), Path(result_folder))

    did_work = split_up.split_up_files(df)
    assert did_work
    assert os.path.exists(test_file_path1)
    assert os.path.exists(test_file_path2)
