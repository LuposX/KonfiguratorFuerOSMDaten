from __future__ import annotations

import os
import shapely as shp

import src.osm_configurator.model.project.configuration.category as category_i
import src.osm_configurator.model.project.configuration.category_manager as category_manager_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i
import src.osm_configurator.model.project.configuration.attractivity_attribute as attractivity_attribute

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final
    from typing import List

# DO NOT CHANGE THE MONACO CUTOUT-FILE, CUTOUT-PARSER DEPENDS ON IT
# -----------------------------------------------------------------
# This file is here, so you can easily define path relative to here

# Defining Test Categories
# -------------------------
name: str = "building_category"
whitelist: List = ["building=*"]
TEST_CATEGORY_BUILDING: Final = category_i.Category()
TEST_CATEGORY_BUILDING.set_category_name(name)
TEST_CATEGORY_BUILDING.set_whitelist(whitelist)
TEST_CATEGORY_BUILDING.set_attribute(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, True)

name: str = "no_building_category"
blacklist: List = ["building=*"]
TEST_CATEGORY_NO_BUILDING: Final = category_i.Category()
TEST_CATEGORY_NO_BUILDING.set_category_name(name)
TEST_CATEGORY_NO_BUILDING.set_blacklist(blacklist)
TEST_CATEGORY_BUILDING.set_attribute(attribute_enum_i.Attribute.FLOOR_AREA, True)

name: str = "shop_category"
blacklist: List = ["shop=*"]
TEST_CATEGORY_SHOP: Final = category_i.Category()
TEST_CATEGORY_SHOP.set_category_name(name)
TEST_CATEGORY_SHOP.set_whitelist(blacklist)
TEST_CATEGORY_BUILDING.set_attribute(attribute_enum_i.Attribute.PROPERTY_AREA, True)

# Define attractivity attributes
TEST_ATTRACTIVITY_COOLNESS: Final = attractivity_attribute.AttractivityAttribute("coolness", 0)
TEST_ATTRACTIVITY_COOLNESS.set_attribute_factor(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, 1)
TEST_ATTRACTIVITY_COOLNESS.set_attribute_factor(attribute_enum_i.Attribute.FLOOR_AREA, 1)
TEST_ATTRACTIVITY_COOLNESS.set_attribute_factor(attribute_enum_i.Attribute.PROPERTY_AREA, 0)

TEST_ATTRACTIVITY_TRADING: Final = attractivity_attribute.AttractivityAttribute("trading", 100)
TEST_ATTRACTIVITY_TRADING.set_attribute_factor(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, 1)
TEST_ATTRACTIVITY_TRADING.set_attribute_factor(attribute_enum_i.Attribute.FLOOR_AREA, 2)
TEST_ATTRACTIVITY_TRADING.set_attribute_factor(attribute_enum_i.Attribute.PROPERTY_AREA, 3)

TEST_ATTRACTIVITY_TRADING2: Final = attractivity_attribute.AttractivityAttribute("trading", 42)
TEST_ATTRACTIVITY_TRADING2.set_attribute_factor(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, 0)
TEST_ATTRACTIVITY_TRADING2.set_attribute_factor(attribute_enum_i.Attribute.FLOOR_AREA, 0)
TEST_ATTRACTIVITY_TRADING2.set_attribute_factor(attribute_enum_i.Attribute.PROPERTY_AREA, 0)

# Set attractivities of categories
TEST_CATEGORY_BUILDING.add_attractivity_attribute(TEST_ATTRACTIVITY_COOLNESS)
TEST_CATEGORY_BUILDING.add_attractivity_attribute(TEST_ATTRACTIVITY_TRADING)
TEST_CATEGORY_NO_BUILDING.add_attractivity_attribute(TEST_ATTRACTIVITY_TRADING2)
TEST_CATEGORY_SHOP.add_attractivity_attribute(TEST_ATTRACTIVITY_COOLNESS)


# Defining Test Category Manager
# -------------------------
CATEGORY_MANAGER = category_manager_i.CategoryManager()
CATEGORY_MANAGER._test_set_categories([TEST_CATEGORY_BUILDING, TEST_CATEGORY_NO_BUILDING, TEST_CATEGORY_SHOP])


# The Test folder
# ---------------
TEST_DIR: Final = os.path.dirname(os.path.abspath(__file__))

# Test polygons of the cutout file, monaco-regions
# ------------------------------------------------
MONACO_TRAFFIC_CELL_0_POLYGON: Final = shp.Polygon([
                  [
                     7.409700947088794,
                     43.72969622483768
                  ],
                  [
                     7.418184746547723,
                     43.725109223058496
                  ],
                  [
                     7.421541645615264,
                     43.72731455621883
                  ],
                  [
                     7.4208702658017955,
                     43.728196666749454
                  ],
                  [
                     7.418245781075996,
                     43.7286377171431
                  ],
                  [
                     7.416231641636699,
                     43.73040188624182
                  ],
                  [
                     7.4154381927665725,
                     43.731107539331504
                  ],
                  [
                     7.4129968116268685,
                     43.73123984836025
                  ],
                  [
                     7.411348879357234,
                     43.731151642373845
                  ],
                  [
                     7.409700947088794,
                     43.72969622483768
                  ]
               ])

MONACO_TRAFFIC_CELL_1_POLYGON: Final = shp.Polygon([
                  [
                     7.426912684122129,
                     43.73542948309182
                  ],
                  [
                     7.427034753178759,
                     43.73401827044526
                  ],
                  [
                     7.4240440612832685,
                     43.7341064722097
                  ],
                  [
                     7.422701301656247,
                     43.73335675306919
                  ],
                  [
                     7.421602680143565,
                     43.731195745383275
                  ],
                  [
                     7.421724749200109,
                     43.72943159966778
                  ],
                  [
                     7.425753028079981,
                     43.7295198081878
                  ],
                  [
                     7.4295982033749794,
                     43.73137215709673
                  ],
                  [
                     7.432100619042956,
                     43.73432697605327
                  ],
                  [
                     7.432466826213897,
                     43.73714935354025
                  ],
                  [
                     7.426912684122129,
                     43.73542948309182
                  ]
               ])