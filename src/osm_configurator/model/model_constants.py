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
CL_GEOMETRY: Final = "geometry"  # THIS IS NOT ALLOWED TO BE SET TO A DIFFERENT VALUE, GEOPANDAS RELIES ON THIS NAME.
CL_TRAFFIC_CELL_NAME: Final = "traffic_cell_name"
CL_OSM_ELEMENT_NAME: Final = "element_name"
CL_AREA: Final = "area"

CL_AREA_WITHOUT_FLOORS: Final = "area_of_osm_element"
CL_AREA_WITH_FLOORS: Final = "area_of_osm_element_with_floors"
CL_NUMBER_OF_FLOORS: Final = "number_of_floors"


# Misc
# -----
STANDARD_OSM_ELEMENT_NAME: Final = "missing"
DONT_CARE_SYMBOL: Final = "*"

DEFAULT_DEFAULT_VALUE_ENTRY_TAG: Final = "default"

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

DF_CL_REDUCTION_PHASE_WITHOUT_ATTRIBUTES: Final = [CL_OSM_TYPE,
                                                   CL_OSM_ELEMENT_NAME,
                                                   CL_GEOMETRY,
                                                   CL_TAGS,
                                                   CL_CATEGORY,
                                                   ]
