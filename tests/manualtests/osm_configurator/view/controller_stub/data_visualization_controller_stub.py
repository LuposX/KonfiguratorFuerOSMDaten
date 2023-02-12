import pathlib

import matplotlib

from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController


class DataVisualizationControllerStub(IDataVisualizationController):
    def generate_cut_out_map(self) -> pathlib.Path:
        pass

    def get_calculation_visualization(self):
        pass
