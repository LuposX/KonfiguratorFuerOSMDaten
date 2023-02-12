from __future__ import annotations

from typing import TYPE_CHECKING

from src_tests.definitions import TEST_CATEGORY_SITE_AREA, TEST_DIR, TEST_CATEGORY_BUILDING_AREA, osm_element_1_default_value
import src.osm_configurator.model.model_constants as model_constants_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i
import src.osm_configurator.model.project.configuration.default_value_entry as default_value_entry_i

import os
import geopandas as gpd
import pandas as pd
import shapely as shp

if TYPE_CHECKING:
    from geopandas import GeoSeries, GeoDataFrame
    from typing import Dict

# without this you get a weird error, idk why
os.environ["PROJ_LIB"]=""


class TestAttributeEnumMethods:
    def test_number_of_floors_with_floor_tag_in_it(self):
        osm_element_1_data: Dict = {
            model_constants_i.CL_OSM_TYPE: model_constants_i.NODE_NAME,
            model_constants_i.CL_OSM_ELEMENT_NAME: "neco_arc_house",
            model_constants_i.CL_GEOMETRY: shp.Point((0.0, 0.0)),
            model_constants_i.CL_TAGS: "[('building', 'yes'), ('shop', 'lol213'), ('building:levels', '2')]",
            model_constants_i.CL_CATEGORY: TEST_CATEGORY_SITE_AREA.get_category_name(),
        }

        osm_element_1: GeoSeries = pd.Series(data=osm_element_1_data)

        calculated_value = attribute_enum_i.Attribute.NUMBER_OF_FLOOR.calculate_attribute_value(
            TEST_CATEGORY_SITE_AREA,
            osm_element_1,
            {},
            osm_element_1_default_value,
            None
        )

        assert 2.0 == calculated_value

    def test_number_of_floors_without_right_tag_in_it(self):
        osm_element_1_data: Dict = {
            model_constants_i.CL_OSM_TYPE: model_constants_i.NODE_NAME,
            model_constants_i.CL_OSM_ELEMENT_NAME: "neco_arc_chaos_house",
            model_constants_i.CL_GEOMETRY: shp.Point((0.0, 0.0)),
            model_constants_i.CL_TAGS: "[('building', 'yes'), ('shop', 'butcher')]",
            model_constants_i.CL_CATEGORY: TEST_CATEGORY_SITE_AREA.get_category_name(),
        }

        osm_element_1: GeoSeries = pd.Series(data=osm_element_1_data)

        calculated_value = attribute_enum_i.Attribute.NUMBER_OF_FLOOR.calculate_attribute_value(
            TEST_CATEGORY_SITE_AREA,
            osm_element_1,
            {},
            osm_element_1_default_value,
            None
        )

        assert 1 == calculated_value

    def test_floor_area_correctly(self):
        osm_element_1_data: Dict = {
            model_constants_i.CL_OSM_TYPE: model_constants_i.NODE_NAME,
            model_constants_i.CL_OSM_ELEMENT_NAME: "neco_arc_chaos_house",
            model_constants_i.CL_GEOMETRY: shp.Point((0.0, 0.0)),
            model_constants_i.CL_TAGS:  "[('building', 'yes'), ('shop', 'butcher')]",
            model_constants_i.CL_CATEGORY: TEST_CATEGORY_SITE_AREA.get_category_name(),
        }
        osm_element_1: GeoSeries = pd.Series(data=osm_element_1_data)

        calculated_value = attribute_enum_i.Attribute.FLOOR_AREA.calculate_attribute_value(
            TEST_CATEGORY_SITE_AREA,
            osm_element_1,
            {
                attribute_enum_i.Attribute.NUMBER_OF_FLOOR.get_name(): 5,
                attribute_enum_i.Attribute.PROPERTY_AREA.get_name(): 5,
            },
            osm_element_1_default_value,
            None
        )

        assert 25 == calculated_value

    def test_property_area_correctly_with_node(self):
        osm_element_1_data: Dict = {
            model_constants_i.CL_OSM_TYPE: model_constants_i.NODE_NAME,
            model_constants_i.CL_OSM_ELEMENT_NAME: "Zhang Yongラーメンを落とす",
            model_constants_i.CL_GEOMETRY: shp.Point((0.0, 0.0)),
            model_constants_i.CL_TAGS: "[('building', 'yes'), ('song', 'Red Sun Sky')]",
            model_constants_i.CL_CATEGORY: TEST_CATEGORY_SITE_AREA.get_category_name(),
        }

        osm_element_1: GeoSeries = pd.Series(data=osm_element_1_data)

        calculated_value = attribute_enum_i.Attribute.PROPERTY_AREA.calculate_attribute_value(
            TEST_CATEGORY_SITE_AREA,
            osm_element_1,
            {},
            osm_element_1_default_value,
            None
        )

        assert 1 == calculated_value

    def test_property_area_correctly_with_polygon_and_site_area(self):
        osm_element_1_data: Dict = {
            model_constants_i.CL_OSM_TYPE: model_constants_i.AREA_WAY_NAME,
            model_constants_i.CL_OSM_ELEMENT_NAME: "奧的斯電梯公司",
            model_constants_i.CL_GEOMETRY: shp.Polygon([(0, 0), (1, 1), (1, 0)]),
            model_constants_i.CL_TAGS: "[('building', 'yes'), ('pepe', 'rare_pepe')]",
            model_constants_i.CL_CATEGORY: TEST_CATEGORY_SITE_AREA.get_category_name(),
        }

        osm_element_1: GeoSeries = pd.Series(data=osm_element_1_data)

        calculated_value = attribute_enum_i.Attribute.PROPERTY_AREA.calculate_attribute_value(
            TEST_CATEGORY_SITE_AREA,
            osm_element_1,
            {},
            osm_element_1_default_value,
            None
        )
        assert 0.5 == calculated_value

    def test_property_area_correctly_with_polygon_and_building_area(self):
        # read int the data
        df: GeoDataFrame = gpd.read_file(os.path.join(TEST_DIR, "data/reduction_test_property_area.csv"),
                                         GEOM_POSSIBLE_NAMES=model_constants_i.CL_GEOMETRY,
                                         KEEP_GEOM_COLUMNS="NO")

        osm_element_1_data: Dict = {
            model_constants_i.CL_OSM_TYPE: model_constants_i.AREA_WAY_NAME,
            model_constants_i.CL_OSM_ELEMENT_NAME: "奧的斯電梯公司",
            model_constants_i.CL_GEOMETRY: shp.Polygon([(0, 0), (0, 10), (10, 10), (10,0), (0,0)]),
            model_constants_i.CL_TAGS: "[('building', 'yes'), ('pepe', 'rare_pepe')]",
            model_constants_i.CL_CATEGORY: TEST_CATEGORY_BUILDING_AREA.get_category_name(),
        }

        osm_element_1: GeoSeries = pd.Series(data=osm_element_1_data)

        calculated_value = attribute_enum_i.Attribute.PROPERTY_AREA.calculate_attribute_value(
            TEST_CATEGORY_BUILDING_AREA,
            osm_element_1,
            {},
            osm_element_1_default_value,
            df
        )
        assert 100.0 == calculated_value


