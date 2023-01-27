import src.osm_configurator.model.parser.osm_data_handler as osm_data_handler_i

from src_tests.definitions import CATEGORY_MANAGER, MONACO_TRAFFIC_CELL_1_POLYGON


def test_osm_data_handler():
    osm_data_handler = osm_data_handler_i.DataOSMHandler(CATEGORY_MANAGER, MONACO_TRAFFIC_CELL_1_POLYGON)

    osm_data_handler.apply_file(PLACEHOLDER)

    test = osm_data_handler.get_osm_data()

    assert test != None
    assert test