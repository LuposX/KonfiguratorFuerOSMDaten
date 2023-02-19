import pathlib

import matplotlib

from src.osm_configurator.control.data_visualization_controller_interface import IDataVisualizationController


class DataVisualizationControllerStub(IDataVisualizationController):
    def generate_cut_out_map(self) -> pathlib.Path:
        return pathlib.Path("")

    def get_calculation_visualization(self):
        return
