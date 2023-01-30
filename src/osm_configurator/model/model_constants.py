from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final

"""
This file is used, to name the columns in the Dataframe.
"""

# Dataframe column(CL) names
# ----------------------------
CL_OSM_TYPE: Final = "osm_type"
CL_TAGS: Final = "tags"
CL_CATEGORY: Final = "category"
CL_GEOMETRY: Final = "geometry"
CL_TRAFFIC_CELL_NAME: Final = "traffic_cell_name"
CL_OSM_ELEMENT_NAME: Final = "element_name"
CL_AREA_PROPERTY: Final = "area_property"
CL_BUILDING_PROPERTY: Final = "building_area"

# Misc
# -----
STANDARD_OSM_ELEMENT_NAME: Final = "missing"
DONT_CARE_SYMBOL: Final = "*"

# Name of osm elements
# ---------------------
NODE_NAME: Final = "node"
AREA_WAY_NAME: Final = "area-way"
AREA_RELATION_NAME: Final = "area-relation"

# Columns of the dataframe for each phase
# ---------------------------------------
DF_CL_TAG_FILTER_PHASE: Final = [CL_OSM_TYPE,
                                 CL_OSM_ELEMENT_NAME,
                                 CL_GEOMETRY,
                                 CL_TAGS,
                                 CL_CATEGORY
                                 ]

DF_CL_REDUCTION_PHASE: Final = [CL_OSM_TYPE,
                                CL_OSM_ELEMENT_NAME,
                                CL_GEOMETRY,
                                CL_TAGS,
                                CL_CATEGORY,
                                CL_AREA_PROPERTY,
                                CL_BUILDING_PROPERTY
                                ]