import os.path
from src_tests.definitions import TEST_DIR

from pathlib import Path
import src.osm_configurator.model.project.calculation.osm_file_converter as ofc
import src.osm_configurator.model.project.calculation.osm_file_format_enum as offe


def _prepare(target_path):
    result_folder = os.path.dirname(target_path)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    if os.path.exists(target_path):
        os.remove(target_path)


def test_correct_convert_pbf_to_osm():
    origin_path = os.path.join(TEST_DIR, "data/monaco-latest.osm.pbf")
    target_path = os.path.join(TEST_DIR, "build/osm_file_converter/monaco-latest.osm")

    _prepare(target_path)

    converter = ofc.OSMFileConverter(Path(origin_path), Path(target_path))
    assert converter.convert_file(offe.OSMFileFormat.OSM)
    assert os.path.exists(target_path)
    assert os.path.getsize(target_path) != 0


def test_correct_convert_osm_to_pbf():
    origin_path = os.path.join(TEST_DIR, "data/monaco-latest.osm")
    target_path = os.path.join(TEST_DIR, "build/osm_file_converter/monaco-latest.osm.pbf")

    _prepare(target_path)
    assert not os.path.exists(target_path)
    assert os.path.exists(origin_path)

    converter = ofc.OSMFileConverter(Path(origin_path), Path(target_path))
    assert converter.convert_file(offe.OSMFileFormat.PBF)
    assert os.path.exists(target_path)
    assert os.path.getsize(target_path) != 0


def test_wrong_format():
    origin_path = os.path.join(TEST_DIR, "data/monaco-latest.osm.pbf")
    target_path = os.path.join(TEST_DIR, "build/osm_file_converter/monaco-latest.osm")

    _prepare(target_path)

    converter = ofc.OSMFileConverter(Path(origin_path), Path(target_path))
    assert not converter.convert_file(offe.OSMFileFormat.PBF)


def test_illegal_origin_path():
    origin_path = os.path.join(TEST_DIR, "data/monacoasasdasduiasdiasdasidazs-latest.osm.pbf")
    target_path = os.path.join(TEST_DIR, "build/osm_file_converter/monaco-latest.osm")

    _prepare(target_path)

    converter = ofc.OSMFileConverter(Path(origin_path), Path(target_path))
    assert not converter.convert_file(offe.OSMFileFormat.OSM)
