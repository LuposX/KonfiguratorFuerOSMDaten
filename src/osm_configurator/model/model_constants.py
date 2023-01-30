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

# Misc
# -----
STANDARD_OSM_ELEMENT_NAME: Final = "missing"
DONT_CARE_SYMBOL: Final = "*"

# Name of osm elements
# ---------------------
NODE_NAME: Final = "node"
AREA_WAY_NAME: Final = "area-way"
AREA_RELATION_NAME: Final = "area-relation"