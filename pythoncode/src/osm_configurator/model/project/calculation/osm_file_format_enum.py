from __future__ import annotations

from enum import Enum, unique


@unique
class OSMFileFormat(Enum):
    """
    This enum describes the different osm file formats we use for file_conversion.
    For more information on the osm file formats check this out: https://wiki.openstreetmap.org/wiki/OSM_file_formats.
    """

    PBF = ".pbf"
    BZ2 = ".osm.bz2"
    OSM = ".osm"

    def get_file_extension(self):
        """
        Getter for the file extension of an enum type.

        Returns:
            str: The File extension the osm file format uses.
        """
        pass
