from __future__ import annotations

import os.path
import subprocess
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
        self.origin_path = origin_path
        self.target_path = target_path

    def convert_file(self, data_format):
        """
        Transforms an osm file format into another osm file format.
        Allowed format: ".pbf", ".osm.bz2", ".osm".

        Args:
            data_format (osm_file_format_enum.OSMFileFormat): In which osm file format we want to transform our file into.

        Returns:
            bool: True if successful, otherwise false.
        """

        # Return false, if origin does not exist; target does exist or suffix of target is wrong
        if not os.path.exists(self.origin_path) or os.path.exists(self.target_path):
            return False
        if self.target_path.suffix != data_format.get_file_extension():
            print(self.target_path.suffix + " " + data_format.get_file_extension())
            return False

        # Create subprocess to call osmium and convert the file
        result = subprocess.run(
            ["osmium", "cat", str(self.origin_path), "-o", str(self.target_path)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("rt: " + str(result.returncode), " stout: " + str(result.stdout), " stderr: " + str(result.stderr))

        return result.returncode == 0
