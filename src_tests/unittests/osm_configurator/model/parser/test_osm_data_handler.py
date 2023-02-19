import src.osm_configurator.model.parser.osm_data_handler as osm_data_handler_i

from src_tests.definitions import CATEGORY_MANAGER, MONACO_TRAFFIC_CELL_0_POLYGON,MONACO_TRAFFIC_CELL_1_POLYGON, TEST_DIR

import os

# without this you get a weird error, idk why
os.environ["PROJ_LIB"]=""


def test_osm_data_handler():
    # you can't test here much besides that list ist not empty because data is still in raw format
    # all the important test will be in the test file for the "osm_data_parser" instead, because there
    # we processed the raw format to a better accessible format.
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

