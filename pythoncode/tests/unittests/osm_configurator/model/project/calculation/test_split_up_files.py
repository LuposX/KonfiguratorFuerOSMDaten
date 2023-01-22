import os.path

import geopandas as gpd
from pathlib import Path
import src.osm_configurator.model.project.calculation.split_up_files as suf


def test_illegal_origin_path():
    origin_path = Path("adhadhkaduad/ishlisafglaif.pbf")
    result_folder = Path("../../../../../build/split_up_files")
    geojson_path = Path("../../../../../data/monaco-regions.geojson")

    df = gpd.read_file(geojson_path)
    split_up = suf.SplitUpFile(origin_path, result_folder)

    did_work = split_up.split_up_files(df["geometry"])
    assert not did_work


def test_illegal_result_folder():
    origin_path = Path("../../../../../data/monaco-latest.osm.pbf")
    result_folder = Path("asdiodoadaos/asdhidhaodh")
    geojson_path = Path("../../../../../data/monaco-regions.geojson")

    df = gpd.read_file(geojson_path)
    split_up = suf.SplitUpFile(origin_path, result_folder)

    did_work = split_up.split_up_files(df["geometry"])
    assert not did_work


def test_no_name_column():
    # Declare paths
    origin_path = Path("../../../../../data/monaco-latest.osm.pbf")
    result_folder = Path("../../../../../build/split_up_files")
    geojson_path = Path("../../../../../data/monaco-regions.geojson")
    test_file_path = Path("../../../../../build/split_up_files/3.pbf")

    # Clean up last tests
    # Create build directory
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # Delete old build files
    delete_path = str(result_folder) + '//'
    for file_name in os.listdir(delete_path):
        # construct full file path
        file = delete_path + file_name
        if os.path.isfile(file):
            os.remove(file)

    # Begin test
    df = gpd.read_file(geojson_path)
    split_up = suf.SplitUpFile(origin_path, result_folder)

    did_work = split_up.split_up_files(df)
    assert not did_work


def test_correct_split_up():
    # Declare paths
    origin_path = Path("../../../../../data/monaco-latest.osm.pbf")
    result_folder = Path("../../../../../build/split_up_files")
    geojson_path = Path("../../../../../data/monaco-regions.geojson")
    test_file_path1 = Path("../../../../../build/split_up_files/3.pbf")
    test_file_path2 = Path("../../../../../build/split_up_files/cell_with_a_name.pbf")

    # Clean up last tests
    # Create build directory
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # Delete old build files
    delete_path = str(result_folder) + '//'
    for file_name in os.listdir(delete_path):
        # construct full file path
        file = delete_path + file_name
        if os.path.isfile(file):
            os.remove(file)

    # Begin test
    df = gpd.read_file(geojson_path)
    df["name"] = df.index
    df["name"][2] = "cell_with_a_name"
    split_up = suf.SplitUpFile(origin_path, result_folder)

    did_work = split_up.split_up_files(df)
    assert did_work
    assert os.path.exists(test_file_path1)
    assert os.path.exists(test_file_path2)
