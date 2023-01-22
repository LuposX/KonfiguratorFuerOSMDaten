from __future__ import annotations

from src.osm_configurator.model.parser.cut_out_parser_interface import CutOutParserInterface
import geopandas as gpd
import os


class CutOutParser(CutOutParserInterface):
    __doc__ = CutOutParserInterface.__doc__

    def __int__(self):
        """
        Creates a new instance of the CutOutParser.
        """
        pass

    def parse_cutout_file(self, path):
        df = gpd.read_file(path)
        if 'name' not in df.columns:
            df["name"] = df.index

        return df
