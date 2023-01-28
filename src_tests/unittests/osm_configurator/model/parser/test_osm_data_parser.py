import os

import src.osm_configurator.model.parser.osm_data_parser as osm_data_parser_i
import src.osm_configurator.model.project.configuration.cut_out_mode_enum as cut_out_mode_enum_i

from src_tests.definitions import CATEGORY_MANAGER, MONACO_TRAFFIC_CELL_1_POLYGON, TEST_DIR


class TestOSMDataParser:
    def test_parse_osm_data_file(self):
        osm_parser = osm_data_parser_i.OSMDataParser()

        test_data_path = os.path.join(TEST_DIR, "data/monaco_split_up_files/0_super_traffic_cell.pbf")
        test_cutout_path = os.path.join(TEST_DIR, "data/monaco-regions.geojson")

        parsed_data = osm_parser.parse_osm_data_file(test_data_path, CATEGORY_MANAGER,
                                                     cut_out_mode_enum_i.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED,
                                                     test_cutout_path)

        assert parsed_data

