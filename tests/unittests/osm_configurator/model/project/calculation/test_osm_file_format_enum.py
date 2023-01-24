import src.osm_configurator.model.project.calculation.osm_file_format_enum as format


def test_get_file_extension():
    assert format.OSMFileFormat.PBF.get_file_extension() == ".pbf"
    assert format.OSMFileFormat.BZ2.get_file_extension() == ".bz2"
    assert format.OSMFileFormat.OSM.get_file_extension() == ".osm"
