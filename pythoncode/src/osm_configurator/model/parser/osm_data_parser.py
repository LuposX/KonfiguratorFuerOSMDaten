from src.osm_configurator.model.parser.osm_data_parser_interface import OSMDataParserInterface


class OSMDataParser(OSMDataParserInterface):
    __doc__ = OSMDataParserInterface.__doc__

    def __init__(self):
        """
        Creates a new instance of the CategoryParser.
        """
        pass

    def parse_osm_data_file(self, path):
        # opening the file
        with open(path.absolute(), "r") as traffic_cell_file:

