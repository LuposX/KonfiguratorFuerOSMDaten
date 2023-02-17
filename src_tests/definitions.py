from __future__ import annotations

import os
import pathlib

import shapely as shp

import src.osm_configurator.model.project.configuration.category as category_i
import src.osm_configurator.model.project.configuration.category_manager as category_manager_i
import src.osm_configurator.model.project.configuration.attribute_enum as attribute_enum_i
import src.osm_configurator.model.project.configuration.calculation_method_of_area_enum as calculation_method_of_area_enum_i
import src.osm_configurator.model.project.configuration.default_value_entry as default_value_entry_i
import src.osm_configurator.model.project.configuration.attractivity_attribute as attractivity_attribute

import src.osm_configurator.model.application.application_settings as application_settings
import src.osm_configurator.model.application.application_settings_default_enum as application_settings_default_enum

from pathlib import Path

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final
    from typing import List


# Folder Paths
# ---------------
TEST_DIR: Final = os.path.dirname(os.path.abspath(__file__))
PROJECT_MAIN_FOLDER: Final = pathlib.Path(__file__).parent.parent


# DO NOT CHANGE THE MONACO CUTOUT-FILE, CUTOUT-PARSER DEPENDS ON IT
# -----------------------------------------------------------------
# This file is here, so you can easily define path relative to here

# Defining Test Categories
# -------------------------
osm_element_1_default_value = default_value_entry_i.DefaultValueEntry("building")
osm_element_1_default_value.set_attribute_default(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, 1)
osm_element_1_default_value.set_attribute_default(attribute_enum_i.Attribute.PROPERTY_AREA, 1)
osm_element_1_default_value.set_attribute_default(attribute_enum_i.Attribute.FLOOR_AREA, 1)

whitelist: List = ["building=*"]
TEST_CATEGORY_SITE_AREA: Final = category_i.Category("building_category_site_area")
TEST_CATEGORY_SITE_AREA.set_whitelist(whitelist)

for member in attribute_enum_i.Attribute:
    TEST_CATEGORY_SITE_AREA.set_attribute(member, True)

TEST_CATEGORY_SITE_AREA.set_calculation_method_of_area(calculation_method_of_area_enum_i.CalculationMethodOfArea.CALCULATE_SITE_AREA)
TEST_CATEGORY_SITE_AREA.add_default_value_entry(osm_element_1_default_value)

whitelist: List = ["building=*"]
TEST_CATEGORY_BUILDING_AREA: Final = category_i.Category("building_category_building_area")
TEST_CATEGORY_BUILDING_AREA.set_whitelist(whitelist)
for member in attribute_enum_i.Attribute:
    TEST_CATEGORY_BUILDING_AREA.set_attribute(member, True)
TEST_CATEGORY_BUILDING_AREA.set_calculation_method_of_area(calculation_method_of_area_enum_i.CalculationMethodOfArea.CALCULATE_BUILDING_AREA)
TEST_CATEGORY_BUILDING_AREA.add_default_value_entry(osm_element_1_default_value)

blacklist: List = ["building=*"]
TEST_CATEGORY_NO_BUILDING: Final = category_i.Category("no_building_category")
TEST_CATEGORY_NO_BUILDING.set_blacklist(blacklist)
for member in attribute_enum_i.Attribute:
    TEST_CATEGORY_NO_BUILDING.set_attribute(member, True)
TEST_CATEGORY_NO_BUILDING.add_default_value_entry(osm_element_1_default_value)

blacklist: List = ["shop=*"]
TEST_CATEGORY_SHOP: Final = category_i.Category("shop_category")
TEST_CATEGORY_SHOP.set_whitelist(blacklist)
for member in attribute_enum_i.Attribute:
    TEST_CATEGORY_SHOP.set_attribute(member, True)
TEST_CATEGORY_SHOP.add_default_value_entry(osm_element_1_default_value)


# Define attractivity attributes
TEST_ATTRACTIVITY_COOLNESS: Final = attractivity_attribute.AttractivityAttribute("coolness")
TEST_ATTRACTIVITY_COOLNESS.set_base_factor(0)
TEST_ATTRACTIVITY_COOLNESS.set_attribute_factor(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, 1)
TEST_ATTRACTIVITY_COOLNESS.set_attribute_factor(attribute_enum_i.Attribute.FLOOR_AREA, 1)
TEST_ATTRACTIVITY_COOLNESS.set_attribute_factor(attribute_enum_i.Attribute.PROPERTY_AREA, 0)

TEST_ATTRACTIVITY_TRADING: Final = attractivity_attribute.AttractivityAttribute("trading")
TEST_ATTRACTIVITY_TRADING.set_base_factor(100)
TEST_ATTRACTIVITY_TRADING.set_attribute_factor(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, 1)
TEST_ATTRACTIVITY_TRADING.set_attribute_factor(attribute_enum_i.Attribute.FLOOR_AREA, 2)
TEST_ATTRACTIVITY_TRADING.set_attribute_factor(attribute_enum_i.Attribute.PROPERTY_AREA, 3)

TEST_ATTRACTIVITY_TRADING2: Final = attractivity_attribute.AttractivityAttribute("trading")
TEST_ATTRACTIVITY_TRADING2.set_base_factor(42)
TEST_ATTRACTIVITY_TRADING2.set_attribute_factor(attribute_enum_i.Attribute.NUMBER_OF_FLOOR, 0)
TEST_ATTRACTIVITY_TRADING2.set_attribute_factor(attribute_enum_i.Attribute.FLOOR_AREA, 0)
TEST_ATTRACTIVITY_TRADING2.set_attribute_factor(attribute_enum_i.Attribute.PROPERTY_AREA, 0)

# Set attractivities of categories
TEST_CATEGORY_BUILDING_AREA.add_attractivity_attribute(TEST_ATTRACTIVITY_COOLNESS)
TEST_CATEGORY_BUILDING_AREA.add_attractivity_attribute(TEST_ATTRACTIVITY_TRADING)
TEST_CATEGORY_NO_BUILDING.add_attractivity_attribute(TEST_ATTRACTIVITY_TRADING2)
TEST_CATEGORY_SHOP.add_attractivity_attribute(TEST_ATTRACTIVITY_COOLNESS)


# Defining Test Category Manager
# -------------------------
CATEGORY_MANAGER = category_manager_i.CategoryManager()
CATEGORY_MANAGER.add_categories([TEST_CATEGORY_SITE_AREA, TEST_CATEGORY_NO_BUILDING, TEST_CATEGORY_SHOP])


# Define example APPLICATIONSettings
APPLICATION_MANAGER: Final = application_settings.ApplicationSettings(Path(os.path.join(TEST_DIR, "build/example_settings/settings.json")))
APPLICATION_MANAGER.set_setting(application_settings_default_enum.ApplicationSettingsDefault.NUMBER_OF_PROCESSES, 1)

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