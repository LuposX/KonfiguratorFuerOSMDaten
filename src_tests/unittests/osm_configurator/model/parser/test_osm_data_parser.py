
import src.osm_configurator.model.parser.osm_data_parser as osm_data_parser_i

from src_tests.definitions import CATEGORY_MANAGER, MONACO_TRAFFIC_CELL_1_POLYGON, TEST_DIR

class TestOSMDataParser:
    def test_parse_osm_data_file(self):
        osm_parser = osm_data_parser_i.OSMDataParser()

        test_data_path = os.path.join(TEST_DIR, "data/monaco_split_up_files/0_super_traffic_cell.pbf")

        osm_parser.parse_osm_data_file()

