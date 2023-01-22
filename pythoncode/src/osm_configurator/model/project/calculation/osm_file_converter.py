from __future__ import annotations

import pathlib
import src.osm_configurator.model.project.calculation.osm_file_format_enum


class OSMFileConverter:
    """
    This class handles osm file conversion, it is used to transform an osm data file
    from one format to the others.
    For more on the different file format check "calculation.OSMFileFormat" out.
    """

    def __init__(self, origin_path, target_path):
        """
        Creates a new instance of "OSMFileConverter".

        Args:
            origin_path (pathlib.Path): The path pointing towards the file which format we want to transform into another format.
            target_path (pathlib.Path): The path pointing towards the place, where we want the translated file o be
        """
        pass

    def convert_file(self, data_format):
        """
        Transforms an osm file format into another osm file format.
        Allowed format: ".pbf", ".osm.bz2", ".osm".

        Args:
            data_format (osm_file_format_enum.OSMFileFormat): In which osm file format we want to transform our file into.

        Returns:
            bool: True if successful, otherwise false.
        """
        pass
