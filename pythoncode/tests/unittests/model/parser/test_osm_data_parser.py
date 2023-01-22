
import src.osm_configurator.model.parser.osm_data_parser as osm_data_parser
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum
import src.osm_configurator.model.project.configuration.category_manager as category_manager
import src.osm_configurator.model.project.configuration.category as category

import pathlib
import geopandas as gpd


class TestOSMDataParser:
    def test_parse_osm_data_file(self):
        osm_parser = osm_data_parser.OSMDataParser()
        category_example = category.Category()

        category_example.set_whitelist(["Building=yes"])
        category_example.set_category_name("test_Category")

        assert osm_parser is not None
        assert category_example is not None

        category_manager_o = category_manager.CategoryManager(category_example)

        assert category_manager_o is not None

        osm_data_path = pathlib.Path("data/andorra-latest.osm.pbf").resolve()

        assert osm_data_path is not None

        dataframe = osm_parser.parse_osm_data_file(osm_data_path, category_manager_o,
                                                   [attribute_enum.Attribute.FIRST_FLOOR_AREA,
                                                    attribute_enum.Attribute.NUMER_OF_FLOOR])

        assert dataframe is not None
        assert isinstance(dataframe, gpd.GeoDataFrame)
        assert not dataframe.empty
