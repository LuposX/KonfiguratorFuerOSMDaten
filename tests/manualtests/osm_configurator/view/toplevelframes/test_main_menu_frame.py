import src.osm_configurator.view.states.main_window as mw
from tests.manualtests.osm_configurator.view.controller_stub.category_controller_stub import CategoryControllerStub

from tests.manualtests.osm_configurator.view.controller_stub.export_controller_stub import ExportControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.category_controller_stub import CategoryControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.project_controller_stub import ProjectControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.settings_controller_stub import SettingsControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.aggregation_controller_stub import AggreationControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.cut_out_controller_stub import CutOutControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.data_visualization_controller_stub import DataVisualizationControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.osm_data_controller_stub import OSMDataControllerStub
from tests.manualtests.osm_configurator.view.controller_stub.calculation_controller_stub import CalculationControllerStub



# This Test will perform manual tests on the main window
export_controller = IExportController()
category_controller = ICategoryController()
project_controller = IProjectController()
settings_controller = ISettingsController()
aggregation_controller = IAggregationController()
calculation_controller = ICalculationController()
cut_out_controller = ICutOutController()
data_visualization_controller = IDataVisualizationController()
osm_data_controller = IOSMDataController()


def test_display_main_window():
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
