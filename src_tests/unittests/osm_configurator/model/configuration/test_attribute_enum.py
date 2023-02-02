from __future__ import annotations

from typing import TYPE_CHECKING


from src_tests.definitions import TEST_CATEGORY_BUILDING
import src.osm_configurator.model.model_constants as model_constants_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i
import src.osm_configurator.model.project.configuration.default_value_entry as default_value_entry_i

import pandas as pd
import geopandas as gpd
import shapely as shp

if TYPE_CHECKING:
    from geopandas import GeoDataFrame, GeoSeries
    from typing import Dict


class TestAttributeEnumMethods:
    def test_number_of_floors_with_floor_tag_in_it(self):
        osm_element_1_data: Dict = {
            model_constants_i.CL_OSM_TYPE: model_constants_i.NODE_NAME,
            model_constants_i.CL_OSM_ELEMENT_NAME: "neco_arc_house",
            model_constants_i.CL_GEOMETRY: shp.Point((0.0, 0.0)),
            model_constants_i.CL_TAGS: ["building=yes", "shop=butcher", "building:levels=2"],
            model_constants_i.CL_CATEGORY: TEST_CATEGORY_BUILDING.get_category_name(),
        }
        osm_element_1_default_value = default_value_entry_i.DefaultValueEntry()
        osm_element_1_default_value.set_attribute_default(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, 0)

        osm_element_1: GeoSeries = pd.Series(data=osm_element_1_data)

        calculated_value = attribute_enum_i.Attribute.NUMBER_OF_FLOOR.calculate_attribute_value(
            TEST_CATEGORY_BUILDING,
            osm_element_1,
            {},
            osm_element_1_default_value,
            None
        )

        assert 2.0 == calculated_value

    def test_number_of_floors_without_right_tag_in_it(self):
        osm_element_1_data: Dict = {
            model_constants_i.CL_OSM_TYPE: model_constants_i.NODE_NAME,
            model_constants_i.CL_OSM_ELEMENT_NAME: "neco_arc_house",
            model_constants_i.CL_GEOMETRY: shp.Point((0.0, 0.0)),
            model_constants_i.CL_TAGS: ["building=yes", "shop=butcher"],
            model_constants_i.CL_CATEGORY: TEST_CATEGORY_BUILDING.get_category_name(),
        }
        osm_element_1_default_value = default_value_entry_i.DefaultValueEntry()
        osm_element_1_default_value.set_attribute_default(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, 0)

        osm_element_1: GeoSeries = pd.Series(data=osm_element_1_data)

        calculated_value = attribute_enum_i.Attribute.NUMBER_OF_FLOOR.calculate_attribute_value(
            TEST_CATEGORY_BUILDING,
            osm_element_1,
            {},
            osm_element_1_default_value,
            None
        )

        assert 0 == calculated_value
