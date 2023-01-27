import src.osm_configurator.model.parser.osm_data_handler as osm_data_handler_i

from src_tests.definitions import CATEGORY_MANAGER, MONACO_TRAFFIC_CELL_1_POLYGON, TEST_DIR


def test_osm_data_handler():
    osm_data_handler = osm_data_handler_i.DataOSMHandler(CATEGORY_MANAGER, MONACO_TRAFFIC_CELL_1_POLYGON)

    osm_data_handler.apply_file(TEST_DIR.join("data/monaco_split_up_files/0_super_traffic_cell.pbf"))

    test_osm_data = osm_data_handler.get_osm_data()

    # Checks that the list is not empty
    assert test_osm_data

    osm_data_handler.apply_file(TEST_DIR.join("data/monaco_split_up_files/1_the_funny_cat.pbf"))

    test_osm_data = osm_data_handler.get_osm_data()

    # Checks that the list is not empty
    assert test_osm_data

