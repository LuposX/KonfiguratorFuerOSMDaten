import src.osm_configurator.model.parser.osm_data_handler as osm_data_handler_i

from src_tests.definitions import CATEGORY_MANAGER, MONACO_TRAFFIC_CELL_0_POLYGON,MONACO_TRAFFIC_CELL_1_POLYGON, TEST_DIR

import os


def test_osm_data_handler():
    osm_data_handler = osm_data_handler_i.DataOSMHandler(CATEGORY_MANAGER, MONACO_TRAFFIC_CELL_0_POLYGON)

    test_data_path = os.path.join(TEST_DIR, "data/monaco_split_up_files/0_super_traffic_cell.pbf")
    osm_data_handler.apply_file(test_data_path)

    test_osm_data = osm_data_handler.get_osm_data()

    # Checks that the list is not empty
    assert test_osm_data

    osm_data_handler = osm_data_handler_i.DataOSMHandler(CATEGORY_MANAGER, MONACO_TRAFFIC_CELL_1_POLYGON)

    test_data_path = os.path.join(TEST_DIR, "data/monaco_split_up_files/1_the_funny_cat.pbf")
    osm_data_handler.apply_file(test_data_path)

    test_osm_data = osm_data_handler.get_osm_data()

    # Checks that the list is not empty
    assert test_osm_data

