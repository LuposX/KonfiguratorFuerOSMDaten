import os
from pathlib import Path

from src.osm_configurator.model.project.configuration.osm_data_configuration import OSMDataConfiguration
from src_tests.definitions import TEST_DIR


class TestOSMDataConfiguration:
    def test_get_osm_data(self):
       self.osm_data_configuration: OSMDataConfiguration = OSMDataConfiguration()
       assert self.osm_data_configuration.get_osm_data() is None

    def test_set_osm_data(self):
       self.osm_data_configuration: OSMDataConfiguration = OSMDataConfiguration()
       self.osm_data_configuration.set_osm_data(Path(os.path.join(TEST_DIR, "build/Projects")))
       assert self.osm_data_configuration.get_osm_data() == Path(os.path.join(TEST_DIR, "build/Projects"))