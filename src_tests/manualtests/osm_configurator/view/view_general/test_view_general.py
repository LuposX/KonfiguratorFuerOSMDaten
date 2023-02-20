import src.osm_configurator.view.states.main_window as mw

from src_tests.manualtests.osm_configurator.view.controller_stub.export_controller_stub import ExportControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.category_controller_stub import CategoryControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.project_controller_stub import ProjectControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.settings_controller_stub import SettingsControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.aggregation_controller_stub import AggregationControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.cut_out_controller_stub import CutOutControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.data_visualization_controller_stub import \
    DataVisualizationControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.osm_data_controller_stub import OSMDataControllerStub
from src_tests.manualtests.osm_configurator.view.controller_stub.calculation_controller_stub import \
    CalculationControllerStub

import src.osm_configurator.view.states.state_name_enum as state_name_enum_i

# This Test will perform manual tests on the main window
export_controller = ExportControllerStub()
category_controller = CategoryControllerStub()
project_controller = ProjectControllerStub()
settings_controller = SettingsControllerStub()
aggregation_controller = AggregationControllerStub()
calculation_controller = CalculationControllerStub()
cut_out_controller = CutOutControllerStub()
data_visualization_controller = DataVisualizationControllerStub()
osm_data_controller = OSMDataControllerStub()

def test_view_general():
    main_window = mw.MainWindow(export_controller=export_controller,
                                category_controller=category_controller,
                                project_controller=project_controller,
                                settings_controller=settings_controller,
                                aggregation_controller=aggregation_controller,
                                calculation_controller=calculation_controller,
                                cut_out_controller=cut_out_controller,
                                data_visualization_controller=data_visualization_controller,
                                osm_data_controller=osm_data_controller,
                                )

    main_window.start_main_window()