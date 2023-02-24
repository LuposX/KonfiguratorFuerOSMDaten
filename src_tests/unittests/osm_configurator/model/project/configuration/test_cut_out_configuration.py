import os
from pathlib import Path

from src.osm_configurator.model.project.configuration.cut_out_configuration import CutOutConfiguration
from src.osm_configurator.model.project.configuration.cut_out_mode_enum import CutOutMode
from src_tests.definitions import TEST_DIR


class TestCutOutConfiguration:

    def test_get_cut_out_mode(self):
        self.cut_out_configurator: CutOutConfiguration = CutOutConfiguration()
        assert self.cut_out_configurator.get_cut_out_mode() == CutOutMode.BUILDINGS_ON_EDGE_ACCEPTED

    def test_set_cut_out_mode(self):
        self.cut_out_configurator: CutOutConfiguration = CutOutConfiguration()
        self.cut_out_configurator.set_cut_out_mode(CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED)
        assert self.cut_out_configurator.get_cut_out_mode() == CutOutMode.BUILDINGS_ON_EDGE_NOT_ACCEPTED

    def test_get_cut_out_path(self):
        self.cut_out_configurator: CutOutConfiguration = CutOutConfiguration()
        assert self.cut_out_configurator.get_cut_out_path() is None

    def test_set_cut_out_path(self):
        self.cut_out_configurator: CutOutConfiguration = CutOutConfiguration()
        self.cut_out_configurator.set_cut_out_path(Path(os.path.join(TEST_DIR, "build/Projects")))
        assert self.cut_out_configurator.get_cut_out_path() == Path(os.path.join(TEST_DIR, "build/Projects"))

