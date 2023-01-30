import os
import pytest

from pathlib import Path

import src.osm_configurator.model.parser.osm_data_parser as osm_data_parser_i
import src.osm_configurator.model.project.configuration.cut_out_mode_enum as cut_out_mode_enum_i

from src_tests.definitions import CATEGORY_MANAGER, \
    MONACO_TRAFFIC_CELL_1_POLYGON, \
    TEST_DIR, \
    TEST_CATEGORY_SHOP, \
    TEST_CATEGORY_NO_BUILDING, \
    TEST_CATEGORY_BUILDING

from src.osm_configurator.model.model_constants import CL_OSM_ELEMENT_NAME, CL_CATEGORY

# without this you get a weird error, idk why
os.environ["PROJ_LIB"]=""

class TestOSMDataParser:
    def test_parse_osm_data_file(self):
        osm_parser = osm_data_parser_i.OSMDataParser()

        test_data_path = Path(os.path.join(TEST_DIR, "data/monaco_split_up_files/0_super_traffic_cell.pbf"))
        test_cutout_path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
        saving_location_path = Path(os.path.join(TEST_DIR, "build/osm_data_parser/output.csv"))

        parsed_data_df = osm_parser.parse_osm_data_file(test_data_path, CATEGORY_MANAGER,
                                                     cut_out_mode_enum_i.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED,
                                                     test_cutout_path)

        assert parsed_data_df is not None

        # Building which are fully inside
        assert "Église Saint-Nicolas" in parsed_data_df[CL_OSM_ELEMENT_NAME].tolist()
        assert TEST_CATEGORY_BUILDING.get_category_name() in \
               parsed_data_df[parsed_data_df[CL_OSM_ELEMENT_NAME] == "Église Saint-Nicolas"][CL_CATEGORY].item()

        assert "L'Aigue Marine"  in parsed_data_df[CL_OSM_ELEMENT_NAME].tolist()
        assert TEST_CATEGORY_BUILDING.get_category_name() in \
               parsed_data_df[parsed_data_df[CL_OSM_ELEMENT_NAME] == "L'Aigue Marine"][CL_CATEGORY].item()

        assert "Monaco Mutualité" in parsed_data_df[CL_OSM_ELEMENT_NAME].tolist()
        assert TEST_CATEGORY_SHOP.get_category_name() in \
               parsed_data_df[parsed_data_df[CL_OSM_ELEMENT_NAME] == "Monaco Mutualité"][CL_CATEGORY].item()


        # Buildings which lie on the edge
        assert "Le Mantegna" in parsed_data_df[CL_OSM_ELEMENT_NAME].tolist()
        assert TEST_CATEGORY_BUILDING.get_category_name() in \
               parsed_data_df[parsed_data_df[CL_OSM_ELEMENT_NAME] == "Le Mantegna"][CL_CATEGORY].item()

        assert "Le Magellan - Bât. A-F" in parsed_data_df[CL_OSM_ELEMENT_NAME].tolist()
        assert TEST_CATEGORY_BUILDING.get_category_name() in \
               parsed_data_df[parsed_data_df[CL_OSM_ELEMENT_NAME] == "Le Magellan - Bât. A-F"][CL_CATEGORY].item()

        assert "Héliport de Monaco" in parsed_data_df[CL_OSM_ELEMENT_NAME].tolist()
        assert TEST_CATEGORY_NO_BUILDING.get_category_name() in \
               parsed_data_df[parsed_data_df[CL_OSM_ELEMENT_NAME] == "Héliport de Monaco"][CL_CATEGORY].iloc[0]

    def test_parse_osm_data_file_with_edge_detection(self):
        osm_parser = osm_data_parser_i.OSMDataParser()

        test_data_path = Path(os.path.join(TEST_DIR, "data/monaco_split_up_files/0_super_traffic_cell.pbf"))
        test_cutout_path = Path(os.path.join(TEST_DIR, "data/monaco-regions.geojson"))
        saving_location_path = Path(os.path.join(TEST_DIR, "build/osm_data_parser/output.csv"))

        parsed_data_df = osm_parser.parse_osm_data_file(test_data_path, CATEGORY_MANAGER,
                                                        cut_out_mode_enum_i.CutOutMode.BUILDINGS_ON_EDGE_ACCEPTED,
                                                        test_cutout_path)

        assert parsed_data_df is not None

        # Building which are fully inside
        assert "Église Saint-Nicolas" in parsed_data_df[CL_OSM_ELEMENT_NAME].tolist()
        assert TEST_CATEGORY_BUILDING.get_category_name() in \
               parsed_data_df[parsed_data_df[CL_OSM_ELEMENT_NAME] == "Église Saint-Nicolas"][CL_CATEGORY].item()

        assert "L'Aigue Marine" in parsed_data_df[CL_OSM_ELEMENT_NAME].tolist()
        assert TEST_CATEGORY_BUILDING.get_category_name() in \
               parsed_data_df[parsed_data_df[CL_OSM_ELEMENT_NAME] == "L'Aigue Marine"][CL_CATEGORY].item()

        # Buildings which lie on the edge
        assert "Le Mantegna" not in parsed_data_df[CL_OSM_ELEMENT_NAME].tolist()
        assert "Le Magellan - Bât. A-F" not in parsed_data_df[CL_OSM_ELEMENT_NAME].tolist()
        assert "Héliport de Monaco" not in parsed_data_df[CL_OSM_ELEMENT_NAME].tolist()

    def test_saving_of_file(self):
        # Test the saving of a file.
        osm_parser = osm_data_parser_i.OSMDataParser()

        test_data_path = os.path.join(TEST_DIR, "data/monaco_split_up_files/0_super_traffic_cell.pbf")
        test_cutout_path = os.path.join(TEST_DIR, "data/monaco-regions.geojson")
        saving_location_path = os.path.join(TEST_DIR, "build/osm_data_parser/output.csv")

        parsed_data_df = osm_parser.parse_osm_data_file(test_data_path, CATEGORY_MANAGER,
                                                     cut_out_mode_enum_i.CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED,
                                                     test_cutout_path)

        # save result for inspection
        with pytest.raises(Exception) as e:
            parsed_data_df.to_csv(saving_location_path, exist_ok=True)